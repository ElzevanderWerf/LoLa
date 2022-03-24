"""Extract some useful values from the results of experiment 1. There is one
TSV file per response."""

import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr

##############################################################################
# FUNCTIONS
def flatten(listOfLists):
    """Flatten a list of lists to a list"""
    return [item for l in listOfLists for item in l]

def countNonNullValues(l):
    """Return the count of non null values in a given list."""
    return sum(1 for e in l if not pd.isna(e))

def countNullValues(l):
    """Return the count of null values in a given list."""
    return sum(1 for e in l if pd.isna(e))

def filterQs(participants, q, rangeij):
    """
    Return answers to a particular question in a range of experimental items, 
    for the given participant(s), as a flattened list.

    Parameters
    ----------
    participants : List
        The participant IDs.
    q : String
        The question.
    rangeij : Range
        The experimental item range (e.g., range(11,21) = the RG questions).

    Returns
    -------
    List
        A flattened list of answers of the participant(s) to the question
        in the range of experimental items.
    """
    return flatten([DFs[p].loc[:, tuple([str(k) + q 
                                         for k in rangeij])].iloc[0].tolist() 
                        for p in participants])

def changeInLength(s1, s2):
    """Return the percentage of the length of s2 given that s1 = 100%."""
    return 100 * len(s2) / len(s1) 
        
##############################################################################
# 1. IMPORT RESULTS
participants = [1,2,3,4,5,6,8,9,10,11] #TODO change

allqs = range(1,26)
GGCqs = range(1,11)
RGqs = range(11,21)
nonfillerqs = range(1,21)
fillerqs = range(21,26)

# List of column names to use when reading the TSVs (bc there are duplicates)
columns = ["Informed consent", "Gender", "Age", "Logic experience"]
for i in range(25):
    columns += [str(i+1) + q  for q in ["Correct?", "Clear?", "Fluent?", "Post-Edit"]]
columns += ["General review", "Final comments"]

# Read the TSVs into a list of Pandas DataFrames
DFs = {}
for p in participants:
    DFs[p] = pd.read_csv("results/TSVs/1." + str(p) + " results.tsv", 
                   sep="\t", header=0, names=columns)


##############################################################################
# 2. ANALYSES
# GENDER
genders = [df.iloc[0]["Gender"] for df in DFs.values()]
print("Gender\n\tMale:", genders.count("Male"), 
      genders.count("Male") / len(genders))
print("\tFemale:", genders.count("Female"), 
      genders.count("Female") / len(genders))
print("\tPrefer not to say:", genders.count("Prefer not to say"), 
      genders.count("Prefer not to say") / len(genders))

# AGE
ages = [df.iloc[0]["Age"] for df in DFs.values()]
print("\n\nAge\n\tMean:", np.mean(ages))
print("\tSD:", np.std(ages))

# LOGIC EXPERIENCE
experiences = [df.iloc[0]["Logic experience"] for df in DFs.values()]
print("\n\nLogic experience\n\tMean:", np.mean(experiences))
print("\tSD:", np.std(experiences))

# FILLER CORRECTNESS
fillers = filterQs(participants, "Correct?", fillerqs)
print("\n\nFiller correctness\n\tYes:", fillers.count("Yes"), 
      fillers.count("Yes") / len(fillers))
print("\tNo:", fillers.count("No"), 
      fillers.count("No") / len(fillers))

#Find participants that spotted less than 3 fillers
print("Participants who spotted less than 3 fillers:")        
for p, df in DFs.items():
    fillers = df.loc[:, tuple([str(k) + "Correct?" 
                                          for k in fillerqs])].iloc[0].tolist()
    if fillers.count("No") < 3:
        print("\tParticipant", p)
print("Participants who spotted less than 2 fillers:")        
for p, df in DFs.items():
    fillers = df.loc[:, tuple([str(k) + "Correct?" 
                                          for k in fillerqs])].iloc[0].tolist()
    if fillers.count("No") < 2:
        print("\tParticipant", p)

print("\n\n\nFor the normal (non-filler) items:")
# CORRECTNESS
correct = filterQs(participants, "Correct?", nonfillerqs)
GGCcorrect = filterQs(participants, "Correct?", GGCqs)
RGcorrect = filterQs(participants, "Correct?", RGqs)

print("Correctness\n\tOverall\n\t\tYes:", 
      correct.count("Yes"), correct.count("Yes") / len(correct))
print("\t\tNo:", correct.count("No"), 
      correct.count("No") / len(correct))
print("\tFor GGC formulas:\n\t\tYes:", 
      GGCcorrect.count("Yes"), GGCcorrect.count("Yes") / len(GGCcorrect))
print("\t\tNo:", GGCcorrect.count("No"), 
      GGCcorrect.count("No") / len(GGCcorrect))
print("\tFor RG formulas:\n\t\tYes:", 
      RGcorrect.count("Yes"), RGcorrect.count("Yes") / len(RGcorrect))
print("\t\tNo:", RGcorrect.count("No"), 
      RGcorrect.count("No") / len(RGcorrect))

# CLARITY
clear = filterQs(participants, "Clear?", nonfillerqs)
GGCclear = filterQs(participants, "Clear?", GGCqs)
RGclear = filterQs(participants, "Clear?", RGqs)

print("\n\nClarity\n\tOverall\n\t\tMean:", np.mean(clear))
print("\t\tSD:", np.std(clear))
print("\tFor GGC formulas:\n\t\tMean:", np.mean(GGCclear))
print("\t\tSD:", np.std(GGCclear))
print("\tFor RG formulas:\n\t\tMean:", np.mean(RGclear))
print("\t\tSD:", np.std(RGclear))

