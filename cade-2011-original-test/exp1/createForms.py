"""Write 20 Google Apps Script functions that generate different forms in 
Google Forms, results in folder `scripts`. The .gs files can be run from 
script.google.com. The batches of experimental items are written to folder 
`batches`."""

import pandas as pd

# Initialization
numberOfForms = 30      # The number of different forms to generate
numberOfItems = 25      # The number of experimental items

ggc_df = pd.read_csv("exp1-ggc-to-eng.csv", header=0, error_bad_lines=False, encoding="utf-8")
rg_df = pd.read_csv("exp1-rg-to-eng.csv", header=0, error_bad_lines=False, encoding="utf-8")
fillers_df = pd.read_csv("fillers.csv", header=0, error_bad_lines=False, sep=";", encoding="utf-8")

# The formula sets for each batch taken from the DataFrames
batches = []
for i in range(numberOfForms):
    ggc_10 = [tuple(ft) for ft in ggc_df.iloc[i*10:i*10+10, 1:3].to_numpy()]
    rg_10 = [tuple(ft) for ft in rg_df.iloc[i*10:i*10+10, 1:3].to_numpy()]
    fillers_5 = [tuple(ft) for ft in fillers_df.iloc[:5, 1:3].to_numpy() ]
    batch = ggc_10+rg_10+fillers_5
    
    batch_df = pd.DataFrame(batch, columns = ["Formula", "Translation"])
    batch_df.insert(loc=0, 
                    column = "Condition",
                    value = 10 * ["GGC"] + 10 * ["RG"] + 5 * ["Filler"])
    batch_df.to_csv(
        "batches/batch"+ str(i+1) + ".csv", sep=',')
    
    batches.append(batch)
    

# Lists of item variables
items = ['item'+str(n) for n in range(1, numberOfItems+1)]

