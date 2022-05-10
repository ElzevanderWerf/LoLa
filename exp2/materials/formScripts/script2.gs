function main0() {
var file = DriveApp.getFileById("1LYuXRnB1Q4enFnlhA-wvr90vFIJjG8YB0EdBs4RZSTs").makeCopy("Form 2.0");
var form = FormApp.openById(file.getId());
form.setTitle("Natural Language Inference & Fluency Ranking");

var nli1 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nE is a cube, a is a cube or c is a cube.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli2 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all v, for all w, if v is a tetrahedron and w is a dodecahedron, then v is in front of w.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli3 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf c is medium, then it is not the case that d is a cube or e is a cube and f is not a cube.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli4 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIt is not the case that there is an element x such that there is an element y such that x is a cube, y is a dodecahedron and x is larger than y.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli5 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all u, if u is a cube and there is an element y such that y is in back of u, then u is small.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli6 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all w, if w is to the left of a, then it is not the case that for all z, if z is to the left of b, then w is larger than z.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli7 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all y, there is an element z such that if y is a dodecahedron, then z is a cube and y is of the same size as z.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli8 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, if x is to the left of b, then x is to the left of a and for all x, if x is to the left of a, then x is to the left of b.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli9 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIt is not the case that everything is a dodecahedron and e is to the left of everything.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli10 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, a is not adjacent to c, a is not adjacent to b, a is not adjacent to x and a is not adjacent to itself.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli11 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nEvery cube is to the left of every tetrahedron.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli12 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nEvery cube is to the left of every tetrahedron.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli13 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nB is not a tetrahedron or c is a tetrahedron.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli14 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all dodecahedrons x, for all cubes y, x is larger than y or y is of the same size as x.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli15 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf d is to the right of a or d is to the left of a, then a is a cube.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli16 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nF is to the right of a and f is to the left of b.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli17 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, for all z, for all y, if z is a cube and y is a cube and x is in back of y and x is in front of z, then it is not the case that x is large.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli18 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, for all y, if x is in back of y, then y is smaller than x.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli19 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf it is not the case that b is a tetrahedron, then it is not the case that a is a tetrahedron.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli20 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nThere is an element x such that x is large and x is a cube and there is an element y such that y is small and y is a cube and y is in back of x.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli21 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIt is not the case that there is an element x such that there is an element z such that x is a cube and x is to the right of z.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli22 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, a is large or x is a tetrahedron and for all x, if b is in front of x, then x is a student.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli23 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf it is not the case that a is small or b is a tetrahedron, then for all x, x is a cube.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli24 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nThere is an element x such that at least one of these holds : \n\t• x is larger than a and b is a cube \n\t• c is to the left of itself.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli25 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, if there is an element x such that a is even, then for all y, x is in back of itself.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli26 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nThere is an element x such that if a is not to the right of x, then b is a prime and x is a pet.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli27 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nA is not adjacent to b, a is not small and there is an element x such that for all y, y is medium.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli28 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nAt least one of these holds : \n\t• for all x, a is medium and a is not a tetrahedron \n\t• if there is an element x such that x is a student, then there is an element y such that b is a dodecahedron.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli29 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf a is in back of b or everything is larger than b, then something is in front of itself or something is a student.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli30 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf if a is large, then a is in the same column as itself, then a is large.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli31 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nB is a student, a is not a student or a is small.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli32 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nSomething is to the left of a.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli33 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nThere is a student x such that all these hold : \n\t• a is a person or x is a prime \n\t• x is in the same row as b.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli34 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nNothing is in back of itself and a is a dodecahedron.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli35 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nB is not of the same size as a or a is not medium.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli36 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, x is large and a is in front of b and it is not the case that x is large.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli37 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nThere is an element x such that it is not the case that a is a prime or a is a cube.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli38 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf a is a student, then if b is small, then a is a tetrahedron and for all x, x is a person.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli39 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nFor all x, for all x, if x is of the same size as x, then a is large.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli40 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIf a is a cube and a is in back of a and b is even, then there is an element x such that for all y, a is smaller than a.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli41 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIt is not the case that if it is not the case that a is a cube, then a is medium or a is small.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);
var nli42 = form.addMultipleChoiceItem().setTitle("Does the hypothesis automatically follow from the premise?\n\nPremise:\nIt is not the case that for all x, a is a dodecahedron and it is not the case that b is small and b is in the same row as c or a is of the same shape as a.\n\nHypothesis:\nH").setChoiceValues(["Yes", "No"]).showOtherOption(true).setRequired(true);

