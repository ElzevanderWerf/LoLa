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
import scipy.stats as stats
from IPython.display import display


# TODO change file names. Import results
df1 = pd.read_csv("../results/CSVs/2.1 results - intermediate version.csv", header=0)
df2 = pd.read_csv("../results/CSVs/2.2 results - intermediate version.csv", header=0)
df3 = pd.read_csv("../results/CSVs/2.3 results - intermediate version.csv", header=0)

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
lines.append("MEAN PERCENTAGE OF CORRECT ANSWERS PER PARTICIPANT")

correctPerP = [list(df.loc[j, df.columns.str.startswith("NLI")]).count("Correct")/42
               for df in DFs for j in range(len(df))]
lines.append("correctPerP: {}".format(correctPerP))
lines.append("\tMean: {}".format(np.mean(correctPerP)))
lines.append("\tSD: {}".format(np.std(correctPerP)))

lines.append("\nParticipants with percentage of correct answers more than 2 standard deviations from the mean:")
for i in range(len(DFs)):
    lines.append("\tSurvey {}".format(i+1))
    for j in range(len(DFs[i])):
        correct = list(DFs[i].loc[j, DFs[i].columns.str.startswith("NLI")]
                       ).count("Correct") / 42
        
        # Throw away participants' answers more than 2 SDs from the mean (TODO also in FR?)
        if correct < np.mean(correctPerP) - 2 * np.std(correctPerP) or correct > np.mean(correctPerP) + 2 * np.std(correctPerP):
            lines.append("\t\tParticipant {}: {} percent --> dropped from analysis".format(j + 1, correct))
            DFs[i].drop(j, inplace=True)

##############################################################################
lines.append("\n\nHYPOTHESIS 1-3: COMPARING THE THREE SYSTEMS")
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

systemDF = pd.DataFrame(list(zip(baseline, ranta, lola)), 
                  columns = ["BASELINE", "RANTA", "LoLa"])

# Averages
lines.append("Description of the percentage of correct answers per system:\n{}".format(
    systemDF.describe()))
        
# One-way ANOVA
lines.append("\nOne-way ANOVA for checking whether there are differences between the 3 systems in general:")
df_melt = pd.melt(systemDF.reset_index(), id_vars=['index'], 
                  value_vars=["BASELINE", "RANTA", "LoLa"])
df_melt.columns = ["index", "Systems", "Correctness"]
display(df_melt)

ax = sns.catplot(x='Systems', y='Correctness', kind="box", 
                 data=df_melt, palette = "Set2")
ax.set_axis_labels("Translation system", "Percentage of correct answers")
plt.show() #graph of ANOVA results

# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(systemDF['BASELINE'], systemDF['RANTA'], systemDF['LoLa'])
lines.append("F-value: {}\tP-value: {}".format(fvalue, pvalue))

# Post-hoc test if statistical differences are found, to see which pairs of systems are different from each other
# Note: p-value 0.001 from tukey_hsd output should be interpreted as <=0.001
res = stat()
res.tukey_hsd(df=df_melt, res_var='Correctness', xfac_var='Systems', anova_model='Correctness ~ C(Systems)')
lines.append("\nTukey's HSD post-hoc:\n{}".format(res.tukey_summary))

# Testing ANOVA assumptions
# res.anova_std_residuals are standardized residuals obtained from ANOVA (check above)
sm.qqplot(res.anova_std_residuals, line='45')
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Standardized Residuals")
plt.show()

# histogram
plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 
plt.xlabel("Residuals")
plt.ylabel('Frequency')
plt.show()

# Shapiro-Wilk's test to check the normal distribution of residuals
# Null-hypothesis: data is drawn from normal distribution
# If the p value is non significant, we fail to reject null hypothesis and conclude that data is drawn from normal distribution
# So if not significant -> normal distribution!
model = ols('Correctness ~ C(Systems)', data=df_melt).fit()
w, pvalue = stats.shapiro(model.resid)
lines.append("\nShapiro-Wilk test\tw: {}\tP-value: {}".format(w, pvalue))

# Bartlett's test to check the homogeneity of variances
# Null-hypothesis: samples from populations have equal variances
# If the p value  is non-significant, we fail to reject the null hypothesis and conclude that treatments have equal variances.
# So if not significant -> homogeneity of variances!
w, pvalue = stats.bartlett(systemDF['BASELINE'], systemDF['RANTA'], systemDF['LoLa'])
lines.append("\nBartlett's test:\tw: {}\tP-value: {}".format(w, pvalue))

# Levene's test to check the homogeneity of variances
# Null-hypothesis: samples from populations have equal variances
# If the p value  is non-significant, we fail to reject the null hypothesis and conclude that treatments have equal variances.
# So if not significant -> homogeneity of variances!
# TODO use this is data not drawn from normal distribution! Otherwise Bartlett
res = stat()
res.levene(df=df_melt, res_var='Correctness', xfac_var='Systems')
lines.append("\nLevene's test:\n{}".format(res.levene_summary))

