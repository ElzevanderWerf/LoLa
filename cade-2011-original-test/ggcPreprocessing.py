"""Python script to extract all correct formulas from the Grade Grinder
Corpus, with several preprocessing steps."""

import pandas as pd
import re

# Open GGC as DataFrame
ggc_df = pd.read_csv("translationcorpus-1.0.1.csv", 
                     header=0, 
                     error_bad_lines=False)
#print("original number of translations",len(ggc_df) )

# Take the canonical form of the formulas that were correct, 
# and remove duplicates (dict.fromkeys() is used for keeping the original order):
formulas = list(dict.fromkeys(ggc_df[(ggc_df["status"] == "correct")]["canonical"]))
#print("initial amount of correct formulas:", len(formulas)) --> 26089

# Remove NaNs
formulas = [f for f in formulas if not(pd.isnull(f))] 
# print("after removing nans:", len(formulas)) --> 26088

# Remove formulas with these specific characters or strings
ignore = ["=", "<", ">", "^", "+", "*", "%", "is", "not", "equivalent", 
          ".", "\"", "\\", "0", "1", "2", "3", "4", "5", ":"]
formulas = [f for f in formulas if not any(s in f for s in ignore)]

# Remove formulas with 3-place predicates, e.g. Between(a,b,c)
formulas = [f for f in formulas if re.search(r'\([a-z]+,[a-z]+,[a-z]+\)', f) == None]

# Remove formulas with 4-place predicates, e.g. Gave(a,b,c,d)
formulas = [f for f in formulas if re.search(r'\([a-z]+,[a-z]+,[a-z]+,[a-z]+\)', f) == None]
#print("after removing formulas not parsable by Ranta's system:", len(formulas)) --> 7000

# Change to correct spacing:
# - Put spaces before and after the given characters: ,|&$()@/~
formulas = [re.sub(re.compile(r'([,|&$()@/~])'), " \\1 ", f) for f in formulas]
# - Remove double spaces
formulas = [re.sub(' +', ' ', f) for f in formulas]
# - Remove beginning and end spaces
formulas = [f[1:] if f[0]==' ' else f for f in formulas]
formulas = [f[:-1] if f[-1]==' ' else f for f in formulas]

# Remove formulas longer than a 100 characters (cannot be parsed by GF)
formulas = [f for f in formulas if len(f)<100]
#print("after removing formulas longer than 100 characters:", len(formulas)) --> 5463

#Write formulas to file with newlines
with(open(r'out/ggc-formulas.tmp', 'w')) as f:
    f.write('\n'.join(formulas))
f.close()


