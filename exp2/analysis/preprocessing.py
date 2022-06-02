"""Preprocessing of the 3 TSVs of experimental results."""
import pandas as pd

# Read results
# TODO change file names
df1 = pd.read_csv("../results/TSVs/2.1 results - intermediate version.tsv", header=0, sep="\t")
df2 = pd.read_csv("../results/TSVs/2.2 results - intermediate version.tsv", header=0, sep="\t")
df3 = pd.read_csv("../results/TSVs/2.3 results - intermediate version.tsv", header=0, sep="\t")
df12 = pd.read_csv("../results/TSVs/2.1.2 results - intermediate version.tsv", header=0, sep="\t")
df22 = pd.read_csv("../results/TSVs/2.2.2 results - intermediate version.tsv", header=0, sep="\t")
df32 = pd.read_csv("../results/TSVs/2.3.2 results - intermediate version.tsv", header=0, sep="\t")

for df in [df1, df2, df3]:
    # Drop emtpy rows
    df.dropna(how="all", inplace=True)
    
    # Barcelona researchers did not participate in previous experiment
    df.insert(7, "Did you participate in our previous experiment in March 2022?", "No", allow_duplicates=True)

for df in [df12, df22, df32]:
    # Drop emtpy rows + remove unnecessary info
    df.dropna(how="all", inplace=True)
    df.drop("Please fill in the account number AND name of the account holder to which you would like us to send the payment of €5. If you are uncomfortable with providing this info here, you can send this info (or a payment request) to Elze (06-10362723).", axis=1, inplace=True)
    df.rename(columns={"Tijdstempel":"Timestamp"}, inplace=True)

    
df1 = pd.concat([df1, df12], axis=0)
df2 = pd.concat([df2, df22], axis=0)
df3 = pd.concat([df3, df32], axis=0)
DFs = [df1, df2, df3]

# New column names
cols = ["Timestamp", "InformedConsent", "Gender", "Age", "EnglishLevel", 
       "LogicLevel", "LogicPerspective", "ParticipatedInExp1"] + [
           "NLI-GGC" + str(i) for i in range(0,21)] + [
               "NLI-RG" + str(i) for i in range(0,21)] + [
                   "FR-GGC" + str(i) + "-" + j for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                       "FR-RG" + str(i) + "-" + j  for i in range(0,10) for j in ["T1", "T2", "T3"]] + [
                           "FinalComments"]

# Values to replace                          
qDict = {"Lower level than the ones below":int(1),
         "Level of a bachelor/master student who has followed 1 or 2 classes of logic.":int(2),
         "Level of a bachelor/master student who has followed more than 2 classes of logic.":int(3),
         "Higher level than the ones above":int(4),
         "(Most fluent) 1":int(1),
         "2":int(2),
         "3 (Least fluent)":int(3)
         }

# Hypotheses
hyps = pd.read_csv("../materials/experimental_items/nli-hypotheses123.csv", header=0)

for df in DFs:  
    # Rename columns
    df.columns = cols
    
    # Replace values with qDict
    df.replace(qDict, value=None, inplace=True)
    
    # Process NLI answers as being correct or incorrect
    nliQs = df.iloc[:,7:49].copy()
    for colName, col in nliQs.items():
        if colName.startswith("NLI-GGC"):
            i = int(colName[7:])
            correct = hyps.loc[i, "CorrectAnswer"]
            col.replace(regex={correct:"Correct", "^(.(?<!"+correct+'))*?$':"Incorrect"}, 
                        inplace=True)
        elif colName.startswith("NLI-RG"):
            i = int(colName[6:])
            correct = hyps.loc[i+21, "CorrectAnswer"]
            col.replace(regex={correct:"Correct", "^(.(?<!"+correct+'))*?$':"Incorrect"}, 
                        inplace=True)
    df.iloc[:,7:49] = nliQs.copy()
    
    # Process FR answers as integers
    for col in df.columns:
        if col.startswith("FR"):
            df[col] = df[col].astype(int)

# Write to CSVs
# TODO change file names
df1.to_csv("../results/CSVs/2.1 results - intermediate version.csv")
df2.to_csv("../results/CSVs/2.2 results - intermediate version.csv")
df3.to_csv("../results/CSVs/2.3 results - intermediate version.csv")