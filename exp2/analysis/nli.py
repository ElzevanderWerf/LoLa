"""Prints statistics of the participants' answers to the NLI questions
in the survey."""
import pandas as pd
import numpy as np
from scipy.stats.stats import ttest_ind

# TODO change file names
df1 = pd.read_csv("../results/CSVs/ex1.csv", header=0)
df2 = pd.read_csv("../results/CSVs/ex2.csv", header=0)
df3 = pd.read_csv("../results/CSVs/ex3.csv", header=0)

DFs = [df1, df2, df3]

lines = []
participants = sum([len(df) for df in DFs])


lines.append("COMPARISON BETWEEN THE 3 SYSTEMS")
def lookUpNLI(df,formulaType, rrange):
    answersPerParticipant = df.loc[:,
                  "NLI-"+formulaType+str(rrange[0]):
                  "NLI-"+formulaType+str(rrange[-1])].to_numpy()
    correctPercentagePerQ = []
    for a in range(len(rrange)):
        answers = [participant[a] for participant in answersPerParticipant]
        correctPercentagePerQ.append(answers.count("Correct") / len(answers))
    return correctPercentagePerQ

# Question sets
GGC1 = RG1 = range(0,7)
GGC2 = RG2 = range(7,14)
GGC3 = RG3 = range(14,20)

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


lines.append("\n\nGGC VS RG FORMULAS")
ggcPerDF = [lookUpNLI(df1, "GGC", range(0,21)), 
            lookUpNLI(df2, "GGC", range(0,21)), 
            lookUpNLI(df3, "GGC", range(0,21))]
ggc = [np.mean([ggcPerDF[0][i], ggcPerDF[1][i], ggcPerDF[2][i]]) for i in range(len(ggcPerDF[0]))]

rgPerDF = [lookUpNLI(df1, "RG", range(0,21)), 
            lookUpNLI(df2, "RG", range(0,21)), 
            lookUpNLI(df3, "RG", range(0,21))]
rg = [np.mean([rgPerDF[0][i], rgPerDF[1][i], rgPerDF[2][i]]) for i in range(len(rgPerDF[0]))]

# Averages
lines.append("\tGGC: {} percent correct".format(
    np.mean(ggc)))
lines.append("\tRG: {} percent correct".format(
    np.mean(rg)))
        
# T-tests
# Mean proportion of correct answers per question. Then compare these
# percentages per group
lines.append("\n\tT-test GGC vs RG: {}".format(ttest_ind(ggc, rg)))


lines.append("\n\nWB VS NWB FORMULAS")


for l in lines:
    print(l)