##############################################################################
lines.append("\n\n\nHYPOTHESIS 7: WB VS NWB FORMULAS")
   
nli_items = pd.read_csv("../materials/experimental_items/nli-items1.csv", header=0)
WBness = list(nli_items.loc[:,"Well-behavedness"])

WB_indices = [i for i in range(len(WBness)) if WBness[i] == "WB"]
NWB_indices = [i for i in range(len(WBness)) if WBness[i] == "NWB"]

WBPerDF = [lookUpNLI(df, WB_indices) for df in DFs]
NWBPerDF = [lookUpNLI(df, NWB_indices) for df in DFs]

WB = [np.mean([WBPerDF[0][i], WBPerDF[1][i], WBPerDF[2][i]]) for i in range(len(WBPerDF[0]))]
NWB = [np.mean([NWBPerDF[0][i], NWBPerDF[1][i], NWBPerDF[2][i]]) for i in range(len(NWBPerDF[0]))]

# Averages
lines.append("\tWB: percentage correct: Mean: {}, SD: {}".format(
    np.mean(WB), np.std(WB)))
lines.append("\tNWB: percentage correct: Mean: {}, SD: {}".format(
    np.mean(NWB), np.std(NWB)))

# ANOVA to test interaction effects:
# Does understandability of WB vs NWB depend on whether they are translated
# by RANTA or LoLa?

# Prepare DF
systemWBnessDF = pd.DataFrame({"WBness": np.repeat(WBness, 3),
                       "System": ["BASELINE"] * 42 + ["RANTA"] * 42 + ["LoLa"] * 42,
                       "Correctness":baseline + ranta + lola})

# Make boxplot of data distribution
ax = sns.boxplot(x="WBness", y="Correctness", hue="System", data=systemWBnessDF, 
                 palette="Set2")
ax.set_xlabel("Translation system")
ax.set_ylabel("Percentage of correct answers")
plt.legend(loc="lower center")
plt.show() #graph of ANOVA results

# TWO-WAY ANOVA
model = ols('Correctness ~ C(WBness) + C(System) + C(WBness):C(System)', 
            data=systemWBnessDF).fit()
lines.append("\nTwo-way ANOVA for testing interaction between well-behavedness and systems:\n{}".format(sm.stats.anova_lm(model, typ=2)))

# If interaction is significant, visualize interaction plot (the lines should not be parallel, but cross):
fig = interaction_plot(x=systemWBnessDF['WBness'], trace=systemWBnessDF['System'], response=systemWBnessDF['Correctness'], 
    colors=['#66c2a5','#fc8d62', '#8da0cb'], xlabel="Well-behavedness", ylabel = "percentage of correct answers")
plt.show()

# Post-hoc test if statistical differences are found, to see which pairs of systems are different from each other
res = stat()

# 1. For main effect WBness
res.tukey_hsd(df=systemWBnessDF, res_var='Correctness', xfac_var='WBness', anova_model='Correctness~C(WBness)+C(System)+C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for main effect WBness:\n{}".format(res.tukey_summary))

# 2. For main effect System
res.tukey_hsd(df=systemWBnessDF, res_var='Correctness', xfac_var='System', anova_model='Correctness ~ C(WBness) + C(System) + C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for main effect System:\n{}".format(res.tukey_summary))

# 3. For interaction effect between WBness and System
res.tukey_hsd(df=systemWBnessDF, res_var='Correctness', xfac_var=['WBness','System'], anova_model='Correctness ~ C(WBness) + C(System) + C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for interaction effect WBness and System:\n{}".format(res.tukey_summary))

# Checking ANOVA assumptions
sm.qqplot(res.anova_std_residuals, line='45')
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Standardized Residuals")
plt.show()

# histogram
plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 
plt.xlabel("Residuals")
plt.ylabel('Frequency')
plt.show()

# 1. Shapiro-Wilk test for checking assumption that there is a normal distribution of residuals
w, pvalue = stats.shapiro(res.anova_model_out.resid)
lines.append("\nShapiro-Wilk test:\tw: {}\tp-value:{}".format(w, pvalue))
# If the p value is non significant, we fail to reject null hypothesis and conclude that data is drawn from normal distribution
# So if not significant -> normal distribution!

# 2. Levene's test for checking homogeneity of variances
res = stat()
res.levene(df=systemWBnessDF, res_var='Correctness', xfac_var=['WBness', 'System'])
lines.append("\nLevene's test:\n{}".format(res.levene_summary))
# If the p value  is non-significant, we fail to reject the null hypothesis and conclude that treatments have equal variances.
# So if not significant -> homogeneity of variances!

# TODO write to output txt doc + save the final figures
for l in lines:
    print(l)