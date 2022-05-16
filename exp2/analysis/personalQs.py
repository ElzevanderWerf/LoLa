"""Prints statistics of the participants' answers to the personal questions
in the survey (gender, age, etc.)."""
import pandas as pd
from itertools import chain
import numpy as np
from scipy.stats.stats import pearsonr

# TODO change file names
df1 = pd.read_csv("../results/CSVs/ex1.csv", header=0)
df2 = pd.read_csv("../results/CSVs/ex2.csv", header=0)
df3 = pd.read_csv("../results/CSVs/ex3.csv", header=0)

DFs = [df1, df2, df3]

def lookUp(column):
    return list(chain(*[list(df.loc[:,column]) for df in DFs]))

lines = []
participants = sum([len(df) for df in DFs])

lines.append("GENDER")
genders = lookUp("Gender")
lines.append("\tMale: {} out of {} is {} percent".format(
    genders.count("Male"), 
    participants, 
    genders.count("Male")/participants))
lines.append("\tFemale: {} out of {} is {} percent".format(
    genders.count("Female"), 
    participants, 
    genders.count("Female")/participants))
lines.append("\tPrefer not to say: {} out of {} is {} percent".format(
    genders.count("Prefer not to say"), 
    participants, 
    genders.count("Prefer not to say")/participants))

lines.append("AGE")
ages = lookUp("Age")
lines.append("\tMean: {}".format(np.mean(ages)))
lines.append("\tSD: {}".format(np.std(ages)))

lines.append("\nENGLISH EXPERIENCE")
englishXP = lookUp("EnglishLevel")
lines.append("\tMean: {}".format(np.mean(englishXP)))
lines.append("\tSD: {}".format(np.std(englishXP)))

lines.append("\nLOGIC EXPERIENCE")
logicXP = lookUp("LogicLevel")
lines.append("\tMean: {}".format(np.mean(logicXP)))
lines.append("\tSD: {}".format(np.std(logicXP)))

lines.append("\nLOGIC PERSPECTIVE")
logicP = lookUp("LogicPerspective")
lines.append("\tComputational/mathematical: {} out of {} is {} percent".format(
    logicP.count("Computational/mathematical perspective"), 
    participants, 
    logicP.count("Computational/mathematical perspective")/participants))
lines.append("\tLinguistic/philosophical: {} out of {} is {} percent".format(
    logicP.count("Linguistic/philosophical perspective"), 
    participants, 
    logicP.count("Linguistic/philosophical perspective")/participants))
lines.append("\tOther: {} out of {} is {} percent".format(
    logicP.count("Another perspective"), 
    participants, 
    logicP.count("Another perspective")/participants))

for l in lines:
    print(l)

