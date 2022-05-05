"""This script combines the ggc and rg formulas and translations into two
CSVs of experimental items per task (one for NLI and one for FR)."""

import pandas as pd
import random

# Open files
with open("data/ggc-formulas.tmp") as f1, open("data/ggc-base.tmp") as f2, open("data/ggc-rantaI.tmp") as f3, open("data/ggc-rantaII.tmp") as f4, open("data/rg-formulas.tmp") as f5, open("data/rg-base.tmp") as f6, open("data/rg-rantaI.tmp") as f7, open("data/rg-rantaII.tmp") as f8:
    ggc_formulas = f1.read().splitlines()
    ggc_base = f2.read().splitlines()
    ggc_rantaI = f3.read().splitlines()
    ggc_rantaII = f4.read().splitlines()
    rg_formulas = f5.read().splitlines()
    rg_base = f6.read().splitlines()
    rg_rantaI = f7.read().splitlines()
    rg_rantaII = f8.read().splitlines()
for f in [f1, f2, f3, f4, f5, f6, f7, f8]:
    f.close()

# Select subset of items
items = 20
ggc_indices = random.sample(range(0,len(ggc_formulas), items))
rg_indices = range(0,items) #formulas were generated randomly, so they don't have to be picked randomly.

# Export to CSVs
# GGC
ggc = list(zip([l[i] for i in ggc_indices for l in [ggc_formulas, ggc_base, ggc_rantaI, ggc_rantaII]]))
df = pd.DataFrame(ggc, columns=["Formula", "Baseline", "RantaI", "RantaII"])
csv = df.to_csv("ggc-items", sep=',')

# RG
rg = list(zip([l[i] for i in rg_indices for l in [rg_formulas, rg_base, rg_rantaI, rg_rantaII]]))
df = pd.DataFrame(rg, columns=["Formula", "Baseline", "RantaI", "RantaII"])
csv = df.to_csv("rg-items", sep=',')
    

