"""This script combines the ggc and rg formulas and translations into 4
CSVs of experimental items: 3 NLI question sets and 1 FR question set
(126 NLI questions are divided over 3 participant groups according to a
 Latin Square Design)."""

import pandas as pd
import random
from preprocessing import replace_symbols, replace_bulleting, add_punctuation

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
    ggc_formulas = [replace_symbols(s) for s in f1.read().splitlines()]
    ggc_base = list(filter(None, f2.read().splitlines()))
    ggc_rantaI = list(filter(None, f3.read().splitlines()))
    ggc_rantaII = list(filter(None, f4.read().splitlines()))
    ggc_WB = [s.split(",")[0] for s in ggc_rantaII]
    ggc_rantaII = [", ".join(s.split(", ")[2:]) for s in ggc_rantaII]
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

# Select subset of GGC and RG items
items = 42 + 20     #nli + fr
random.seed(500)
ggc_indices = random.sample(range(0,len(ggc_formulas)), int(items/2))
rg_indices = range(0,int(items/2))     #formulas were generated randomly, so they don't have to be picked randomly.

ggc = list(zip(ggc_type, ggc_WB, ggc_formulas, ggc_base, ggc_rantaI, ggc_rantaII))
ggc_sub = [ggc[i] for i in ggc_indices]
ggc_df = pd.DataFrame(ggc_sub, columns=["Type", "Well-behavedness", "Formula", "Baseline", "RantaI", "RantaII"])

rg = list(zip(rg_type, rg_WB, rg_formulas, rg_base, rg_rantaI, rg_rantaII))
rg_sub = [rg[i] for i in rg_indices]
rg_df = pd.DataFrame(rg_sub, columns=["Type", "Well-behavedness", "Formula", "Baseline", "RantaI", "RantaII"])

# NLI
def makeNLI_DF(df, order, hypotheses, correct_answers):
    """
    Returns a DataFrame of NLI items for a given ordering of translation
    systems over the 3 question sets.
    """

    systems = 2 * (7 * [order[0]] + 7 * [order[1]] + 7 * [order[2]])
    df.insert(len(df.columns), "System", systems, allow_duplicates=True)
    translations = pd.concat([ggc_df.loc[:6, order[0]], 
                              ggc_df.loc[7:13, order[1]],
                              ggc_df.loc[14:20, order[2]],
                              rg_df.loc[:6, order[0]],
                              rg_df.loc[7:13, order[1]],
                              rg_df.loc[14:20, order[2]]])
    translations = [add_punctuation(replace_bulleting(t)) for t in translations]
    df.insert(len(df.columns), "Translation", translations, allow_duplicates=True)
    
    # Empty (to be filled) columns for hypotheses and correct NLI answer
    df.insert(len(df.columns), "Hypothesis", hypotheses, allow_duplicates=True)
    df.insert(len(df.columns), "CorrectAnswer", correct_answers, allow_duplicates=True)
    return df

# Hypotheses and correct answers (made them myself)
hypotheses = 42 * ["H"]
correct_answers = 42 * ["Y/N"]

# Survey 1, 2 and 3
nli_df = pd.concat([ggc_df.loc[:20, ["Type", "Well-behavedness", "Formula"]], 
                rg_df.loc[:20, ["Type", "Well-behavedness", "Formula"]]])

nli1_df = makeNLI_DF(nli_df, ["Baseline", "RantaI", "RantaII"], hypotheses, correct_answers)
nli1_df.to_csv("experimental_items/nli-items1.csv", sep=',')

nli2_df = makeNLI_DF(nli_df, ["RantaI", "RantaII", "Baseline"], hypotheses, correct_answers)
nli2_df.to_csv("experimental_items/nli-items2.csv", sep=',')

nli3_df = makeNLI_DF(nli_df, ["RantaII", "Baseline", "RantaI"], hypotheses, correct_answers)
nli3_df.to_csv("experimental_items/nli-items3.csv", sep=',')

all_df = pd.concat([ggc_df.loc[:20], rg_df.loc[:20]])
all_df.to_csv("experimental_items/nli-items123.csv", sep=',')

# FR
fr_df = pd.concat([ggc_df.loc[21:], 
                   rg_df.loc[21:]], 
                  axis=0)
fr_df[["Baseline", "RantaI", "RantaII"]] = fr_df[["Baseline", "RantaI", "RantaII"]].applymap(lambda x: add_punctuation(replace_bulleting(x)))

# For shuffling the three translations per FR item
fr_df["Translation 1"] = ""
fr_df["Translation 2"] = ""
fr_df["Translation 3"] = ""
for index, row in fr_df.iterrows():
    l = ["Baseline", "RantaI", "RantaII"]
    random.shuffle(l)
    row["Translation 1"] = l[0]
    row["Translation 2"] = l[1]
    row["Translation 3"] = l[2]
csv = fr_df.to_csv("experimental_items/fr-items123.csv", sep=',')

    