# FLUENCY
fluent = filterQs(participants, "Fluent?", nonfillerqs)
GGCfluent = filterQs(participants, "Fluent?", GGCqs)
RGfluent = filterQs(participants, "Fluent?", RGqs)

print("\n\nFluency\n\tOverall\n\t\tMean:", np.mean(fluent))
print("\t\tSD:", np.std(fluent))
print("\tFor GGC formulas:\n\t\tMean:", np.mean(GGCfluent))
print("\t\tSD:", np.std(GGCfluent))
print("\tFor RG formulas:\n\t\tMean:", np.mean(RGfluent))
print("\t\tSD:", np.std(RGfluent))

# POST-EDITS
edits = filterQs(participants, "Post-Edit", nonfillerqs)
GGCedits = filterQs(participants, "Post-Edit", GGCqs)
RGedits = filterQs(participants, "Post-Edit", RGqs)

print("\n\nPost-edits\n\tOverall\n\t\tEdited:", 
      countNonNullValues(edits), countNonNullValues(edits) / len(edits))
print("\t\tNot edited:", 
      countNullValues(edits), countNullValues(edits) / len(edits))
print("\tFor GGC formulas:\n\t\tEdited:", 
      countNonNullValues(GGCedits), countNonNullValues(GGCedits) / len(GGCedits))
print("\t\tNot edited:", 
      countNullValues(GGCedits), countNullValues(GGCedits) / len(GGCedits))
print("\tFor RG formulas:\n\t\tEdited:", 
      countNonNullValues(RGedits), countNonNullValues(RGedits) / len(RGedits))
print("\t\tNot edited:", 
      countNullValues(RGedits), countNullValues(RGedits) / len(RGedits))

# CORRELATION CLARITY AND FLUENCY
print("\n\nCorrelation between clarity and fluency:", pearsonr(clear, fluent))

# CORRELATION FORMULA LENGTH AND CLARITY/FLUENCY
formulas = flatten([pd.read_csv("batches/batch" + str(p) + ".csv", 
                                header=0).loc[:19, "Formula"] 
                    for p in participants])
formula_lengths = [len(f) for f in formulas]
print("Correlation between formula length and clarity:", 
      pearsonr(formula_lengths, clear))
print("Correlation between formula length and fluency:", 
      pearsonr(formula_lengths, fluent))
print("Degrees of freedom:", len(formulas) - 2) 

# CHANGE IN LENGTH BETWEEN OLD AND NEW TRANSLATIONS
translations = flatten([pd.read_csv("batches/batch" + str(p) + ".csv", 
                                header=0).loc[:19, "Translation"] 
                    for p in participants])

edited_translations = [translations[i] for i in range(len(translations))
                       if not pd.isna(edits[i])] #if the translation is edited
nonNullEdits = [e for e in edits 
         if not pd.isna(e)] #if the translation is edited

length_change = [changeInLength(t,e) 
                 for t, e in zip(edited_translations, nonNullEdits)]
print("\n\nAverage change in length between original translations and edits:\n\tMean:", 
      np.mean(length_change), "\n\tSD:", np.std(length_change))

# CLARITY AND FLUENCY OF THE TRANSLATIONS WITH AND WITHOUT VARIABLES
withVarsIndices = [t for t in range(len(translations)) if 
            any(s in translations[t] for s in [' ' + c + ' ' for c in "xyzwv"])]
withoutVarsIndices = [t for t in range(len(translations)) if not
            any(s in translations[t] for s in [' ' + c + ' ' for c in "xyzwv"])] 
withVarsClear = [clear[i] for i in withVarsIndices]
withoutVarsClear = [clear[i] for i in withoutVarsIndices]
withVarsFluent = [fluent[i] for i in withVarsIndices]
withoutVarsFluent = [fluent[i] for i in withoutVarsIndices]
withVarsCorrect = [correct[i] for i in withVarsIndices]
withoutVarsCorrect = [correct[i] for i in withoutVarsIndices]
print("\n\nThere were", len(withVarsIndices), "translations with variables and",
      len(withoutVarsIndices), "translations without variables.")
print("Average clarity of formulas with variables:\n\tMean:", 
      np.mean(withVarsClear), "\n\tSD:", np.std(withVarsClear))
print("Average clarity of formulas without variables:\n\tMean:", 
      np.mean(withoutVarsClear), "\n\tSD:", np.std(withoutVarsClear))
print("Average fluency of formulas with variables:\n\tMean:", 
      np.mean(withVarsFluent), "\n\tSD:", np.std(withVarsFluent))
print("Average fluency of formulas without variables:\n\tMean:", 
      np.mean(withoutVarsFluent), "\n\tSD:", np.std(withoutVarsFluent))

print("Correctness\n\tWith variables\n\t\tYes:", 
      withVarsCorrect.count("Yes"), withVarsCorrect.count("Yes") / len(withVarsCorrect))
print("\t\tNo:", withVarsCorrect.count("No"), 
      withVarsCorrect.count("No") / len(withVarsCorrect))
print("\tWithout variables:\n\t\tYes:", 
      withoutVarsCorrect.count("Yes"), withoutVarsCorrect.count("Yes") / len(withoutVarsCorrect))
print("\t\tNo:", GGCcorrect.count("No"), 
      withoutVarsCorrect.count("No") / len(withoutVarsCorrect))


##############################################################################
# 2. Write to CSV
for p in participants:
    batch_df = pd.read_csv("batches/batch" + str(p) + ".csv", header=0)
    
    for q in ["Correct?", "Clear?", "Fluent?", "Post-Edit"]:
        batch_df[q] = filterQs([p], q, allqs)
        
    batch_df.to_csv("results/CSVs/1." + str(p) + " results.csv", sep=',')




