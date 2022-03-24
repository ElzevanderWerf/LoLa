import pandas as pd
import random
r = random.SystemRandom()

#Randomly take 1000 rows of GGC formulas with translations
ggc_df = pd.read_csv("out/ggc-formulas-to-eng.csv", 
                     header=0, 
                     error_bad_lines=False)

subset = r.sample(range(len(ggc_df)), 1000)
subset_df = ggc_df.loc[subset, :]

csv = subset_df.to_csv(r'exp1/exp1-ggc-to-eng.csv', sep=',')

