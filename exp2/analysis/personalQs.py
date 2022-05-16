"""Prints statistics of the participants' answers to the personal questions
in the survey (gender, age, etc.)."""
import pandas as pd

df1 = pd.read_csv("../results/ex.tsv", header=0, sep="\t")
df2 = pd.read_csv("../results/ex.tsv", header=0, sep="\t")
df3 = pd.read_csv("../results/ex.tsv", header=0, sep="\t")

# Gender
genders = df1.loc[:,"G"]