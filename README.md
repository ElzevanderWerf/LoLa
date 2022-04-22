13-06-2022

## Grammatical Framework application grammar for translating between language and predicate logic

This system is based on the study of Ranta (2011):
_Translating between language and logic: what is easy and what is difficult._
A Ranta - International Conference on Automated Deduction, 2011, LNCS/LNAI. See http://www.cse.chalmers.se/~aarne/articles/cade2011.pdf.

The original version of Ranta's code is taken from [cade-2011](https://github.com/GrammaticalFramework/gf-contrib/tree/master/cade-2011). The file `Changes.md` lists all bug fixes and changes to the original code. The file `Experiment2.md` reports the steps taken for setting up experiment 2 and analyzing the results.

### Compile with stack

To build

    make pgf
    stack build

To test

    stack run trans "for all numbers x , x is even or x is odd"

For translating all sentences in a source language from an input text file to a target language with AST simplification, writing them to an output text file:

    stack run trans <source-language> <input-file> <target-language> <output-file>
    

### Source files

```
  -- reports
  Changes.md                -- report of bug fixes and changes in code
  Experiment2.md            -- report of all steps taken in experiment 2, see also the folder `exp2'
  
  -- language-neutral
  Prop.gf                   -- abstract syntax
  Trans.hs                  -- top loop
  TransProp.hs              -- conversions
  TransPropFunctions.hs     -- additional functions used in TransProp
  TransLogicLaws.hs         -- AST functions based on logical equivalence laws of Partee et al. (1990) Mathematical Methods in Linguistics
  Makefile

  -- concrete syntax
  PropI.gf                  -- concrete syntax, functor with RGL
  PropDut.gf	            -- concrete syntax, Dutch with RGL functor
  PropEng.gf                -- concrete syntax, English with RGL functor
  PropFin.gf                -- concrete syntax, Finnish with RGL functor
  PropFre.gf                -- concrete syntax, French  with RGL functor
  PropGer.gf                -- concrete syntax, German  with RGL functor
  PropPor.gf                -- concrete syntax, Portuguese with RGL functor
  PropSwe.gf                -- concrete syntax, Swedish with RGL functor
  PropLatex.gf              -- concrete syntax, symbolic logic in LaTeX

  -- not in use
  PropENF.gf                -- concrete syntax, English with RGL ordinary module
  PropStr.gf                -- concrete syntax, pidgin English
```

### Generated files

```
  Prop.hs        -- abstract syntax in Haskell
  Prop.pgf       -- abstract syntax in Portable Grammar Format (PGF)

```
