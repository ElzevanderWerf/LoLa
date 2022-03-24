function main8() {
var file = DriveApp.getFileById("1brt4qB9t1gXp4q93JaMCuNRmO22LRAb-CtPXK4mWp2k").makeCopy("1.8 Evaluating English translations from First-Order Logic formulae");
var form = FormApp.openById(file.getId());
form.setTitle("1.8 Evaluating English translations from First-Order Logic formulae");

form.setDescription("Thank you very much for participating in this experiment. It will take approximately 15 to 30 minutes to fill in this survey. If at any point you would like to stop, you can close this form and your response will be deleted. If you do wish to participate, your response will be handled anonymously: The information in this study will only be used in ways that will not reveal who you are. You will not be identified in any publication from this study or in any data files shared with other researchers. Your participation in this study is confidential. \n\nThe purpose of this experiment is to evaluate the strengths and weaknesses of a system that translates first-order logic formulas into English. We will present to you, one by one, 25 formulas with their translations, such as the one below:\n\n\tFormula:\t\t\t\t¬ ∃ x ( Cube ( x ) ∧ LeftOf ( b , x ) )\n\tEnglish translation:\t\tIt is not the case that b is to the left of some cube\n\nPlease answer the following questions for each of them:\n\t1. Is the translation 𝗰𝗼𝗿𝗿𝗲𝗰𝘁, yes or no? By a correct translation, we mean that the sentence conveys the same information as the input logical formula (there is no possible world in which the formula is true while the English translation is false, or vice versa).\n\t2. Is the translation 𝗰𝗹𝗲𝗮𝗿? By a clear translation, we mean that the sentence is understandable and does not have multiple readings.\n\t3. Is the translation 𝗳𝗹𝘂𝗲𝗻𝘁? By a fluent translation, we mean that the sentence sounds like a natural English sentence.\n\t4. Do you have a suggestion for a 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗶𝗼𝗻? Think, for example, about how the translation can be improved given the above three criteria (correctness, clarity, and fluency). However, you can be very free in your ideas here, write whatever you like! \n\n𝗬𝗼𝘂𝗿 𝗮𝗻𝘀𝘄𝗲𝗿 𝘁𝗼 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻 𝟰 𝗶𝘀 𝗺𝗼𝘀𝘁 𝗶𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁 𝗳𝗼𝗿 𝘂𝘀. Especially if you think the given translation is unclear and/or not fluent, write down a translation that you think is more understandable and/or sounds better. A translation should always be one or more whole sentences.\n\nIn answering all questions, please note that it is very important that you evaluate the quality of the translations and base your opinion only on the semantic content (the meaning) of the formula, not on its specific syntactic form (such as the order of the conjuncts). In other words, think about whether the translation is suitable given the formula\'s meaning, no matter what the formula looks like.\n\nThe survey will start off with a few personal questions and a practice example. After you have answered all of the questions for each formula and translation pair, you will be asked to give a general structured review of the strengths and weaknesses of the translation system. With which types of sentences does the system have difficulties? For which types of sentences do you believe the system performs sufficiently well? Please keep this final question in mind while evaluating the translations.\n\nFor your information, these are the interpretations of the predicates used:\nDodec ( x )\t\t\t\tx is a dodecahedron\nSmall ( x )\t\t\t\tx is small\nStudent ( x )\t\t\t\tx is a student\nMedium ( x )\t\t\t\tx is medium\nCube ( x )\t\t\t\tx is a cube\nPrime ( x )\t\t\t\tx is a prime\nPerson ( x )\t\t\t\tx is a person\nTet ( x )\t\t\t\t\tx is a tetrahedron\nPet ( x )\t\t\t\t\tx is a pet\nLarge ( x )\t\t\t\tx is large\nEven ( x )\t\t\t\tx is even\nAdjoins ( x , y )\t\t\tx is adjacent to y\nSameCol ( x , y )\t\t\tx is in the same column as y\nLeftOf ( x , y )\t\t\tx is to the left of y\nRightOf ( x , y )\t\t\tx is to the right of y\nSmaller ( x , y )\t\t\tx is smaller than y\nFrontOf ( x , y )\t\t\tx is in front of y\nLarger ( x , y )\t\t\tx is larger than y\nSameRow ( x , y )\t\tx is in the same row as y\nSameShape ( x , y )\t\tx is the same shape as y\nSameSize ( x , y )\t\t\tx is the same size as y\nBackOf ( x , y )\t\t\tx is in back of y\n");
informedConsent = form.addMultipleChoiceItem().setTitle("I have read the above information and understand the purpose of the research and that data will be collected from me. I also understand that participating in this study is completely voluntary. I agree that data gathered for the study may be published or made available provided my name or other identifying information is not used.").setRequired(true);
var withDrawn = form.addPageBreakItem().setTitle("Withdrawn from participation").setHelpText("You are withdrawn from participation. You can close this window and your response will not be recorded.");
var personalQs = form.addPageBreakItem().setTitle("Personal questions");
var agreed = informedConsent.createChoice("I confirm this", personalQs);
var disagreed = informedConsent.createChoice("I do not confirm this and want to withdraw from participation", withDrawn);
informedConsent.setChoices([agreed, disagreed]);

form.addMultipleChoiceItem().setTitle("What is your gender?").setChoiceValues(["Male", "Female", "Prefer not to say"]).setRequired(true);
var ageValidation = FormApp.createTextValidation().setHelpText("Your answer should be a whole number greater than 0.").requireNumberGreaterThan(0).requireWholeNumber().build();
form.addTextItem().setTitle("How old are you?").setRequired(true).setValidation(ageValidation);
form.addScaleItem().setTitle("How would you rate your knowledge of and familiarity with first-order logic?").setBounds(1,5).setLabels("I have been introduced to logic but it is long ago and I am a bit rusty", "I use logic on a daily basis").setRequired(true);

var examples = form.addPageBreakItem().setTitle("Two examples").setHelpText("Here are two example formula-translation pairs with potential answers (but many more can be correct!) that would be helpful for us in thinking about how to improve the translation system:\n\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲 𝟭\n\nFormula:\t\t∀ x ∃ y ( ( LeftOf ( x , y ) ) ∧  ¬ Dodec ( y ) )\nTranslation:\t\tfor all x , there is an element y such that x is to the left of y and y is not a dodecahedron\n1. Is the translation 𝗰𝗼𝗿𝗿𝗲𝗰𝘁, yes or no?\n\t\"Yes\"\n\n2. Is the translation 𝗰𝗹𝗲𝗮𝗿, on a scale of 1 to 5?\n\t\"3\"\n\n3. Is the translation 𝗳𝗹𝘂𝗲𝗻𝘁, on a scale of 1 to 5?\n\t\"2\"\n\n4. Do you have a suggestion for a 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗶𝗼𝗻?\n\t\"everything has something to the right of it that is not a dodecahedron\"\n\n\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲 𝟮\n\nFormula:\t\tPet ( a ) → ∃ x Adjoins ( b , b )\nTranslation:\t\tif a is a pet , then there is an element x such that x is adjacent to b\n1. Is the translation 𝗰𝗼𝗿𝗿𝗲𝗰𝘁, yes or no?\n\t\"No\"\n\n2. Is the translation 𝗰𝗹𝗲𝗮𝗿, on a scale of 1 to 5?\n\t\"3\"\n\n3. Is the translation 𝗳𝗹𝘂𝗲𝗻𝘁, on a scale of 1 to 5?\n\t\"1\"\n\n4. Do you have a suggestion for a 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗶𝗼𝗻?\n\t\"if a is a pet, then b is adjacent to itself\"\n\n\nNow it is your turn!");

var item1 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ( ¬ ∃ y ( Dodec ( x ) → RightOf ( y , x ) ) → ∃ z RightOf ( x , z ) )\n\nTranslation:\nfor all x , if it is not the case that there is an element y such that if x is a dodecahedron , then y is to the right of x , then there is an element z such that x is to the right of z");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item2 = form.addPageBreakItem().setHelpText("Formula:\n¬ ∃ y ∃ x ( Cube ( x ) ∧ Cube ( y ) ∧ RightOf ( y , x ) )\n\nTranslation:\nit is not the case that there is an element y such that there is an element x such that x is a cube , y is a cube and y is to the right of x");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item3 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ∀ y ( ( Cube ( x ) ∧ SameSize ( x , y ) ) → ¬ Tet ( y ) )\n\nTranslation:\nfor all x , for all y , if x is a cube and x is of the same size as y , then y is not a tetrahedron");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item4 = form.addPageBreakItem().setHelpText("Formula:\n∃ x ( RightOf ( b , x ) ∧ Cube ( x ) ∧ Large ( x ) )\n\nTranslation:\nthere is an element x such that b is to the right of x , x is a cube and x is large");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item5 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ¬ ( Adjoins ( a , x ) ∨ Adjoins ( a , b ) )\n\nTranslation:\nfor all x , it is not the case that a is adjacent to x or adjacent to b");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item6 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ( Cube ( x ) → ∃ y ( Tet ( y ) ∧ LeftOf ( x , y ) ∧ SameSize ( y , x ) ) )\n\nTranslation:\nfor all cubes x , there is an element y such that y is a tetrahedron , x is to the left of y and y is of the same size as x");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item7 = form.addPageBreakItem().setHelpText("Formula:\n∀ u ∃ x ( Tet ( u ) → BackOf ( u , x ) )\n\nTranslation:\nfor all u , there is an element x such that if u is a tetrahedron , then u is in back of x");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item8 = form.addPageBreakItem().setHelpText("Formula:\n∀ y ( Dodec ( y ) → ( Large ( y ) ∨ Small ( y ) ∨ Medium ( y ) ) )\n\nTranslation:\nevery dodecahedron is large , small or medium");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item9 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ∃ x ( Prime ( x ) ∧ ¬ Even ( x ) )\n\nTranslation:\nfor all x , there is a prime x such that x is not even");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item10 = form.addPageBreakItem().setHelpText("Formula:\n( Larger ( c , e ) ∨ SameSize ( c , e ) ) ∧ ( Larger ( c , d ) ∨ SameSize ( c , d ) )\n\nTranslation:\nc is larger than e or of the same size as e and larger than d or of the same size as d");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item11 = form.addPageBreakItem().setHelpText("Formula:\n¬ ∃ x ∃ x Cube ( a )\n\nTranslation:\nit is not the case that there is an element x such that there is an element x such that a is a cube");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item12 = form.addPageBreakItem().setHelpText("Formula:\nSmall ( a ) → ¬ ( Adjoins ( a , a ) → Large ( b ) )\n\nTranslation:\nif a is small , then it is not the case that if a is adjacent to itself , then b is large");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item13 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ¬ Small ( x ) → ( ∃ y Smaller ( y , y ) → ( Person ( a ) ∧ Tet ( a ) ) )\n\nTranslation:\nif for all x , x is not small , then if there is an element y such that y is smaller than itself , then a is a person and a is a tetrahedron");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item14 = form.addPageBreakItem().setHelpText("Formula:\n( ∃ x Pet ( a ) ∧ Person ( a ) ) → ∀ x ( SameSize ( a , x ) → SameRow ( b , x ) )\n\nTranslation:\nif there is an element x such that a is a pet and a is a person , then for all x , if a is of the same size as x , then b is in the same row as x");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item15 = form.addPageBreakItem().setHelpText("Formula:\n∃ x ( ( Smaller ( a , x ) ∧ Even ( b ) ) ∧ ∀ x Medium ( a ) )\n\nTranslation:\nthere is an element x such that a is smaller than x , b is even and for all x , a is medium");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item16 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ∀ x Smaller ( a , a ) ∨ ( ∀ x Student ( x ) ∧ ( RightOf ( b , c ) ∧ Small ( a ) ) )\n\nTranslation:\nat least one of these holds : \n\t• for all x , for all x , a is smaller than itself \n\t• for all x , x is a student , b is to the right of c and a is small");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item17 = form.addPageBreakItem().setHelpText("Formula:\n¬ ( SameShape ( a , a ) ∧ Medium ( a ) ) ∧ ∃ x ( RightOf ( x , a ) → Pet ( b ) )\n\nTranslation:\nit is not the case that a is of the same shape as itself and a is medium and there is an element x such that if x is to the right of a , then b is a pet");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item18 = form.addPageBreakItem().setHelpText("Formula:\n∃ x ( ∃ x Cube ( a ) ∧ ¬ Medium ( a ) )\n\nTranslation:\nthere is an element x such that there is an element x such that a is a cube and a is not medium");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item19 = form.addPageBreakItem().setHelpText("Formula:\n( ( Small ( a ) ∧ Tet ( b ) ) ∧ ∀ x Small ( a ) ) → ( ( Small ( b ) ∧ Tet ( b ) ) ∨ Student ( b ) )\n\nTranslation:\nif a is small , b is a tetrahedron and for all x , a is small , then at least one of these holds : \n\t• b is small and b is a tetrahedron \n\t• b is a student");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item20 = form.addPageBreakItem().setHelpText("Formula:\nLarge ( a ) → ¬ ( Small ( a ) ∧ Person ( b ) )\n\nTranslation:\nif a is large , then it is not the case that a is small and b is a person");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item21 = form.addPageBreakItem().setHelpText("Formula:\n¬ ∃ x ( SameShape ( a , b ) → SameRow ( c , c ) )\n\nTranslation:\nit is not the case that there is an element x such that a is in the same shape as b and c is in the same row as itself");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item22 = form.addPageBreakItem().setHelpText("Formula:\n∀ x ( Tet ( x ) ∨ Prime ( a ) ) ∨ ∃ x ( Person ( x ) → Student ( a ) )\n\nTranslation:\nfor all x , x is a tetrahedron or a is a prime or there is an element x such that a is a student");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item23 = form.addPageBreakItem().setHelpText("Formula:\n∃ x ∀ y Larger ( x , a ) ∧ ∀ y ¬ Pet ( b )\n\nTranslation:\nthere is an element x such that for all y , x is larger than a and there is an element x such that for all y , b is not a pet");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item24 = form.addPageBreakItem().setHelpText("Formula:\n∃ x ( ( ( SameShape ( x , a ) ∧ Tet ( x ) ) → Adjoins ( x , a ) )\n\nTranslation:\nfor all x , if x is of the same shape as a, then x is adjacent to a");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");

