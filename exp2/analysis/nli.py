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
# TODO check for participant outliers
# TODO colors in figures

##############################################################################
lines.append("HYPOTHESIS 1-3: COMPARING THE THREE SYSTEMS")
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
ranta = latinSquare([df2, df1, df3])
lola = latinSquare([df3, df2, df1])

# Averages
lines.append("\tBASELINE percentage correct: Mean: {}, SD:{}".format(
    np.mean(baseline), np.std(baseline)))
lines.append("\tRANTA percentage correct: Mean: {}, SD:{}".format(
    np.mean(ranta), np.std(ranta)))
lines.append("\tLoLa percentage correct: Mean: {}, SD:{}".format(
    np.mean(lola), np.std(lola)))
        
# # T-tests
# # Mean proportion of correct answers per question. Then compare these
# # percentages per group
# lines.append("\n\tT-test BASELINE vs RANTA: {}".format(ttest_ind(baseline, ranta)))
# lines.append("\tT-test BASELINE vs LoLa: {}".format(ttest_ind(baseline, lola)))
# lines.append("\tT-test RANTA vs LoLa: {}".format(ttest_ind(ranta, lola)))

# ANOVA
lines.append("\nOne-way ANOVA for checking whether there are differences between the systems:")
df = pd.DataFrame(list(zip(baseline, ranta, lola)), columns = ["BASELINE", "RANTA", "LoLa"])
df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=["BASELINE", "RANTA", "LoLa"])
df_melt.columns = ["index", "Systems", "Correctness"]

ax = sns.boxplot(x='Systems', y='Correctness', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="Systems", y="Correctness", data=df_melt, color='#7d0013')
ax.set_xlabel("Translation system")
ax.set_ylabel("Percentage of correct answers")
plt.show() #graph of ANOVA results

# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(df['BASELINE'], df['RANTA'], df['LoLa'])
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
w, pvalue = stats.bartlett(df['BASELINE'], df['RANTA'], df['LoLa'])
lines.append("\nBartlett's test:\tw: {}\tP-value: {}".format(w, pvalue))

# Levene's test to check the homogeneity of variances
# Null-hypothesis: samples from populations have equal variances
# If the p value  is non-significant, we fail to reject the null hypothesis and conclude that treatments have equal variances.
# So if not significant -> homogeneity of variances!
# TODO use this is data not drawn from normal distribution! Otherwise Bartlett
res = stat()
res.levene(df=df_melt, res_var='Correctness', xfac_var='Systems')
lines.append("\nLevene's test:\n{}".format(res.levene_summary))

# ##############################################################################
# lines.append("\n\nGGC VS RG FORMULAS")
# ggcPerDF = [lookUpNLI(df, list(chain(GGC1, GGC2, GGC3))) for df in DFs]
# ggc = [np.mean([ggcPerDF[0][i], ggcPerDF[1][i], ggcPerDF[2][i]]) 
#        for i in range(len(ggcPerDF[0]))]

# rgPerDF = [lookUpNLI(df, list(chain(RG1, RG2, RG3))) for df in DFs]
# rg = [np.mean([rgPerDF[0][i], rgPerDF[1][i], rgPerDF[2][i]]) 
#       for i in range(len(rgPerDF[0]))]

# # Averages
# lines.append("\tGGC: {} percent correct".format(np.mean(ggc)))
# lines.append("\tRG: {} percent correct".format(np.mean(rg)))
        
# # T-tests
# # Mean proportion of correct answers per question. Then compare these
# # percentages per group
# lines.append("\n\tT-test GGC vs RG: {}".format(ttest_ind(ggc, rg)))


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
lines.append("\tWB: {} percent correct".format(np.mean(WB)))
lines.append("\tNWB: {} percent correct".format(np.mean(NWB)))

# # T-tests
# # Mean proportion of correct answers per question. Then compare these
# # percentages per group
# lines.append("\nT-test WB vs NWB: {}".format(ttest_ind(WB, NWB)))

# ANOVA to test interaction effects:
# Does understandability of WB vs NWB depend on whether they are translated
# by RANTA or LoLa?

lines.append("\nTwo-way ANOVA for testing interaction between well-behavedness and systems")

# Prepare DF
anovaDF = pd.DataFrame({"WBness": np.repeat(WBness, 3),
                       "System": ["BASELINE"] * 42 + ["RANTA"] * 42 + ["LoLa"] * 42,
                       "Correctness":baseline + ranta + lola})

# Make boxplot of data distribution
ax = sns.boxplot(x="WBness", y="Correctness", hue="System", data=anovaDF, palette="Set3")
ax.set_xlabel("Translation system")
ax.set_ylabel("Percentage of correct answers")
# TODO legend location
plt.show() #graph of ANOVA results

# ANOVA
model = ols('Correctness ~ C(WBness) + C(System) + C(WBness):C(System)', 
            data=anovaDF).fit()
lines.append("Two-way ANOVA output for WBness:\n{}".format(sm.stats.anova_lm(model, typ=2)))

# If interaction is significant, visualize interaction plot (the lines should not be parallel, but cross):
fig = interaction_plot(x=anovaDF['WBness'], trace=anovaDF['System'], response=anovaDF['Correctness'], 
    colors=['#4c061d','#d17a22', '#b4c292'], xlabel="Well-behavedness", ylabel = "Translation system")
plt.show()

# Post-hoc test if statistical differences are found, to see which pairs of systems are different from each other
res = stat()

# 1. For main effect WBness
res.tukey_hsd(df=anovaDF, res_var='Correctness', xfac_var='WBness', anova_model='Correctness~C(WBness)+C(System)+C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for main effect WBness:\n{}".format(res.tukey_summary))

# 2. For main effect System
res.tukey_hsd(df=anovaDF, res_var='Correctness', xfac_var='System', anova_model='Correctness ~ C(WBness) + C(System) + C(WBness):C(System)')
lines.append("\nTukey's HSD post-hoc for main effect System:\n{}".format(res.tukey_summary))

# 3. For interaction effect between WBness and System
res.tukey_hsd(df=anovaDF, res_var='Correctness', xfac_var=['WBness','System'], anova_model='Correctness ~ C(WBness) + C(System) + C(WBness):C(System)')
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
res.levene(df=anovaDF, res_var='Correctness', xfac_var=['WBness', 'System'])
lines.append("\nLevene's test:\n{}".format(res.levene_summary))
# If the p value  is non-significant, we fail to reject the null hypothesis and conclude that treatments have equal variances.
# So if not significant -> homogeneity of variances!

# TODO write to output txt doc + save the final figures
for l in lines:
    print(l)