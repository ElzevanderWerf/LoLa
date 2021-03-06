# EXPERIMENT 2 REPORT

This report lists the steps taken to prepare the experiment of my second study. See section 6 of my thesis for an extensive explanation of the method.

## Experimental items
**See materials folder**
This section explains how the following list of experimental items is created:
- In `nli-items.csv`: For the Natural Language Inference task, 10 GGC formulas + 10 RG formulas with for each of them the three system translations, with my own hypotheses designed for them.
- In `fr-items.csv`: For the Fluency Ranking task, 10 GGC formulas + 10 RG formulas  with for each of them the three system translations.

In `Trans.hs`, I have added the option to translate all sentences from an input file in a source language to a target language, writing them to an output file. To use this option, do:

    stack run trans <mode> <source-language> <input-file> <target-language> <output-file>

The translations are printed in the following format: `WB/NWB, Output AST, Translation`, where `WB` stands for *well-behaved* and `NWB` for *ill-behaved*.

### (GGC) Grade Grinder Corpus translations
From the Grade Grinder Corpus (in the ignored file `translationcorpus-1.0.1.csv`), a set of useful formulas was extracted as follows:

1. The Python script in `ggcPreprocessing.py` writes all suitable GGC formulas to the file `ggc-formulas.tmp`, with the following preprocessing to ignore weird formulas and include spacing:
	- Take only the canonical form of the formulas (student answers) that were marked correct.
	- Remove all formulas with NaN.
	- Remove formulas with these specific characters or strings: "=", "<", ">", "^", "+", "*", "%", "is", "not", "equivalent", ".", "\"", "\\", "0", "1", "2", "3", "4", "5", ":" (these are part of structures that are not parsable by Ranta’s system).
	- Remove formulas with 3- and 4-place predicates (not parsable by Ranta's system either).
	- Add spaces to the formulas, so that they are parsable by the GF shell (see also next step for why I did this).
	- Remove formulas with more than 100 characters (because the GF shell gets stuck at the formulas that are too long)

2. I made a GF grammar for the GGC notation, called `PropGGC` in `PropGGC.gf` (in this way, I could do the translations from GGC to Latex notation very easily; this is its only use, so it is not extended in any other way). I added this grammar to `Makefile`.
3. The Python script in `ggcExtractPredicates.py` extracts the list of 1- and 2-place predicates used in the corpus. I added these predicates to the abstract grammar Prop and the concrete grammars PropEng, PropLatex and PropGGC.
4. For compiling the grammar and building the executable:

        >make pgf
		>stack build
5. I obtained the translations of 3 different systems for each of the formulas in `ggc-formulas`:
    1. BASELINE: `ggc-baseline.tmp`, produced by
    
         >stack run trans MNone PropGGC data/ggc-formulas.tmp PropEng data/ggc-baseline.tmp
    
    (this took around 15 minutes)
    2. RANTA: `ggc-ranta.tmp`, copied from [cade-2011-study-1](https://github.com/ElzevanderWerf/cade-2011-study-1/blob/master/out/ggc-eng.tmp).
    3. LoLa:`ggc-lola.tmp`, produced by
            
        >stack run trans MSimplify PropGGC data/ggc-formulas.tmp PropEng data/ggc-lola.tmp
	
	(this took around 2.5 hours)


### (RG) Own random generation function
I designed a random generation function, which generates formulas from the entire space of first-order logic formulas.

1. In `RandomGenerationGGC.py`, I wrote a Python script to randomly generate formulas in GGC notation, with a lexicon similar as the one in GGC. 99 generated formulas are in `rg-formulas.tmp`.

5. I obtained the translations of 3 different systems for each of the formulas in `rg-formulas.tmp`:
    1. BASELINE: `rg-baseline.tmp`, produced by
    
         >stack run trans MNone PropGGC data/rg-formulas.tmp PropEng data/rg-baseline.tmp
    
    (this took around 1 minute)
    2. RANTA: `rg-ranta.tmp`, translated with Trans in repo [cade-2011-study-1](https://github.com/ElzevanderWerf/cade-2011-study-1/blob/master/out/test3Eng.tmp).
    3. LoLa:`rg-lola.tmp`, produced by
            
        >stack run trans MSimplify PropGGC data/rg-formulas.tmp PropEng data/rg-lola.tmp
	
	(this took around 3 minutes)

		
### Preparing experiment 1
**See materials folder**
1. For readability, I wrote `makeCSV.py` to combine the above mentioned `tmp` files into CSVs for each task (`nli-items1.csv`, `nli-items2.csv`, `nli-items3.csv`, and `fr-items123.csv`), found in the folder `experimental_items`:

		>python makecsv.py   
2. For the NLI questions, I created one hypothesis per formula, and added whether the correct answer should be *Yes* or *No*. See the file `nli-hypotheses 123.csv` in the folder `experimental_items`.
3. The Python script in `createForms.py` writes 3 different Google Apps Script files to the folder `formScripts`, thereby creating 3 different surveys in Google Forms, each with a different set of experimental items, according to a Latin Square Design.

## Results analysis
**See results and analysis folders**
1. The results per survey were downloaded from Google Forms as TSV files in `results/TSVs`. Note that there were 6 different surveys, because each of the 3 surveys had 2 versions (one for the Barcelona researchers and one for the newly recruited students, because the student version included two extra questionts: (1) about participation in the experiment of Study 1, and (2) asked for their payment info). The script in `analysis/preprocessing.py` performs some preprocessing to make them more readible and transform them into CSVs, written to the folder `results/CSVs`.
2. The python scripts `personalQs.py` and `nli.py` perform several analyses on the results, writing the results to the command line. For Fluency Ranking, the *TrueSkill* adaptation of Sakaguchi et al. (2014) is used, extracted from [WMT-TrueSkill](www.github.com/keisks/wmt-trueskill). The script in `fr.py` processes the rankings into a CSV readible by *TrueSkill*.
3. The folder `out` contains output texts from the analyses. The results are reported and discussed in my thesis.