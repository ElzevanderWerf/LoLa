## Testing the logic-to-language translation system of Ranta (2011)

This is the original version of Ranta's code, taken from [cade-2011](https://github.com/GrammaticalFramework/gf-contrib/tree/master/cade-2011), with 3 small bug fixes:
1. 	`PropLatex.gf`) Comment of Ranta `fix negation of in` at `lin AKind`: *1 \in N* is parsed and linearized as both *1 is a number* and *1 is not a number*. New code:
        
        AKind k x = table {True => top x ++ "\\in" ++ k ; False => top (prefix 3 "\\sim" (constant (top x ++ "\\in" ++ k)))} ;
	Now it only returns *1 is a number*.
2. 	`PropLatex.gf`) The linearization functions of `ModKind` and `PartPred` were wrong and commented out. New code:

			ModKind k m = (m ! True) ++ k ;
			PartPred f y = \\b => (f ! b)  ++ "to" ++ (top y) ;
3.	`PropLatex.gf`) *\even { 2 }* translates to *2 is even* (`PAtom (APred1  Even (IInt 2)`) AND *2 is not even* (`PNegAtom (APred1 Even (IInt 2))`). This happened because of wrong code in the `slash` operation (3rd case of the overload). New code: 

			slash : Str -> Bool => Str = \f -> table {True => "\\" + f ; False => top (prefix 3 "\\sim" (constant ("\\" + f)))} ;

I have done the following three tests to create a set of logical formulas and their English translations, for study 1 (post-editing). The generated files are in folder `out`.
									 
#### TEST 1: GF random generation
**(Filenames start with test1)**
0. In `Prop.gf` and `PropLatex.gf`, I removed (commented out) the geometry lexicon (the functions `Vertical`, `Horizontal`, `Parallel`, `Line`, `Point`, `Centre`, and `Intersection`), so that I would only generate formulas with arithmetic predicates and functions.
   
1. Random generation. I opened the GF shell and imported the Latex grammar as follows:

	    >gf cade-2011-original-test/PropLatex.gf
   In the GF shell, I generated 1000 trees with:
   
		>gr -number=1000 | wf -file=out/test1.tmp
   Note that the default generation depth is 4 (so the maximum depth of the generated abstract syntax trees is 4).
		
2. I read through these trees and generated the latex linearizations of these trees:

		>rf -file=out/test1.tmp -lines -tree | l -lang=Latex | wf -file=out/test1Latex.tmp
		
   Result: a file of 1000 Latex formulas, called `test1Latex.tmp`.
   
3. To translate these formulas into English with Ranta's optmiziation, I wrote a Haskell script in `TransTest.hs`. In `cade.cabal` (for running it from the command line), I changed the line 

		main-is: Trans.hs 
	to
	
		main-is: TransTest.hs
		
    `TransTest.hs` includes code to read sentences or formulas from an input-file and parse and linearize them into a source language, with optimization. These translations are written to another output-file. There might be more than one parse of a latex formula, so there might be more than one target language translation for each input sentence. That is why the output file is longer than the input file, but for readability there is an extra space between the translations of one source language sentence and the next one.
4. Running `TransTest.hs`:
    I build the executable `trans.exe`:

		>stack build
		
    To run `TransTest.hs`, do

		>>stack run trans <source-language> <input-file> <target-language> <output-file>
		
	So in our case, translating a file of Latex formulas into English:
	
		>stack run trans PropLatex out/test1Latex.tmp PropEng out/test1Eng.tmp
		
6. For combining the two files (`test1Latex.tmp` and `test1Eng.tmp`) into one, for readability, I wrote a Python script in `makecsv.py` that writes the formulas with translations to a csv file. To run the script, do:

		>python makecsv.py <source-lang-file> <target-lang-file> <output-csv>
    In this case:
    
		>python makecsv.py out/test1Latex.tmp out/test1Eng.tmp out/test1.csv


#### TEST 2: Grade Grinder Corpus translations
**(Filenames start with ggc)**
The usefulness of the translations of is very low, because of the way the random generation function is built. Therefore, I have decided to use the Grade Grinder Corpus (in `translationcorpus-1.0.1.csv`) for generating more useful Latex formulas. This means that we skip the generation steps (1-2) from TEST 1, and instead do the following:

