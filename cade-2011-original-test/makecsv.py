"""Python script to combine generated source language (arg0) and 
target language (arg1) files into a csv file (arg2).

To run the script, do:
    >python makecsv.py <source-lang-file> <target-lang-file> <output-csv>"""

import sys
import pandas as pd
from itertools import groupby

(f_source, f_target, f_test) = sys.argv[1:]

# IMPORT FILE CONTENTS
with open(f_source) as f:
    source = f.read().splitlines() # list of strings
f.close()

with open(f_target) as f:
    target = f.read().splitlines() # list of strings
f.close()

target = [list(g) for k,g in groupby(target, key=lambda x: x != "") if k] #list of lists of strings
target = [list(set(l)) for l in target] # remove duplicate translations   

#set all lists of translation to length 10 (I don't expect more than 10 different tranlations)
def extend_n(l, n):
    l.extend([0] * n)
    return l[:n]
target = [extend_n(l, 10) for l in target] 

target_1 = [l[0] for l in target]
target_2 = [l[1] for l in target]
target_3 = [l[2] for l in target]
target_4 = [l[3] for l in target]
target_5 = [l[4] for l in target]

# EXPORT TO CSV
l = list(zip(source, target_1, target_2, target_3, target_4, target_5)) # zip the two lists
df = pd.DataFrame(l, columns=["Source language", "Translation 1", 
                              "Translation 2", "Translation 3", 
                              "Translation 4", "Translation 5"])
csv = df.to_csv(f_test, sep=',')

    

