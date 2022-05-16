"""Preprocessing of the 3 TSVs of experimental results."""
import pandas as pd

# Read results
# TODO change file names
df1 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")
df2 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")
df3 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")

# New column names
col = ["Timestamp", "InformedConsent", "Gender", "Age", "EnglishLevel", 
       "LogicLevel", "LogicPerspective"] + [
           "NLI-GGC" + str(i) for i in range(0,21)] + [
               "NLI-RG" + str(i) for i in range(0,21)] + [
                   "FR-GGC" + str(i) + "-" + j for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                       "FR-RG" + str(i) + "-" + j  for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                           "FinalComments"]

# Values to replace                          
qDict = {"Lower level than the ones below":0,
         "Level of a bachelor/master student who has followed 1 or 2 classes of logic.":1,
         "Level of a bachelor/master student who has followed more than 2 classes of logic.":2,
         "Higher level than the ones above":3,
         "(Most fluent) 1":1,
         "2":2,
         "3 (Least fluent)":3
         }

# Replace values with qDict and write to CSVs
# TODO change file names
df1.replace(qDict, None).to_csv("../results/CSVs/ex1.csv", header = col)
df2.replace(qDict, None).to_csv("../results/CSVs/ex2.csv", header = col)
df3.replace(qDict, None).to_csv("../results/CSVs/ex3.csv", header = col)