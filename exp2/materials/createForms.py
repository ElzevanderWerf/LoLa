"""Write 3 Google Apps Script functions that generate different forms in 
Google Forms, results in folder `scripts`. The .gs files can be run from 
script.google.com. A template of the form is imported from my personal Google
Account, so unfortunately this cannot be replicated."""

import pandas as pd

# Import items
nli_df = pd.read_csv("data/nli-items.csv", header=0, error_bad_lines=False, encoding="utf-8")
fr_df = pd.read_csv("data/fr-items.csv", header=0, error_bad_lines=False, encoding="utf-8")
    

# Lists of item variables
nliNumber = len(nli_df)
frNumber = len(fr_df)

script = []     # a list of lines to be part of the final script

# open function
script += [r'function main0() {']

# copy form from existing template with UU theme and set title
script += [r'var file = DriveApp.getFileById("1LYuXRnB1Q4enFnlhA-wvr90vFIJjG8YB0EdBs4RZSTs").makeCopy("Form 2.0");']
script += [r'var form = FormApp.openById(file.getId());']
script += [r'form.setTitle("Natural Language Inference & Fluency Ranking");']
script += ['']

# copied from template: instruction + informed consent, personal questions, instructions NLI task

# the NLI questions
def makeNLI(premise, hypothesis, index):
    return [r'var nli' + str(index) + r' = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\t'
              + premise
              + r'\nHypothesis:\t' 
              + hypothesis 
              + r'").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);'] #TODO add I don't know., delete otherOption

index = 0
for item_i in range(nliNumber):
    hypothesis = nli_df.loc[item_i, "Hypothesis"]
    index += 1
    script += makeNLI(nli_df.loc[item_i, "Baseline"], hypothesis, index)
    index += 1
    script += makeNLI(nli_df.loc[item_i, "RantaI"], hypothesis, index)
    index += 1
    script += makeNLI(nli_df.loc[item_i, "RantaII"], hypothesis, index)
   
# the FR instructions
script += ['']
script += [r'form.addPageBreakItem().setTitle("Fluency Ranking").setHelpText("The purpose of this task is to evaluate the fluency of English translations from first-order logic formulas. We will present to you, one by one, 20 formulas with 3 candidate translations, like in the example below:\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\nFormula:\t\t\t¬ ∃ x ( Cube ( x ) ∧ LeftOf ( b , x ) )\n\nTranslation 1:\t\tIt is not the case that b is to the left of some cube.\nTranslation 2:\t\tIt is not the case that there exists an element x such that x is a cube and b is to the left of x.\nTranslation 3:\t\tFor all x, b is not to the left of x or x is not even.\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nPlease rank the translations by the criterion of 𝗳𝗹𝘂𝗲𝗻𝗰𝘆, where rank 1 stands for the most fluent, and 3 for the least fluent translation. By a fluent translation, we mean a translation that sounds as a natural English sentence. In ranking, ties are allowed. So, for example, if you think Translation 1 is best and Translation 2 and 3 are equally bad, give Translation 1 the highest rank (1), and Translation 2 and 3 the next highest rank (2), assigning nothing to the third rank.\n\nFor your information, these are the interpretations of the predicates used in the formulas:\nDodec ( x )\t\tx is a dodecahedron\nSmall ( x )\t\tx is small\nStudent ( x )\t\tx is a student\nMedium ( x )\t\tx is medium\nCube ( x )\t\tx is a cube\nPrime ( x )\t\tx is a prime\nPerson ( x )\t\tx is a person\nTet ( x )\t\tx is a tetrahedron\nPet ( x )\t\tx is a pet\nLarge ( x )\t\tx is large\nEven ( x )\t\tx is even\nAdjoins ( x , y )\t\tx is adjacent to y\nSameCol ( x , y )\t\tx is in the same column as y\nLeftOf ( x , y )\t\tx is to the left of y\nRightOf ( x , y )\t\tx is to the right of y\nSmaller ( x , y )\t\tx is smaller than y\nFrontOf ( x , y )\t\tx is in front of y\nLarger ( x , y )\t\tx is larger than y\nSameRow ( x , y )\t\tx is in the same row as y\nSameShape ( x , y )\t\tx is the same shape as y\nSameSize ( x , y )\t\tx is the same size as y\nBackOf ( x , y )\t\tx is in back of y");']

# the FR questions
for item_i in range(frNumber):
    formula = fr_df.loc[item_i, "Formula"]
    t1 = fr_df.loc[item_i, fr_df.loc[item_i, "Translation 1"]]
    t2 = fr_df.loc[item_i, fr_df.loc[item_i, "Translation 2"]]
    t3 = fr_df.loc[item_i, fr_df.loc[item_i, "Translation 3"]]
    script += [r'var fr' + str(item_i) + r' = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\t'
               + formula
               + r'\n\nTranslation 1:\t'
               + t1
               + r'\nTranslation 2:\t'
               + t2
               + r'\nTranslation 3:\t'
               + t3
               + r'").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);']


# final questions
script += ['']
script += [r'final = form.addPageBreakItem().setTitle("Final question");']
script += [r'form.addParagraphTextItem().setTitle("Do you have any final comments on the survey?");']
script += ['']

# Form settings
script += [r'var ss = SpreadsheetApp.create("2.0. results");']
script += [r'form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());']

# close function
script += [r'}']
        

with open('formScripts/script0.gs', 'w', encoding="utf-8") as f:
    f.writelines("%s\n" % l for l in script)