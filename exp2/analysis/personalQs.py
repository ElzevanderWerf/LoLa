"""Prints statistics of the participants' answers to the personal questions
in the survey (gender, age, etc.)."""
import pandas as pd
from itertools import chain
import numpy as np

# TODO change file names
df1 = pd.read_csv("../results/CSVs/2.1 results - intermediate version.csv", header=0)
df2 = pd.read_csv("../results/CSVs/2.2 results - intermediate version.csv", header=0)
df3 = pd.read_csv("../results/CSVs/2.3 results - intermediate version.csv", header=0)


DFs = [df1, df2, df3]

def lookUp(column):
    return list(chain(*[list(df.loc[:,column]) for df in DFs]))

lines = []
participants = sum([len(df) for df in DFs])
lines.append("PARTICIPANTS")
lines.append("Participants per survey:\n\tSurvey1:\t{}\n\tSurvey2:\t{}\n\tSurvey3:\t{}".format(
    len(df1), len(df2), len(df3)))
lines.append("Total:\t{} participants".format(participants))

lines.append("\nGENDER")
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

lines.append("\nAGE")
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

lines.append("\nPARTICIPATED IN EXP1")
prevExp = lookUp("ParticipatedInExp1")
lines.append("\tYes: {} out of {} is {} percent".format(
    prevExp.count("Yes"), 
    participants, 
    prevExp.count("Yes")/participants))
lines.append("\tNo: {} out of {} is {} percent".format(
    prevExp.count("No"), 
    participants, 
    prevExp.count("No")/participants))

for l in lines:
    print(l)