form.addPageBreakItem().setTitle("Fluency Ranking").setHelpText("The purpose of this task is to evaluate the fluency of English translations from first-order logic formulas. We will present to you, one by one, 20 formulas with 3 candidate translations, like in the example below:\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\nFormula:\t\t\t¬ ∃ x ( Cube ( x ) ∧ LeftOf ( b , x ) )\n\nTranslation 1:\t\tIt is not the case that b is to the left of some cube.\nTranslation 2:\t\tIt is not the case that there exists an element x such that x is a cube and b is to the left of x.\nTranslation 3:\t\tFor all x, b is not to the left of x or x is not even.\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nPlease rank the translations by the criterion of 𝗳𝗹𝘂𝗲𝗻𝗰𝘆, where rank 1 stands for the most fluent, and 3 for the least fluent translation. By a fluent translation, we mean a translation that sounds as a natural English sentence. In ranking, ties are allowed. So, for example, if you think Translation 1 is best and Translation 2 and 3 are equally bad, give Translation 1 the highest rank (1), and Translation 2 and 3 the next highest rank (2), assigning nothing to the third rank.\n\nIn ranking the translations, please note that it is very important that you evaluate the fluency of the translations based only on the form of the translations (not on their adequacy given the formula). It can happen that two candidate translations are exactly the same. Please assign them the same rank always.\n\nFor your information, these are the interpretations of the predicates used in the formulas:\nDodec ( x )\t\t\tx is a dodecahedron\nSmall ( x )\t\t\tx is small\nStudent ( x )\t\t\tx is a student\nMedium ( x )\t\tx is medium\nCube ( x )\t\t\tx is a cube\nPrime ( x )\t\t\tx is a prime\nPerson ( x )\t\t\tx is a person\nTet ( x )\t\t\t\tx is a tetrahedron\nPet ( x )\t\t\t\tx is a pet\nLarge ( x )\t\t\tx is large\nEven ( x )\t\t\tx is even\nAdjoins ( x , y )\t\tx is adjacent to y\nSameCol ( x , y )\t\tx is in the same column as y\nLeftOf ( x , y )\t\tx is to the left of y\nRightOf ( x , y )\t\tx is to the right of y\nSmaller ( x , y )\t\tx is smaller than y\nFrontOf ( x , y )\t\tx is in front of y\nLarger ( x , y )\t\tx is larger than y\nSameRow ( x , y )\tx is in the same row as y\nSameShape ( x , y )\tx is the same shape as y\nSameSize ( x , y )\tx is the same size as y\nBackOf ( x , y )\t\tx is in back of y");
var fr1 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∃ v ( Dodec ( v ) ∧ ¬ Large ( v ) )\n\n\nTranslation 1:\nIt is not the case that every dodecahedron is large.\n\nTranslation 2:\nThere is an element v such that v is a dodecahedron and it is not the case that v is large.\n\nTranslation 3:\nThere is a dodecahedron v such that v is not large.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr2 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∃ u ( ¬ ( Large ( u ) ∨ Small ( u ) ) ∧ Dodec ( u ) )\n\n\nTranslation 1:\nThere is an element u such that it is not the case that u is large or u is small and u is a dodecahedron.\n\nTranslation 2:\nIt is not the case that every dodecahedron is small or large.\n\nTranslation 3:\nThere is an element u such that it is not the case that u is large or small and u is a dodecahedron.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr3 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ y ( ¬ ∃ x FrontOf ( x , y ) → Large ( y ) )\n\n\nTranslation 1:\nFor all y, if it is not the case that there is an element x such that x is in front of y, then y is large.\n\nTranslation 2:\nFor all y, y is large or something is in front of y.\n\nTranslation 3:\nFor all y, if it is not the case that there is an element x such that x is in front of y, then y is large.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr4 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ x ( Dodec ( x ) → RightOf ( x , a ) )\n\n\nTranslation 1:\nEvery dodecahedron is to the right of a.\n\nTranslation 2:\nFor all x, if x is a dodecahedron, then x is to the right of a.\n\nTranslation 3:\nEvery dodecahedron is to the right of a.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr5 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ x ∃ y ( ¬ ∃ z ( Dodec ( x ) → RightOf ( z , x ) ) → LeftOf ( y , x ) )\n\n\nTranslation 1:\nFor all x, there is an element y such that if it is not the case that there is an element z such that if x is a dodecahedron, then z is to the right of x, then y is to the left of x.\n\nTranslation 2:\nFor all x, there is an element y such that if it is not the case that there is an element z such that if x is a dodecahedron, then z is to the right of x, then y is to the left of x.\n\nTranslation 3:\nFor all x, x is not a dodecahedron, something is to the right of x or something is to the left of x.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr6 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ x ( Cube ( x ) → ∀ y ¬ RightOf ( x , y ) )\n\n\nTranslation 1:\nFor all cubes x, for all y, x is not to the right of y.\n\nTranslation 2:\nEvery cube is to the right of nothing.\n\nTranslation 3:\nFor all x, if x is a cube, then for all y, it is not the case that x is to the right of y.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr7 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n¬ ∃ x ∀ y ( ¬ FrontOf ( y , x ) ∧ ¬ Tet ( x ) )\n\n\nTranslation 1:\nFor all x, there is an element y such that y is in front of x or x is a tetrahedron.\n\nTranslation 2:\nIt is not the case that there is an element x such that for all y, y is not in front of x and x is not a tetrahedron.\n\nTranslation 3:\nIt is not the case that there is an element x such that for all y, it is not the case that y is in front of x and it is not the case that x is a tetrahedron.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr8 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\nLeftOf ( f , b ) ∧ LeftOf ( a , f )\n\n\nTranslation 1:\nF is to the left of b and a is to the left of f.\n\nTranslation 2:\nF is to the left of b and a is to the left of f.\n\nTranslation 3:\nF is to the left of b and a is to the left of f.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr9 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∃ x ∃ y ∃ z ( Tet ( x ) ∧ Tet ( y ) ∧ Tet ( z ) ∧ ¬ ( SameCol ( x , y ) ∧ SameCol ( y , z ) ) )\n\n\nTranslation 1:\nThere is an element x such that there is an element y such that there is an element z such that x is a tetrahedron and y is a tetrahedron and z is a tetrahedron and it is not the case that x is in the same column as y and y is in the same column as z.\n\nTranslation 2:\nThere is an element x such that there is an element y such that there is a tetrahedron z such that it is not the case that x is in the same column as y and y is in the same column as z, x is a tetrahedron and y is a tetrahedron.\n\nTranslation 3:\nThere is an element x such that there is an element y such that there is an element z such that x is a tetrahedron, y is a tetrahedron, z is a tetrahedron and it is not the case that x is in the same column as y and y is in the same column as z.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr10 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ x ( SameCol ( x , a ) ∨ SameCol ( b , x ) ∨ SameCol ( x , c ) )\n\n\nTranslation 1:\nFor all x, x is in the same column as a, b is in the same column as x or x is in the same column as c.\n\nTranslation 2:\nFor all x, x is in the same column as a, b is in the same column as x or x is in the same column as c.\n\nTranslation 3:\nFor all x, x is in the same column as a or b is in the same column as x or x is in the same column as c.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr11 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ x ( Student ( x ) ∨ Dodec ( a ) ) ∨ ∀ y ( Even ( a ) ∨ BackOf ( y , b ) )\n\n\nTranslation 1:\nFor all x, x is a student or a is a dodecahedron or for all y, a is even or y is in back of b.\n\nTranslation 2:\nFor all x, x is a student or a is a dodecahedron or for all y, a is even or y is in back of b.\n\nTranslation 3:\nFor all x, x is a student or a is a dodecahedron or for all y, a is even or y is in back of b.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr12 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ x ( ∃ x RightOf ( x , a ) → ( Smaller ( b , x ) → Large ( a ) ) )\n\n\nTranslation 1:\nFor all x, if there is an element x such that x is to the right of a, then if b is smaller than x, then a is large.\n\nTranslation 2:\nFor all x, if there is an element x such that x is to the right of a, then if b is smaller than x, then a is large.\n\nTranslation 3:\nB is smaller than nothing, a is large or nothing is to the right of a.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr13 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∃ x ¬ SameShape ( x , a )\n\n\nTranslation 1:\nThere is an element x such that it is not the case that x is of the same shape as a.\n\nTranslation 2:\nThere is an element x such that x is not of the same shape as a.\n\nTranslation 3:\nIt is not the case that everything is of the same shape as a.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr14 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∃ x ( ∃ y Tet ( y ) ∨ Even ( a ) )\n\n\nTranslation 1:\nThere is an element x such that there is an element y such that y is a tetrahedron or a is even.\n\nTranslation 2:\nSomething is a tetrahedron or a is even.\n\nTranslation 3:\nThere is an element x such that there is an element y such that y is a tetrahedron or a is even.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr15 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\nSameRow ( a , a ) ∧ ( ∃ x Cube ( b ) ∨ ( Larger ( a , c ) ∨ Person ( c ) ) )\n\n\nTranslation 1:\nAll these hold : \n\t• a is in the same row as itself \n\t• there is an element x such that b is a cube, a is larger than c or c is a person.\n\nTranslation 2:\nAll these hold : \n\t• a is in the same row as itself \n\t• b is a cube, a is larger than c or c is a person.\n\nTranslation 3:\nA is in the same row as a and there is an element x such that b is a cube or a is larger than c or c is a person.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr16 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n¬ ( ¬ SameRow ( a , b ) ∧ ∀ x Larger ( a , c ) )\n\n\nTranslation 1:\nIt is not the case that it is not the case that a is in the same row as b and for all x, a is larger than c.\n\nTranslation 2:\nIt is not the case that a is not in the same row as b and for all x, a is larger than c.\n\nTranslation 3:\nA is in the same row as b or a is not larger than c.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr17 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n¬ ( ( Smaller ( a , a ) ∨ LeftOf ( b , b ) ) ∧ ∀ x Cube ( a ) )\n\n\nTranslation 1:\nIf a is smaller than itself or b is to the left of itself, then a is not a cube.\n\nTranslation 2:\nIt is not the case that all these hold : \n\t• a is smaller than itself or b is to the left of itself \n\t• for all x, a is a cube.\n\nTranslation 3:\nIt is not the case that a is smaller than a or b is to the left of b and for all x, a is a cube.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr18 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∃ x ( Medium ( a ) ∨ Prime ( a ) ) → ∀ y ¬ Tet ( y )\n\n\nTranslation 1:\nIf there is an element x such that a is medium or a is a prime, then for all y, it is not the case that y is a tetrahedron.\n\nTranslation 2:\nIf there is an element x such that a is medium or a is a prime, then for all y, y is not a tetrahedron.\n\nTranslation 3:\nIf a is a prime or a is medium, then nothing is a tetrahedron.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr19 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∀ x ∃ y Medium ( a ) ∨ ∃ x ∀ z Tet ( b )\n\n\nTranslation 1:\nB is a tetrahedron or a is medium.\n\nTranslation 2:\nFor all x, there is an element y such that a is medium or there is an element x such that for all z, b is a tetrahedron.\n\nTranslation 3:\nFor all x, there is an element y such that a is medium or there is an element x such that for all z, b is a tetrahedron.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);
var fr20 = form.addGridItem().setTitle("Given the following formula and candidate translations, rank the translations from most fluent (1) to least fluent (3).\n\n\nFormula:\n∃ x Prime ( x ) ∧ ∃ x ( Prime ( a ) ∨ Cube ( a ) )\n\n\nTranslation 1:\nThere is an element x such that x is a prime and there is an element x such that a is a prime or a is a cube.\n\nTranslation 2:\nThere is an element x such that x is a prime and there is an element x such that a is a prime or a is a cube.\n\nTranslation 3:\nAll these hold : \n\t• something is a prime \n\t• a is a prime or a is a cube.").setHelpText("Ties are allowed.").setRows(["Translation 1", "Translation 2", "Translation 3"]).setColumns(["(Most fluent) 1", "2", "3 (Least fluent)"]).setRequired(true);

final = form.addPageBreakItem().setTitle("Final question");
form.addParagraphTextItem().setTitle("Do you have any final comments on the survey?");

var ss = SpreadsheetApp.create("2.0. results");
form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
}
