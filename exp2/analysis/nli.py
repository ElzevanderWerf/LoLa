"""Prints statistics of the participants' answers to the NLI questions
in the survey."""
import pandas as pd
import numpy as np
from itertools import chain
from scipy.stats.stats import ttest_ind

# TODO change file names. Import results
df1 = pd.read_csv("../results/CSVs/ex1.csv", header=0)
df2 = pd.read_csv("../results/CSVs/ex2.csv", header=0)
df3 = pd.read_csv("../results/CSVs/ex3.csv", header=0)

DFs = [df1, df2, df3]

lines = []  # The output
participants = sum([len(df) for df in DFs])

def lookUpNLI(df, indices):
    nliQs = df.loc[:, df.columns.str.startswith("NLI")]
    
    #the answers per question
    answers = [list(nliQs.iloc[:,i]) for i in indices] 
    
    #the percentage of correct answers per question
    return [answers[q].count("Correct") / len(answers[q])
                             for q in range(len(indices))]

##############################################################################
lines.append("COMPARISON BETWEEN THE 3 SYSTEMS")
# Question sets
(GGC1, GGC2, GGC3, RG1, RG2, RG3) = (range(0,7), range(7,14), range(14,21), 
                                     range(21,28), range(28,35), range(35,42))

def latinSquare(ordering):
    return lookUpNLI(ordering[0], GGC1) + lookUpNLI(
    ordering[1], GGC2) + lookUpNLI(
    ordering[2], GGC3)+ lookUpNLI(
    ordering[0], RG1)+ lookUpNLI(
    ordering[1], RG2)+ lookUpNLI(
    ordering[2], RG3)

baseline = latinSquare([df1, df3, df2])
rantaI = latinSquare([df2, df1, df3])
rantaII = latinSquare([df3, df2, df1])

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


##############################################################################
lines.append("\n\nGGC VS RG FORMULAS")
ggcPerDF = [lookUpNLI(df, list(chain(GGC1, GGC2, GGC3))) for df in DFs]
ggc = [np.mean([ggcPerDF[0][i], ggcPerDF[1][i], ggcPerDF[2][i]]) 
       for i in range(len(ggcPerDF[0]))]

rgPerDF = [lookUpNLI(df, list(chain(RG1, RG2, RG3))) for df in DFs]
rg = [np.mean([rgPerDF[0][i], rgPerDF[1][i], rgPerDF[2][i]]) 
      for i in range(len(rgPerDF[0]))]

# Averages
lines.append("\tGGC: {} percent correct".format(np.mean(ggc)))
lines.append("\tRG: {} percent correct".format(np.mean(rg)))
        
# T-tests
# Mean proportion of correct answers per question. Then compare these
# percentages per group
lines.append("\n\tT-test GGC vs RG: {}".format(ttest_ind(ggc, rg)))


##############################################################################
lines.append("\n\nWB VS NWB FORMULAS")
#TODO check difference between Ranta-I and Ranta-II
   
nli_items = pd.read_csv("../materials/experimental_items/nli-items1.csv", header=0)
WBness = nli_items.loc[:,"Well-behavedness"]

WB_indices = [i for i in range(len(WBness)) if WBness[i] == "WB"]
NWB_indices = [i for i in range(len(WBness)) if WBness[i] == "NWB"]

WBPerDF = [lookUpNLI(df, WB_indices) for df in DFs]
NWBPerDF = [lookUpNLI(df, NWB_indices) for df in DFs]

WB = [np.mean([WBPerDF[0][i], WBPerDF[1][i], WBPerDF[2][i]]) for i in range(len(WBPerDF[0]))]
NWB = [np.mean([NWBPerDF[0][i], NWBPerDF[1][i], NWBPerDF[2][i]]) for i in range(len(NWBPerDF[0]))]

# Averages
lines.append("\tWB: {} percent correct".format(np.mean(WB)))
lines.append("\tNWB: {} percent correct".format(np.mean(NWB)))

# T-tests
# Mean proportion of correct answers per question. Then compare these
# percentages per group
lines.append("\n\tT-test WB vs NWB: {}".format(ttest_ind(WB, NWB)))


for l in lines:
    print(l)