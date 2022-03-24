"""Python script to create a list of randomly generated FOL formulas in
Latex notation, for a given test lexicon."""

import random
r = random.SystemRandom()

class Lexicon:
    def __init__(self, Pred1s, Pred2s, Fun1s, Fun2s, Kinds):
        self.Pred1s = Pred1s    # 1-place predicates
        self.Pred2s = Pred2s    # 2-place predicates
        self.Fun1s = Fun1s      # unary functions
        self.Fun2s = Fun2s      # binary functions
        self.Kinds = Kinds      # kind predicates

class RandomGenerator:
    def __init__(self, lexicon):
        self.lex = lexicon
        self.new_var_i = 0      # integer for a new variable
        self.maxdepth = 0       # maximum depth of a generated proposition

    def makeProp(self, n):
        """
        Randomly generate a proposition from the lexicon,
        with maximum depth n. In the case of conjunction, disjunction and
        implication, an extra check is done such that the final prop does
        not include outer brackets, because then it will not be parsable
        by the GF shell.
        """
        if n == 0:          # termination signal
            return self.makeAtom(n-1)
        else: 
            i = r.choice(range(7))
            if i == 0:      # atomic proposition
                return self.makeAtom(n-1)
            elif i == 1:    # negation
                return "\\sim " + self.makeProp(n-1)
            elif i == 2:    # conjunction
                if n == self.maxdepth:  # exclude outer brackets
                    return self.makeProp(n-1) + " \\& " + self.makeProp(n-1)
                else:
                    return "( " + self.makeProp(n-1) + " \\& " + self.makeProp(n-1) + " )"
            elif i == 3:    # disjunction
                if n == self.maxdepth:  # exclude outer brackets
                    return self.makeProp(n-1) + " \\vee " + self.makeProp(n-1)
                else: 
                    return "( " + self.makeProp(n-1) + " \\vee " + self.makeProp(n-1) + " )"
            elif i == 4:    # implication
                if n == self.maxdepth:  # exclude outer brackets
                    return self.makeProp(n-1) + " \\supset " + self.makeProp(n-1)
                else:
                    return "( " + self.makeProp(n-1) + " \\supset " + self.makeProp(n-1) + " )"
            elif i == 5:    # universal quantification
                return "( \\forall " + self.makeVar() + " ) " + self.makeProp(n-1)
            elif i == 6:    # existential quantification
                return "( \\exists " + self.makeVar() + " ) " + self.makeProp(n-1)
    
    def makeAtom(self, n):
        """
        Randomly generate an atomic proposition from the lexicon,
        with maximum depth n.
        """
        i = r.choice(range(3))
        if i == 0:      # 1-place predicate
            return self.toLatex(r.choice(self.lex.Pred1s)) + " { " + self.makeTerm(n-1) + " }"
        elif i == 1:    # 2-place predicate
            return self.toLatex(r.choice(self.lex.Pred2s)) + " { " + self.makeTerm(n-1) + " } { " + self.makeTerm(n-1) + " }"
        elif i == 2:    # kind predicate
            return self.makeTerm(n-1) + " \\in " + r.choice(self.lex.Kinds)
        
    def makeTerm(self, n):
        """
        Randomly generate a term from the lexicon, with maximum depth n.
        """
        if n == 0:          # termination signal
            return self.makeVar()
        else:
            i = r.choice(range(3))
            if i == 0:      # variable
                return self.makeVar()
            elif i == 1:    # constant
                return self.makeCons()
            elif i == 2:    # function
                return self.makeFun(n-1)
        
    def makeVar(self):
        """
        Generate a variable (new or already used) in the lexicon.
        """
        i = r.randint(0, self.new_var_i)
        if i == self.new_var_i:
            self.new_var_i += 1
        return "x" + str(i+1)
        
    def makeCons(self):
        """
        Generate a new constant in the lexicon.
        """
        return str(r.randint(1, 10)) #or maybe randomly choose from a list of constants in the lexicon?
    
    def makeFun(self, n):
        """
        Randomly generate a function term from the lexicon, with maximum depth n.
        """
        if n == 0:          # termination signal
            return self.toLatex(r.choice(self.lex.Fun1s)) + " { " + self.makeVar() + " }"
        else:
            i = r.choice(range(2))
            if i == 0:      # unary function
                return self.toLatex(r.choice(self.lex.Fun1s)) + " { " + self.makeTerm(n-1) + " }"
            elif i == 1:    # binary function
                return self.toLatex(r.choice(self.lex.Fun2s)) + " { " + self.makeTerm(n-1) + " } { " + self.makeTerm(n-1) + " }"
    
    def toLatex(self,s):
        """
        Turn a function or predicate name into Latex notation, e.g.:
            "Even" --> "\\even"
        """
        return "\\" + s.lower()        
    
#TEST 3 Latex
arithmLexicon = Lexicon(["Even", "Odd"],    #Pred1s
                        ["Equal"],          #Pred2s
                        ["Square"],         #Fun1s
                        ["Sum", "Product"], #Fun2s
                        ["N"])              #Kinds
        
# rg = RandomGenerator(arithmLexicon)  
# rg.maxdepth = 3
# random_formula = rg.makeProp(3)
# print(random_formula)


# Randomly generate 50 formulas with a certain maximum depth
depth = 3
formulas = []
rg = RandomGenerator(arithmLexicon)
rg.maxdepth = depth

while len(formulas) < 50:
    prop = rg.makeProp(depth)
    if len(prop) <= 100:
        formulas.append(prop)
    rg.new_var_i = 0    #set again to 0 for generating a new prop


# Write formulas to file with newlines
with(open(r'out/test3Latex.tmp', 'w')) as f:
    f.write('\n'.join(formulas))
f.close()


# TODO generation of new variables and constants is now pseudorandom (there is a
#   random choice between the list of currently chosen variables and 
#   a new one in the list of integers)


        
        
