"""Prints statistics of the participants' answers to the NLI questions
in the survey."""
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
from bioinfokit.analys import stat

# Import results
df1 = pd.read_csv("../results/CSVs/2.1 results.csv", header=0)
df2 = pd.read_csv("../results/CSVs/2.2 results.csv", header=0)
df3 = pd.read_csv("../results/CSVs/2.3 results.csv", header=0)

DFs = [df1, df2, df3]

lines = []  # analysis output
participants = sum([len(df) for df in DFs])

def lookUpNLI(df, indices):
    nliQs = df.loc[:, df.columns.str.startswith("NLI")]
    
    #the answers per question
    answers = [list(nliQs.iloc[:,i]) for i in indices] 
    
    #the percentage of correct answers per question
    return [answers[q].count("Correct") / len(answers[q]) * 100
                             for q in range(len(indices))]

##############################################################################
lines.append("PARTICIPANT PERFORMANCE")

lines.append("\nMean percentage of correct answers per participant")
correctPerP = [list(df.loc[j, df.columns.str.startswith("NLI")]).count("Correct")/42*100
               for df in DFs for j in range(len(df))]
lines.append("\tMean: {}".format(np.mean(correctPerP)))
lines.append("\tSD: {}".format(np.std(correctPerP)))

lines.append("\nParticipants with percentage of correct answers more than 2 standard deviations from the mean:")
for i in range(len(DFs)):
    lines.append("\tSurvey {}".format(i+1))
    for j in range(len(DFs[i])):
        correct = list(DFs[i].loc[j, DFs[i].columns.str.startswith("NLI")]
                       ).count("Correct") / 42 * 100
        
        # Throw away participants' answers more than 2 SDs from the mean
        if correct < np.mean(correctPerP) - 2 * np.std(correctPerP) or correct > np.mean(correctPerP) + 2 * np.std(correctPerP):
            lines.append("\t\tParticipant {}: {} percent --> dropped from analysis".format(j + 1, correct))
            DFs[i].drop(j, inplace=True)

##############################################################################
# Question sets
(GGC1, GGC2, GGC3, RG1, RG2, RG3) = (range(0,7), 
                                     range(7,14), 
                                     range(14,21), 
                                     range(21,28), 
                                     range(28,35), 
                                     range(35,42))

def latinSquare(ordering):
    return lookUpNLI(ordering[0], GGC1) + lookUpNLI(
    ordering[1], GGC2) + lookUpNLI(
    ordering[2], GGC3)+ lookUpNLI(
    ordering[0], RG1)+ lookUpNLI(
    ordering[1], RG2)+ lookUpNLI(
    ordering[2], RG3)

baseline = latinSquare([df1, df3, df2])
ranta = latinSquare([df2, df1, df3])
lola = latinSquare([df3, df2, df1])
systems = [baseline, ranta, lola]
systemDF = pd.DataFrame(list(zip(baseline, ranta, lola)), 
                  columns = ["BASELINE", "RANTA", "LoLa"])

# Throw away outlier questions if more than 2SDs from the mean
lines.append("\nQUESTION OUTLIERS")
allSs = baseline + ranta + lola
lines.append("\nMean percentage of correct answers per question")
lines.append("\tMean: {}".format(np.mean(allSs)))
lines.append("\tSD: {}".format(np.std(allSs)))

lines.append("\nQuestions with percentage of correct answers more than 2 standard deviations from the mean:") 
toDrop = set()
allSs = baseline + ranta + lola
for q in range(len(baseline)):
    m = (baseline[q] + ranta[q] + lola[q]) / 3
    if m < np.mean(allSs) - 2 * np.std(allSs) or m > np.mean(allSs) + 2 * np.std(allSs):
        lines.append("\tQuestion {}: {} percent --> dropped from analysis".format(
                q + 1, m))
        toDrop.add(q)

systemDF.drop(systemDF.index[list(toDrop)], inplace=True)
        
# Averages
lines.append("\nDESCRIPTIVE STATISTICS OF THE PERCENTAGE OF CORRECT ANSWERS PER SYSTEM:\n{}".format(
    systemDF.describe()))
 
##############################################################################       
# Well-behavedness
nli_items = pd.read_csv("../materials/experimental_items/nli-items1.csv", header=0)
WBness = list(nli_items.loc[:,"Well-behavedness"])
WBness = ["" if i in toDrop else WBness[i] for i in range(len(WBness))]

WBPerDF = [lookUpNLI(df, [i for i in range(len(WBness)) if WBness[i] == "WB"]) 
           for df in DFs]
