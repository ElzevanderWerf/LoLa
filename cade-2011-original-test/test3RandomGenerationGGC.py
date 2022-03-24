"""Python script to create a list of randomly generated FOL formulas in
GGC notation, for a given test lexicon."""

import string
import random
r = random.SystemRandom()

class Lexicon:
    def __init__(self, Pred1s, Pred2s, Kinds):
        self.Pred1s = Pred1s    # 1-place predicates
        self.Pred2s = Pred2s    # 2-place predicates
        self.Kinds = Kinds      # kind predicates

class RandomGenerator:
    def __init__(self, lexicon, maxdepth):
        self.lex = lexicon
        self.variables = ["x", "y", "z", "w", "v"]
        self.new_var_i = 0      # integer for a new variable
        self.new_cons_i = 0     # index for a new constant
        self.maxdepth = maxdepth       # maximum depth of a generated proposition

    def makeProp(self, n, bindsVars=set()):
        """
        Randomly generate a proposition from the lexicon,
        with depth n. bindsVars is a set of variable integers that are bound 
        by the proposition (used for avoiding generation of free variables).
        In the case of conjunction, disjunction and implication, an extra 
        check is done such that the final prop does not include outer brackets, 
        because then it will not be parsable by the GF shell.
        """
        if n == 0:          # termination signal: atomic proposition
            return self.makeAtom(n-1, bindsVars)
        else: 
            i = r.choice(range(7))
            if i == 0:      # atomic proposition
                return self.makeAtom(n-1, bindsVars)
            
            elif i == 1:    # negation
                return "~ " + self.makeProp(n-1, bindsVars)
            
            elif i == 2:    # conjunction
                if n == self.maxdepth:      # exclude outer brackets
                    return self.makeProp(n-1, bindsVars) + " & " + self.makeProp(n-1, bindsVars)
                else:                       # include outer brackets
                    return "( " + self.makeProp(n-1, bindsVars) + " & " + self.makeProp(n-1, bindsVars) + " )"
            
            elif i == 3:    # disjunction
                if n == self.maxdepth:      # exclude outer brackets
                    return self.makeProp(n-1, bindsVars) + " | " + self.makeProp(n-1, bindsVars)
                else:                       # include outer brackets
                    return "( " + self.makeProp(n-1, bindsVars) + " | " + self.makeProp(n-1, bindsVars) + " )"
            
            elif i == 4:    # implication
                if n == self.maxdepth:      # exclude outer brackets
                    return self.makeProp(n-1, bindsVars) + " $ " + self.makeProp(n-1, bindsVars)
                else:                       # include outer brackets
                    return "( " + self.makeProp(n-1, bindsVars) + " $ " + self.makeProp(n-1, bindsVars) + " )"
            
            elif i == 5:    # universal quantification
                var, j = self.makeVar(afterQ=True)
                return "@ " + var + " " + self.makeProp(n-1, bindsVars.union([j]))
            
            elif i == 6:    # existential quantification
                var, j = self.makeVar(afterQ=True)
                return "/ " + var + " " + self.makeProp(n-1, bindsVars.union([j]))
    
    def makeAtom(self, n, bound=set()):
        """
        Randomly generate an atomic proposition from the lexicon,
        with maximum depth n. bound is a set of variable integers that are 
        bound by the proposition (used for avoiding generation of free 
        variables).
        """
        i = r.choice(range(3))
        if i == 0:      # 1-place predicate
            return r.choice(self.lex.Pred1s) + " ( " + self.makeTerm(n-1, bound) + " )"
        elif i == 1:    # 2-place predicate
            return r.choice(self.lex.Pred2s) + " ( " + self.makeTerm(n-1, bound) + " , " + self.makeTerm(n-1, bound) + " )"
        elif i == 2:    # kind predicate
            return r.choice(self.lex.Kinds) + " ( " + self.makeTerm(n-1, bound) + " )"
        
    def makeTerm(self, n, bound=set()):
        """
        Randomly generate a term from the lexicon, with maximum depth n.
        bound is a set of variable integers that are bound by the proposition 
        (used for avoiding generation of free variables).
        """
        if not bound: #if no variables can be bound
            return self.makeCons()
        else:    
            i = r.choice(range(2))
            if i == 0:      # variable
                return self.makeVar(bound)
            elif i == 1:    # constant
                return self.makeCons()
        
    def makeVar(self, bound=set(), afterQ=False):
        """
        Generate a variable (new or already used) in the lexicon. If the
        variable comes directly after a quantifier (afterQ == True), then
        pick a new or already used variable. Otherwise, pick from the list 
        bound (integers of the variables that can be bound in the proposition).
        """
        if afterQ:
            i = r.randint(0, self.new_var_i)
            if i == self.new_var_i:
                self.new_var_i += 1
            return (self.variables[i], i)
        else:
            i = r.choice(list(bound))
            return self.variables[i]
            
    def makeCons(self):
        """
        Generate a constant (new or already used) in the lexicon.
        """
        i = r.randint(0, self.new_cons_i)
        if i == self.new_cons_i:
            self.new_cons_i += 1
        return string.ascii_lowercase[i]
    
#TEST 3 GGC
ggcLexicon = Lexicon(["Small", "Medium", "Large", "Even"],      #Pred1s
                        ["Adjoins", "SameCol", "LeftOf", "RightOf", "Smaller", 
                         "FrontOf", "Larger", "SameRow", "SameShape", 
                         "SameSize", "BackOf"],                 #Pred2s
                        ["Dodec", "Student", "Cube", "Prime", "Person", 
                         "Tet", "Pet"])                 #Kinds

# # Test to generate 1 proposition        
# rg = RandomGenerator(ggcLexicon, 3)  
# random_formula = rg.makeProp(3)
# print(random_formula)


# Randomly generate 1000 formulas with a certain maximum depth
depth = 3       # maximum depth
formulas = []
rg = RandomGenerator(ggcLexicon, depth)

while len(formulas) < 1000:
    prop = rg.makeProp(depth, set())
    if len(prop) >= 20 and len(prop) <= 100:
        formulas.append(prop)
    rg.new_var_i = 0    #set again to 0 for generating a new prop
    rg.new_cons_i = 0   #set again to 0 for generating a new prop

# Write formulas to file with newlines
with(open(r'out/test3GGC.tmp', 'w')) as f:
    f.write('\n'.join(formulas))
f.close()

# DISCUSSION generation of new variables and constants is now pseudorandom (there is a
#   random choice between the list of currently chosen variables and 
#   a new one in the list of integers)


        
        
