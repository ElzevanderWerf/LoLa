"""This script combines the ggc and rg formulas and translations into two
CSVs of experimental items per task (one for NLI and one for FR)."""

import pandas as pd
import random
from replaceSymbols import replace_symbols, replace_bulleting, add_punctuation

# Import data
with open(
        "data/ggc-formulas.tmp") as f1, open(
            "data/ggc-base.tmp") as f2, open(
                "data/ggc-rantaI.tmp") as f3, open(
                    "data/ggc-rantaII.tmp") as f4, open(
                        "data/rg-formulas.tmp") as f5, open(
                            "data/rg-base.tmp") as f6, open(
                                "data/rg-rantaI.tmp") as f7, open(
                                    "data/rg-rantaII.tmp") as f8:                    
    ggc_formulas = [replace_symbols(replace_bulleting(s)) for s in f1.read().splitlines()]
    ggc_base = list(filter(None, f2.read().splitlines()))
    ggc_rantaI = list(filter(None, f3.read().splitlines()))
    ggc_rantaII = list(filter(None, f4.read().splitlines()))
    ggc_WB = [s.split(",")[0] for s in ggc_rantaII]
    ggc_rantaII = [",".join(s.split(",")[2:]) for s in ggc_rantaII]
    ggc_type = ["GGC"] * len(ggc_formulas)
    
    rg_formulas = [replace_symbols(replace_bulleting(s)) for s in f5.read().splitlines()]
    rg_base = list(filter(None, f6.read().splitlines()))
    rg_rantaI = list(filter(None, f7.read().splitlines()))
    rg_rantaII = list(filter(None, f8.read().splitlines()))
    rg_WB = [s.split(",")[0] for s in rg_rantaII]
    rg_rantaII = [",".join(s.split(",")[2:]) for s in rg_rantaII]
    rg_type = ["RG"] * len(rg_formulas)

for f in [f1, f2, f3, f4, f5, f6, f7, f8]:
    f.close()

# Select subset of items
items = 20
half_items = int(items/2)
ggc_indices = random.sample(range(0,len(ggc_formulas)), items)
rg_indices = range(0,items) #formulas were generated randomly, so they don't have to be picked randomly.

ggc = list(zip(ggc_type, ggc_WB, ggc_formulas, ggc_base, ggc_rantaI, ggc_rantaII))
rg = list(zip(rg_type, rg_WB, rg_formulas, rg_base, rg_rantaI, rg_rantaII))

# Export to CSVs
# NLI
nli = [ggc[i] for i in ggc_indices[:7]] + [rg[i] for i in rg_indices[:7]] #TODO change 7
df = pd.DataFrame(nli, columns=["Type", "Well-behavedness", "Formula", "Baseline", "RantaI", "RantaII"])
df.insert(len(df.columns), "Hypothesis", "H", allow_duplicates=True)
df.insert(len(df.columns), "CorrectAnswer", "Y/N", allow_duplicates=True)
df[["Baseline", "RantaI", "RantaII"]] = df[["Baseline", "RantaI", "RantaII"]].applymap(lambda x: add_punctuation(x))
csv = df.to_csv("data/nli-items.csv", sep=',')

# FR
fr = [ggc[i] for i in ggc_indices[half_items:]] + [rg[i] for i in rg_indices[half_items:]]
df = pd.DataFrame(fr, columns=["Type", "Well-behavedness", "Formula", "Baseline", "RantaI", "RantaII"])
df["Translation 1"] = ""
df["Translation 2"] = ""
df["Translation 3"] = ""
for index, row in df.iterrows():
    l = ["Baseline", "RantaI", "RantaII"]
    random.shuffle(l)
    row["Translation 1"] = l[0]
    row["Translation 2"] = l[1]
    row["Translation 3"] = l[2]
df[["Baseline", "RantaI", "RantaII"]] = df[["Baseline", "RantaI", "RantaII"]].applymap(lambda x: add_punctuation(x))
csv = df.to_csv("data/fr-items.csv", sep=',')

    