var item25 = form.addPageBreakItem().setHelpText("Formula:\n∃ x Cube ( x ) ( Person ( a ) → Adjoins ( x , a ) )\n\nTranslation:\nthere is a cube such that a is a person or x is adjacent to a");
form.addMultipleChoiceItem().setTitle("Is the translation correct?").setHelpText("𝘾𝙤𝙧𝙧𝙚𝙘𝙩 means that the sentence conveys exactly the same information as the input logical formula.").setChoiceValues(["Yes", "No"]).setRequired(true);
form.addScaleItem().setTitle("Is the translation clear?").setHelpText("𝘾𝙡𝙚𝙖𝙧 means that the sentence is understandable and does not have multiple readings.").setBounds(1,5).setLabels("Very unclear", "Very clear").setRequired(true);
form.addScaleItem().setTitle("Is the translation fluent?").setHelpText("𝙁𝙡𝙪𝙚𝙣𝙩 means that the sentence sounds as a natural English sentence.").setBounds(1,5).setLabels("Not fluent", "Very fluent").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have a suggestion for a better translation? If so, then write it down here.");


final = form.addPageBreakItem().setTitle("Final questions");
form.addParagraphTextItem().setTitle("Give a general structured review of the strengths and weaknesses of the translation system. With which types of formulas does the system have difficulties? For which types of formulas do you believe the system performs sufficiently well?").setRequired(true);
form.addParagraphTextItem().setTitle("Do you have any final comments?");

item1.setGoToPage(item4)
item2.setGoToPage(item22)
item3.setGoToPage(item21)
item4.setGoToPage(item19)
item5.setGoToPage(item11)
item6.setGoToPage(item15)
item7.setGoToPage(item23)
item8.setGoToPage(item16)
item9.setGoToPage(item6)
item10.setGoToPage(item3)
item11.setGoToPage(item25)
item12.setGoToPage(item5)
item13.setGoToPage(item18)
item14.setGoToPage(item12)
item15.setGoToPage(item2)
item16.setGoToPage(item20)
item17.setGoToPage(item10)
item18.setGoToPage(final)
item19.setGoToPage(item14)
item20.setGoToPage(item8)
item21.setGoToPage(item13)
item22.setGoToPage(item24)
item23.setGoToPage(item17)
item24.setGoToPage(item7)
item25.setGoToPage(item9)
final.setGoToPage(item1)

var ss = SpreadsheetApp.create("1.8 results");
form.setConfirmationMessage("Thank you very much! Your response has been recorded.").setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId()).setShowLinkToRespondAgain(false);
}
