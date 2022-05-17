"""Preprocessing of the 3 TSVs of experimental results."""
import pandas as pd

# Read results
# TODO change file names
df1 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")
df2 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")
df3 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")

DFs = [df1, df2, df3]

# New column names
cols = ["Timestamp", "InformedConsent", "Gender", "Age", "EnglishLevel", 
       "LogicLevel", "LogicPerspective"] + [
           "NLI-GGC" + str(i) for i in range(0,21)] + [
               "NLI-RG" + str(i) for i in range(0,21)] + [
                   "FR-GGC" + str(i) + "-" + j for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                       "FR-RG" + str(i) + "-" + j  for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                           "FinalComments"]

# Values to replace                          
qDict = {"Lower level than the ones below":1,
         "Level of a bachelor/master student who has followed 1 or 2 classes of logic.":2,
         "Level of a bachelor/master student who has followed more than 2 classes of logic.":3,
         "Higher level than the ones above":4,
         "(Most fluent) 1":1,
         "2":2,
         "3 (Least fluent)":3
         }

# Hypotheses
hyps = pd.read_csv("../materials/experimental_items/nli-hypotheses123.csv", header=0)

for df in DFs:
    # Rename columns
    df.columns = cols
    
    # Replace values with qDict
    df.replace(qDict, value=None, inplace=True)
    
    # Process NLI answers as being correct or incorrect
    nliQs = df.iloc[:,7:49].copy()
    for colName, col in nliQs.items():
        if colName.startswith("NLI-GGC"):
            i = int(colName[7:])
            correct = hyps.loc[i, "CorrectAnswer"]
            col.replace(regex={correct:"Correct", "^(.(?<!"+correct+'))*?$':"Incorrect"}, 
                        inplace=True)
        elif colName.startswith("NLI-RG"):
            i = int(colName[6:])
            correct = hyps.loc[i+21, "CorrectAnswer"]
            col.replace(regex={correct:"Correct", "^(.(?<!"+correct+'))*?$':"Incorrect"}, 
                        inplace=True)
    df.iloc[:,7:49] = nliQs.copy()

# Write to CSVs
# TODO change file names
df1.to_csv("../results/CSVs/ex1.csv")
df2.to_csv("../results/CSVs/ex2.csv")
df3.to_csv("../results/CSVs/ex3.csv")