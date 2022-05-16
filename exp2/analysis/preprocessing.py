"""Preprocessing of the 3 TSVs of experimental results."""
import pandas as pd

# TODO change file names
df1 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")
df2 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")
df3 = pd.read_csv("../results/TSVs/ex.tsv", header=0, sep="\t")

col = ["Timestamp", "InformedConsent", "Gender", "Age", "EnglishLevel", 
       "LogicLevel", "LogicPerspective"] + [
           "NLI-GGC" + str(i) for i in range(0,21)] + [
               "NLI-RG" + str(i) for i in range(0,21)] + [
                   "FR-GGC" + str(i) + j for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                       "FR-RG" + str(i) + j  for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                           "FinalComments"]


df1.to_csv("../results/CSVs/ex1.csv", header = col)
df2.to_csv("../results/CSVs/ex2.csv", header = col)
df3.to_csv("../results/CSVs/ex3.csv", header = col)