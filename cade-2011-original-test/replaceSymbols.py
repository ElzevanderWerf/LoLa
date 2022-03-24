"""Replace the GGC symbols with common FOL symbols in a given CSV file with
GGC as source language:
    >python replaceSymbols.py <CSV-file>
"""
import sys
import pandas as pd

csv = sys.argv[1]

df = pd.read_csv(csv, header=0, error_bad_lines=False)
        
def replace_symbols(s):
    """
    Replaces the GGC symbols in input string s with common FOL symbols
    """
    dct = {126:172,
       38:8743,
       124:8744,
       36:8594,
       64:8704,
       47:8707}
    return s.translate(dct)

def replace_bulleting(s):
    return s.replace(r'\item', r'\n\t'+chr(8226))
        
df["Source language"] = df["Source language"].map(replace_symbols)
df["Translation 1"] = df["Translation 1"].map(replace_bulleting)

df[["Source language", "Translation 1"]].to_csv(csv, sep=',')