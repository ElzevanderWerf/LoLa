"""Write 3 Google Apps Script functions that generate different forms in 
Google Forms, results in folder `scripts`. The .gs files can be run from 
script.google.com. A template of the form is imported from my personal Google
Account, so unfortunately this cannot be replicated."""

import pandas as pd

# Import items
nli1_df = pd.read_csv("experimental_items/nli-items1.csv", header=0, error_bad_lines=False, encoding="utf-8")
nli2_df = pd.read_csv("experimental_items/nli-items2.csv", header=0, error_bad_lines=False, encoding="utf-8")
nli3_df = pd.read_csv("experimental_items/nli-items3.csv", header=0, error_bad_lines=False, encoding="utf-8")
fr_df = pd.read_csv("experimental_items/fr-items123.csv", header=0, error_bad_lines=False, encoding="utf-8")


def makeNLI(premise, hypothesis, index):
    return [r'var nli' + str(index) + r' = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\n'
              + premise
              + r'\n\nHypothesis:\n' 
              + hypothesis 
              + r'").setChoiceValues(["Yes", "No"]).showOtherOption(true).setHelpText("Pick the third answer option if it is unclear whether the hypothesis follows from the premise (e.g., if the premise is open to multiple interpretations, or if you do not understand the premise or hypothesis), and explain why.").setRequired(true);'] #TODO add I don't know., delete otherOption

def makeScript(nli_df, fr_df, index):
    # Lists of item variables
    nliNumber = len(nli1_df)
    frNumber = len(fr_df)
    
    script = []     # a list of lines to be part of the final script
    
    # open function
    script += [r'function main' + str(index) + r'() {']
    
    # copy form from existing template with UU theme and set title
    script += [r'var file = DriveApp.getFileById("1LYuXRnB1Q4enFnlhA-wvr90vFIJjG8YB0EdBs4RZSTs").makeCopy("Form 2.'+ str(index) + r'");']
    script += [r'var form = FormApp.openById(file.getId());']
    script += [r'form.setTitle("Natural Language Inference & Fluency Ranking");']
    script += ['']
    
    # copied from template: instruction + informed consent, personal questions, instructions NLI task
    
    # the NLI questions
    
    for item_i in range(nliNumber):
        hypothesis = nli_df.loc[item_i, "Hypothesis"]
        premise = nli_df.loc[item_i, "Translation"]
        script += makeNLI(premise, hypothesis, item_i+1)
       
    # the FR instructions
    script += ['']
    script += [r'form.addPageBreakItem().setTitle("Fluency Ranking").setHelpText("The purpose of this second (and final) task, which is called a Fluency Ranking task, is to evaluate the fluency of English translations from first-order logic formulas. We will present to you, one by one, 20 formulas with 3 candidate translations, like in the example below:\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\nFormula:\t\t\t¬ ∃ x ( Cube ( x ) ∧ LeftOf ( 𝗕 , x ) )\n\nTranslation 1:\t\tThere is no element x such that x is a cube and 𝗕 is to the left of x.\nTranslation 2:\t\tIt is not the case that there is an element x such that x is a cube and 𝗕 is to the left of x.\nTranslation 3:\t\tFor all cubes x, 𝗕 is not to the left of x or x is not even.\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nPlease rank the translations by the criterion of 𝗳𝗹𝘂𝗲𝗻𝗰𝘆, where rank 1 stands for the most fluent, and 3 for the least fluent translation. By a fluent translation, we mean a translation that sounds as a natural English sentence. In ranking, ties are allowed. So, for example, if you think Translation 1 is best and Translation 2 and 3 are equally bad, give Translation 1 the highest rank (1), and Translation 2 and 3 the next highest rank (2), assigning nothing to the third rank.\n\nIn ranking the translations, please note that it is very important that you evaluate the fluency of the translations based only on the form of the translations (not on their adequacy given the formula). It can happen that two candidate translations are exactly the same. Please assign them the same rank always.\n\nFor your information, these are the interpretations of the predicates used in the formulas:\nDodec ( x )\t\t\tx is a dodecahedron\nSmall ( x )\t\t\tx is small\nStudent ( x )\t\t\tx is a student\nMedium ( x )\t\tx is medium\nCube ( x )\t\t\tx is a cube\nPrime ( x )\t\t\tx is a prime\nPerson ( x )\t\t\tx is a person\nTet ( x )\t\t\t\tx is a tetrahedron\nPet ( x )\t\t\t\tx is a pet\nLarge ( x )\t\t\tx is large\nEven ( x )\t\t\tx is even\nAdjoins ( x , y )\t\tx is adjacent to y\nSameCol ( x , y )\t\tx is in the same column as y\nLeftOf ( x , y )\t\tx is to the left of y\nRightOf ( x , y )\t\tx is to the right of y\nSmaller ( x , y )\t\tx is smaller than y\nFrontOf ( x , y )\t\tx is in front of y\nLarger ( x , y )\t\tx is larger than y\nSameRow ( x , y )\tx is in the same row as y\nSameShape ( x , y )\tx is the same shape as y\nSameSize ( x , y )\tx is the same size as y\nBackOf ( x , y )\t\tx is in back of y");']
    
    # the FR questions
    for item_i in range(frNumber):
        formula = fr_df.loc[item_i, "Formula"]
        t1 = fr_df.loc[item_i, fr_df.loc[item_i, "Translation 1"]]
        t2 = fr_df.loc[item_i, fr_df.loc[item_i, "Translation 2"]]
        t3 = fr_df.loc[item_i, fr_df.loc[item_i, "Translation 3"]]
        script += [r'var fr' + str(item_i+1) + r' = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n'
                   + formula
                   + r'\n\n\nTranslation 1:\n'
                   + t1
                   + r'\n\nTranslation 2:\n'
                   + t2
                   + r'\n\nTranslation 3:\n'
                   + t3
                   + r'").setHelpText("Base your ranking only on the criterion of fluency (how natural the sentence sounds in English). Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);']
    
    
    # final questions
    script += ['']
    script += [r'final = form.addPageBreakItem().setTitle("Final question");']
    script += [r'form.addParagraphTextItem().setTitle("Do you have any final comments on the survey?");']
    script += ['']
    
    # Write results to spreadsheet
    script += [r'var ss = SpreadsheetApp.create("2.' + str(index) + r'. results");']
    script += [r'form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());']
    script += [r'var folder = DriveApp.getFoldersByName("AI MSc Thesis Exp2").next();']
    script += [r'folder.addFile(DriveApp.getFileById(ss.getId()));']
    script += [r'DriveApp.getRootFolder().removeFile(DriveApp.getFileById(ss.getId()));']
    
    # close function
    script += [r'}']
    
    return script
            
script1 = makeScript(nli1_df, fr_df, 1)
script2 = makeScript(nli2_df, fr_df, 2)
script3 = makeScript(nli3_df, fr_df, 3)

with open('formScripts/script1.gs', 'w', encoding="utf-8") as f:
    f.writelines("%s\n" % l for l in script1)
    
with open('formScripts/script2.gs', 'w', encoding="utf-8") as f:
    f.writelines("%s\n" % l for l in script2)
    
with open('formScripts/script3.gs', 'w', encoding="utf-8") as f:
    f.writelines("%s\n" % l for l in script3)