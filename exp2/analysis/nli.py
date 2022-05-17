"""Prints statistics of the participants' answers to the NLI questions
in the survey."""
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr, ttest_ind

# TODO change file names
df1 = pd.read_csv("../results/CSVs/ex1.csv", header=0)
df2 = pd.read_csv("../results/CSVs/ex2.csv", header=0)
df3 = pd.read_csv("../results/CSVs/ex3.csv", header=0)

DFs = [df1, df2, df3]

lines = []
participants = sum([len(df) for df in DFs])


lines.append("COMPARISON BETWEEN THE 3 SYSTEMS")
def lookUpNLI(df,formulaType, indexTup):
    answersPerParticipant = df.loc[:,
                  "NLI-"+formulaType+str(indexTup[0]):
                  "NLI-"+formulaType+str(indexTup[1])].to_numpy()
    correctPercentagePerQ = []
    for a in range(0,7):
        answers = [participant[a] for participant in answersPerParticipant]
        correctPercentagePerQ.append(answers.count("Correct") / len(answers))
    return correctPercentagePerQ

# Question sets
GGC1 = RG1 = (0,6)
GGC2 = RG2 = (7,13)
GGC3 = RG3 = (14,20)

baseline = lookUpNLI(df1, "GGC", GGC1) + lookUpNLI(
    df3, "GGC", GGC2) + lookUpNLI(
    df2, "GGC", GGC3) + lookUpNLI(
    df1, "RG", RG1) + lookUpNLI(
    df3, "RG", RG2) + lookUpNLI(
    df2, "RG", RG3) 
        
rantaI = lookUpNLI(df2, "GGC", GGC1) + lookUpNLI(
    df1, "GGC", GGC2) + lookUpNLI(
    df3, "GGC", GGC3) + lookUpNLI(
    df2, "RG", RG1) + lookUpNLI(
    df1, "RG", RG2) + lookUpNLI(
    df3, "RG", RG3) 
        
rantaII = lookUpNLI(df3, "GGC", GGC1) + lookUpNLI(
    df2, "GGC", GGC2) + lookUpNLI(
    df1, "GGC", GGC3) + lookUpNLI(
    df3, "RG", RG1) + lookUpNLI(
    df2, "RG", RG2) + lookUpNLI(
    df1, "RG", RG3) 
        
# Averages
lines.append("\tBaseline: {} percent correct".format(
    np.mean(baseline)))
lines.append("\tRantaI: {} percent correct".format(
    np.mean(rantaI)))
lines.append("\tRantaII: {} percent correct".format(
    np.mean(rantaII)))

        
# T-tests
# Mean proportion of correct answers per question. Then compare these
# percentages per group
lines.append("\n\tT-test Baseline vs RantaI: {}".format(ttest_ind(baseline, rantaI)))
lines.append("\tT-test Baseline vs RantaII: {}".format(ttest_ind(baseline, rantaII)))
lines.append("\tT-test RantaI vs RantaII: {}".format(ttest_ind(rantaI, rantaII)))


lines.append("GGC VS RG")



for l in lines:
    print(l)