1. The Python script in `ggcPreprocessing.py` writes a list of useful formulas to the file `ggc-formulas.tmp`, with the following preprocessing to ignore weird formulas and include spacing:
	- Take only the canonical form of the formulas (student answers) that were marked correct.
	- Remove all formulas with NaN.
	- Remove formulas with these specific characters or strings: "=", "<", ">", "^", "+", "*", "%", "is", "not", "equivalent", ".", "\"", "\\", "0", "1", "2", "3", "4", "5", ":" (these are part of structures that are not parsable by Ranta’s system).
	- Remove formulas with 3- and 4-place predicates (not parsable by Ranta's system either).
	- Add spaces to the formulas, so that they are parsable by the GF shell (see also next step for why I did this).
	- Remove formulas with more than 100 characters (because the GF shell gets stuck at the formulas that are too long)

	Running took about 8 minutes.
2. I made a GF grammar for the GGC notation, called `PropGGC` in `PropGGC.gf` (in this way, I could do the translations from GGC to Latex notation very easily).
3. The Python script in `ggcExtractPredicates.py` extracts the list of 1- and 2-place predicates used in the corpus. I added these predicates to the grammars of English, Latex and GGC, and commented out the other two test lexicons.
4. I ran TransTest.hs with arguments `ggc-formulas.tmp` and `ggc-eng.tmp` (this took about 15 minutes):

		>make pgf
		>stack build
		>stack run trans PropGGC out/ggc-formulas.tmp PropEng out/ggc-eng.tmp
		
5. I used `makecsv.py` to combine them again into a csv for readability:

		>python makecsv.py out/ggc-formulas.tmp out/ggc-eng.tmp out/ggc-formulas-to-eng.csv

#### TEST 3 Own random generation function
**(Filenames start with test3)**
I designed a random generation function myself, which generates formulas that are a little more varied than the ones generated by the GF shell.

1. In `test3RandomGenerationLatex.py`, I wrote a Python script to randomly generate formulas in Latex notation, with an arithmetic lexicon. 50 generated formulas are in `test3Latex.tmp`.
2. In `test3RandomGenerationGGC.py`, I wrote a Python script to randomly generate formulas in GGC notation, with a lexicon similar as the one in GGC. 1000 generated formulas are in `test3GGC.tmp`.
3. I ran TransTest.hs with arguments `test3GGC.tmp` and `test3Eng.tmp` (this took about 2 minutes):

		>stack run trans PropGGC out/test3GGC.tmp PropEng out/test3Eng.tmp

		
#### PREPARING EXPERIMENT 1
**(Filenames start with exp1)**
1. I used `makecsv.py` to combine the files `test3GGC.tmp` and `test3Eng.tmp` into a csv (`exp1-rg-to-eng.csv`) for readability:

		>python makecsv.py out/test3GGC.tmp out/test3Eng.tmp exp1/exp1-rg-to-eng.csv		
2. The Python script in `ggcSubsetFormulasToEng.py` writes a random sample of 1000 formulas and translations from `ggc-formulas-to-eng.csv` to the file `exp1-ggc-to-eng.csv`.
3. In the Python script `replaceSymbols.py`, the GGC symbols in `exp1-rg-to-eng.csv` and `exp1-ggc-to-eng.csv` are replaced by the common FOL symbols:
        
        >python replaceSymbols.py exp1/exp1-rg-to-eng.csv
        >python replaceSymbols.py exp1/exp1-ggc-to-eng.csv
        
4. The Python script in `createForms.py` writes 20 different Google Apps Script files to the folder `scripts`, thereby creating 20 different surveys in Google Forms, each with a different set of experimental items from `exp1-ggc-to-eng.csv` and `exp1-rg-to-eng.csv`, and the same set of fillers from `fillers.csv`.

#### EXPERIMENT 1 ANALYSIS
**(Files in folder exp1)**
1. For each response, I exported TSV files from the Google Forms (in `results/TSVs`), which contain the results of the experiment.
There are x? responses to the following set of questions:
    - "What is your gender?" (multiple-choice between "Male", "Female", and "Prefer not to say")
    - "How old are you?" (multiple-choice)
    - "How would you rate your knowledge of and familiarity with first-order logic?" (5-point Likert scale)
    - For each of the test items in each batch in the folder `batches`, the following questions:
        1. "Is the translation correct?" (multiple-choice between "Yes" and "No")
        2. "Is the translation clear?" (5-point Likert scale)
        3. "Is the translation fluent?" (5-point Likert scale)
        4. "Do you have a suggestion for a better translation? If so, then write it down here." (open question)
    - "Give a general structured review of the strengths and weaknesses of the translation system. With which types of formulas does the system have difficulties? For which types of formulas do you believe the system performs sufficiently well?" (open question)
    - "Do you have any final comments?" (open question)
2. The Python script in `analysis.py` does some preprocessing steps on the TSVs, and performs some small analyses:
    - Gender percentages
    - Age average and standard deviations
    - Experience average and standard deviations
    - Correctness of the fillers
    For all non-filler items:
    - Correctness percentages
    - Clarity average and standard deviations
    - Fluency average and standard deviations
    - Post-edit percentages
    The results on the experimental items are written to CSV files in `results/CSVs` in a more readable format.