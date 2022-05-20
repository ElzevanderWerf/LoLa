"""Prepare CSV of rankings that can be used by TrueSkill"""
import pandas as pd

# TODO change file names. Import results
df1 = pd.read_csv("../results/CSVs/ex1.csv", header=0)
df2 = pd.read_csv("../results/CSVs/ex2.csv", header=0)
df3 = pd.read_csv("../results/CSVs/ex3.csv", header=0)
DFs = [df1, df2, df3]

# Import fluency ranking items
frItems = pd.read_csv("../materials/experimental_items/fr-items123.csv", header=0)

n = 140 # total number of ranks

segmentIds, system1Ids, system2Ids, system3Ids, system1ranks, system2ranks, system3ranks = [], [], [], [], [], [], []

for df in DFs:
    # Get FR columns
    frQs = df.loc[:,"FR-GGC0-T1":"FR-RG9-T3"]
    for q in range(20):
        for index, row in frQs.iloc[:,q*3:q*3+3].iterrows():
            segmentIds.append(q)
            system1Ids.append(frItems.loc[q, "Translation 1"])
            system2Ids.append(frItems.loc[q, "Translation 2"])
            system3Ids.append(frItems.loc[q, "Translation 3"])
            system1ranks.append(row[0])
            system2ranks.append(row[1])
            system3ranks.append(row[2])
    
frDF = pd.DataFrame(data={
    "segmentId":segmentIds,
    "system1Id":system1Ids,
    "system2Id":system2Ids,
    "system3Id":system3Ids,
    "system1rank":system1ranks,
    "system2rank":system2ranks,
    "system3rank":system3ranks,
    })

# TODO GGC vs RG
# TODO WB vs NWB

frDF.to_csv("wmt-trueskill/data/fol-en-all.csv", sep=',')