NWBPerDF = [lookUpNLI(df, [i for i in range(len(WBness)) if WBness[i] == "NWB"]) 
            for df in DFs]

WB = [np.mean([WBPerDF[0][i], WBPerDF[1][i], WBPerDF[2][i]]) for i in range(len(WBPerDF[0]))]
NWB = [np.mean([NWBPerDF[0][i], NWBPerDF[1][i], NWBPerDF[2][i]]) for i in range(len(NWBPerDF[0]))]

lines.append("\nWB: percentage correct: Mean: {}, SD: {}".format(
    np.mean(WB), np.std(WB)))
lines.append("NWB: percentage correct: Mean: {}, SD: {}".format(
    np.mean(NWB), np.std(NWB)))

##############################################################################
lines.append("\nHYPOTHESIS 1-3, 7: TWO-WAY ANOVA")
# Prepare DF
WBness = [i for i in WBness if i != ""]
wellbehavedness = ["Well-behaved" if i == "WB" else "Ill-behaved" for i in WBness]
systemWBnessDF = pd.DataFrame({"WBness": wellbehavedness * 3,
                       "System": ["BASELINE"] * len(systemDF) + ["RANTA"] * len(systemDF) + ["LoLa"] * len(systemDF),
                       "Correctness":list(systemDF.loc[:,"BASELINE"]) + list(systemDF.loc[:,"RANTA"]) + list(systemDF.loc[:,"LoLa"])})

# Make boxplot of data distribution
ax = sns.boxplot(x="WBness", y="Correctness", hue="System", data=systemWBnessDF, 
                 palette="Set2", order=["Ill-behaved", "Well-behaved"])
ax.set_xlabel("Formula type")
ax.set_ylabel("Percentage of correct answers")
plt.legend(title="Translation system", loc="lower right")
plt.show() #graph of ANOVA results

# TWO-WAY ANOVA
model = ols('Correctness ~ C(WBness) + C(System) + C(WBness):C(System)', 
            data=systemWBnessDF).fit()
lines.append(sm.stats.anova_lm(model, typ=2))

# If interaction is significant, visualize interaction plot (the lines should not be parallel, but cross):
fig = interaction_plot(x=systemWBnessDF['WBness'], 
                       trace=systemWBnessDF['System'], 
                       response=systemWBnessDF['Correctness'], 
                       colors=['#66c2a5','#8da0cb', '#fc8d62'], 
                       xlabel="Formula type", 
                       ylabel = "percentage of correct answers")
plt.legend(title="Translation system")
plt.show()

# Post-hoc test if statistical differences are found, to see which pairs of systems are different from each other
res = stat()

# 1. For main effect WBness
res.tukey_hsd(df=systemWBnessDF, res_var='Correctness', xfac_var='WBness', 
              anova_model='Correctness~C(WBness)+C(System)+C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for main effect WBness:\n{}".format(res.tukey_summary))

# 2. For main effect System
res.tukey_hsd(df=systemWBnessDF, res_var='Correctness', xfac_var='System', 
              anova_model='Correctness ~ C(WBness) + C(System) + C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for main effect System:\n{}".format(res.tukey_summary))

# 3. For interaction effect between WBness and System
res.tukey_hsd(df=systemWBnessDF, res_var='Correctness', xfac_var=['WBness','System'], 
              anova_model='Correctness ~ C(WBness) + C(System) + C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for interaction effect WBness and System:\n{}".format(res.tukey_summary))

# # Checking ANOVA assumptions
# sm.qqplot(res.anova_std_residuals, line='45')
# plt.xlabel("Theoretical Quantiles")
# plt.ylabel("Standardized Residuals")
# plt.show()

# # histogram
# plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 
# plt.xlabel("Residuals")
# plt.ylabel('Frequency')
# plt.show()

# # 1. Shapiro-Wilk test for checking assumption that there is a normal distribution of residuals
# w, pvalue = stats.shapiro(res.anova_model_out.resid)
# lines.append("\nShapiro-Wilk test:\tw: {}\tp-value:{}".format(w, pvalue))
# # If the p value is non significant, we fail to reject null hypothesis and conclude that data is drawn from normal distribution
# # So if not significant -> normal distribution!

# # 2. Levene's test for checking homogeneity of variances
# res = stat()
# res.levene(df=systemWBnessDF, res_var='Correctness', xfac_var=['WBness', 'System'])
# lines.append("\nLevene's test:\n{}".format(res.levene_summary))
# # If the p value  is non-significant, we fail to reject the null hypothesis and conclude that treatments have equal variances.
# # So if not significant -> homogeneity of variances!

with open("out/nli.txt", "w") as f:
    f.writelines("%s\n" % l for l in lines)