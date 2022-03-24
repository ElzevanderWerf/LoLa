"""Python script to extract all predicate and function  names from 
ggc-formulas.tmp."""
import re

with(open(r'ggc-formulas.tmp', 'r')) as f:
    formulas = f.read()
f.close()

Pred1 = r'[A-Za-z]+ \( [a-z]+ \)'          # 1-place predicate pattern
Pred2 = r'[A-Za-z]+ \( [a-z]+ , [a-z]+ \)'   # 2-place predicate pattern

Pred1s = re.findall(Pred1, formulas)    # predicates with arguments
# Without arguments, and duplicates removed:
Pred1s = list(set([re.search(r'[A-Za-z]+', p).group() for p in Pred1s]))
# Pred1s: ['Dodec','Small','Student','Medium','Cube','Prime','Person','Tet',
# 'Pet','Large','Even']

Pred2s = re.findall(Pred2, formulas)    # predicates with arguments
# Without arguments, and duplicates removed:
Pred2s = list(set([re.search(r'[A-Za-z]+', p).group() for p in Pred2s]))
# Pred2s: ['Adjoins','SameCol','LeftOf','RightOf','Smaller','FrontOf',
# 'Larger','SameRow','SameShape','SameSize','BackOf']