scripts = []
for form_i in range(numberOfForms):
    script = []     # a list of lines to be part of the final script
    
    # open function
    script += [r'function main' + str(form_i+1) + r'() {']
    
    # copy form from existing template with UU theme and set title
    script += [r'var file = DriveApp.getFileById("1brt4qB9t1gXp4q93JaMCuNRmO22LRAb-CtPXK4mWp2k").makeCopy("1.' + str(form_i+1) + r' Evaluating English translations from First-Order Logic formulae");']
    script += [r'var form = FormApp.openById(file.getId());']
    script += [r'form.setTitle("1.' + str(form_i+1) + ' Evaluating English translations from First-Order Logic formulae");']
    script += ['']
    
    # instruction + informed consent
    script += [r'form.setDescription("Thank you very much for participating in this experiment. It will take approximately 15 to 30 minutes to fill in this survey. If at any point you would like to stop, you can close this form and your response will be deleted. If you do wish to participate, your response will be handled anonymously: The information in this study will only be used in ways that will not reveal who you are. You will not be identified in any publication from this study or in any data files shared with other researchers. Your participation in this study is confidential. \n\nThe purpose of this experiment is to evaluate the strengths and weaknesses of a system that translates first-order logic formulas into English. We will present to you, one by one, 25 formulas with their translations, such as the one below:\n\n\tFormula:\t\t\t\t¬ ∃ x ( Cube ( x ) ∧ LeftOf ( b , x ) )\n\tEnglish translation:\t\tIt is not the case that b is to the left of some cube\n\nPlease answer the following questions for each of them:\n\t1. Is the translation 𝗰𝗼𝗿𝗿𝗲𝗰𝘁, yes or no? By a correct translation, we mean that the sentence conveys the same information as the input logical formula (there is no possible world in which the formula is true while the English translation is false, or vice versa).\n\t2. Is the translation 𝗰𝗹𝗲𝗮𝗿? By a clear translation, we mean that the sentence is understandable and does not have multiple readings.\n\t3. Is the translation 𝗳𝗹𝘂𝗲𝗻𝘁? By a fluent translation, we mean that the sentence sounds like a natural English sentence.\n\t4. Do you have a suggestion for a 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗶𝗼𝗻? Think, for example, about how the translation can be improved given the above three criteria (correctness, clarity, and fluency). However, you can be very free in your ideas here, write whatever you like! \n\n𝗬𝗼𝘂𝗿 𝗮𝗻𝘀𝘄𝗲𝗿 𝘁𝗼 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻 𝟰 𝗶𝘀 𝗺𝗼𝘀𝘁 𝗶𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁 𝗳𝗼𝗿 𝘂𝘀. Especially if you think the given translation is unclear and/or not fluent, write down a translation that you think is more understandable and/or sounds better. A translation should always be one or more whole sentences.\n\nIn answering all questions, please note that it is very important that you evaluate the quality of the translations and base your opinion only on the semantic content (the meaning) of the formula, not on its specific syntactic form (such as the order of the conjuncts). In other words, think about whether the translation is suitable given the formula\'s meaning, no matter what the formula looks like.\n\nThe survey will start off with a few personal questions and a practice example. After you have answered all of the questions for each formula and translation pair, you will be asked to give a general structured review of the strengths and weaknesses of the translation system. With which types of sentences does the system have difficulties? For which types of sentences do you believe the system performs sufficiently well? Please keep this final question in mind while evaluating the translations.\n\nFor your information, these are the interpretations of the predicates used:\nDodec ( x )\t\t\t\tx is a dodecahedron\nSmall ( x )\t\t\t\tx is small\nStudent ( x )\t\t\t\tx is a student\nMedium ( x )\t\t\t\tx is medium\nCube ( x )\t\t\t\tx is a cube\nPrime ( x )\t\t\t\tx is a prime\nPerson ( x )\t\t\t\tx is a person\nTet ( x )\t\t\t\t\tx is a tetrahedron\nPet ( x )\t\t\t\t\tx is a pet\nLarge ( x )\t\t\t\tx is large\nEven ( x )\t\t\t\tx is even\nAdjoins ( x , y )\t\t\tx is adjacent to y\nSameCol ( x , y )\t\t\tx is in the same column as y\nLeftOf ( x , y )\t\t\tx is to the left of y\nRightOf ( x , y )\t\t\tx is to the right of y\nSmaller ( x , y )\t\t\tx is smaller than y\nFrontOf ( x , y )\t\t\tx is in front of y\nLarger ( x , y )\t\t\tx is larger than y\nSameRow ( x , y )\t\tx is in the same row as y\nSameShape ( x , y )\t\tx is the same shape as y\nSameSize ( x , y )\t\t\tx is the same size as y\nBackOf ( x , y )\t\t\tx is in back of y\n");']
    script += [r'informedConsent = form.addMultipleChoiceItem().setTitle("I have read the above information and understand the purpose of the research and that data will be collected from me. I also understand that participating in this study is completely voluntary. I agree that data gathered for the study may be published or made available provided my name or other identifying information is not used.").setRequired(true);']
    script += [r'var withDrawn = form.addPageBreakItem().setTitle("Withdrawn from participation").setHelpText("You are withdrawn from participation. You can close this window and your response will not be recorded.");']
    script += [r'var personalQs = form.addPageBreakItem().setTitle("Personal questions");']
    script += [r'var agreed = informedConsent.createChoice("I confirm this", personalQs);']
    script += [r'var disagreed = informedConsent.createChoice("I do not confirm this and want to withdraw from participation", withDrawn);']
    script += [r'informedConsent.setChoices([agreed, disagreed]);']
    script += ['']
    
    # personal questions
    script += [r'form.addMultipleChoiceItem().setTitle("What is your gender?").setChoiceValues(["Male", "Female", "Prefer not to say"]).setRequired(true);']
    script += [r'var ageValidation = FormApp.createTextValidation().setHelpText("Your answer should be a whole number greater than 0.").requireNumberGreaterThan(0).requireWholeNumber().build();']
    script += [r'form.addTextItem().setTitle("How old are you?").setRequired(true).setValidation(ageValidation);']
    script += [r'form.addScaleItem().setTitle("How would you rate your knowledge of and familiarity with first-order logic?").setBounds(1,5).setLabels("I have been introduced to logic but it is long ago and I am a bit rusty", "I use logic on a daily basis").setRequired(true);']
    script += ['']
    
    # two practice examples
    script += [r'var examples = form.addPageBreakItem().setTitle("Two examples").setHelpText("Here are two example formula-translation pairs with potential answers (but many more can be correct!) that would be helpful for us in thinking about how to improve the translation system:\n\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲 𝟭\n\nFormula:\t\t∀ x ∃ y ( ( LeftOf ( x , y ) ) ∧  ¬ Dodec ( y ) )\nTranslation:\t\tfor all x , there is an element y such that x is to the left of y and y is not a dodecahedron\n1. Is the translation 𝗰𝗼𝗿𝗿𝗲𝗰𝘁, yes or no?\n\t\"Yes\"\n\n2. Is the translation 𝗰𝗹𝗲𝗮𝗿, on a scale of 1 to 5?\n\t\"3\"\n\n3. Is the translation 𝗳𝗹𝘂𝗲𝗻𝘁, on a scale of 1 to 5?\n\t\"2\"\n\n4. Do you have a suggestion for a 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗶𝗼𝗻?\n\t\"everything has something to the right of it that is not a dodecahedron\"\n\n\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲 𝟮\n\nFormula:\t\tPet ( a ) → ∃ x Adjoins ( b , b )\nTranslation:\t\tif a is a pet , then there is an element x such that x is adjacent to b\n1. Is the translation 𝗰𝗼𝗿𝗿𝗲𝗰𝘁, yes or no?\n\t\"No\"\n\n2. Is the translation 𝗰𝗹𝗲𝗮𝗿, on a scale of 1 to 5?\n\t\"3\"\n\n3. Is the translation 𝗳𝗹𝘂𝗲𝗻𝘁, on a scale of 1 to 5?\n\t\"1\"\n\n4. Do you have a suggestion for a 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗶𝗼𝗻?\n\t\"if a is a pet, then b is adjacent to itself\"\n\n\nNow it is your turn!");']
    script += ['']
    
    # the questions per section (each section has one experimental item)
    for item_i in range(numberOfItems):
        script += [r'var ' + items[item_i] + r' = form.addPageBreakItem().setHelpText("Formula:\n'+ batches[form_i][item_i][0] +r'\n\nTranslation:\n'+ batches[form_i][item_i][1] + r'");']
        script += [r'form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);']
        script += [r'form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);']
        script += [r'form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);']
        script += [r'form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");']
        script += ['']
    
    # final questions
    script += ['']
    script += [r'final = form.addPageBreakItem().setTitle("Final questions");']
    script += [r'form.addParagraphTextItem().setTitle("Give a general structured review of the strengths and weaknesses of the translation system. With which types of formulas does the system have difficulties? For which types of formulas do you believe the system performs sufficiently well?").setRequired(true);']
    script += [r'form.addParagraphTextItem().setTitle("Do you have any final comments?");']
    script += ['']
    
    # Shuffle order view of sections for participants
    shuffled = ['item4', 'item22', 'item21', 'item19', 'item11', 'item15', 'item23', 
         'item16', 'item6', 'item3', 'item25', 'item5', 'item18', 'item12', 
         'item2', 'item20', 'item10', 'final', 'item14', 'item8',
         'item13', 'item24', 'item17', 'item7', 'item9', 'item1']
    for item_i in range(numberOfItems):
        script += [items[item_i] + r'.setGoToPage('+ shuffled[item_i] + r')']
    script += [r'final.setGoToPage(' + shuffled[-1] + r')']
    script += ['']
    
    # Form settings
    script += [r'var ss = SpreadsheetApp.create("1.' + str(form_i+1) + r' results");']
    script += [r'form.setConfirmationMessage("Thank you very much! Your response has been recorded.").setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId()).setShowLinkToRespondAgain(false);']
    
    # close function
    script += [r'}']
    
    scripts.append(script)
        
for script_i in range(numberOfForms):
    with open('scripts/script'+str(script_i+1)+'.gs', 'w', encoding="utf-8") as f:
        f.writelines("%s\n" % l for l in scripts[script_i])