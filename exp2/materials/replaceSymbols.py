"""Module for replacing GGC symbols with common FOL symbols and changing bulleting"""
        
def replace_symbols(s):
    """
    Replaces the GGC symbols in input string s with common FOL symbols
    """
    dct = {126:172,
       38:8743,
       124:8744,
       36:8594,
       64:8704,
       47:8707}
    return s.translate(dct)

def replace_bulleting(s):
    return s.replace(r'\item', r'\n\t'+chr(8226)) #TODO enter erna

def add_punctuation(s):
    s = str(s)
    s = s[0].upper() + s[1:]        # Capitalize
    s = s.replace(" ,", ",")          # Remove space before comma
    s = s + "."              # End sentence with period
    return s
    
    
