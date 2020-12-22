import re


def abbreviate(words):
    acronymResult = ""
    
    
    p = re.finditer(r'[A-Z\']+', words, re.IGNORECASE)
    for x in p:
        print(x[0][0])  
        acronymResult += x[0][0].upper()
        
    return(acronymResult)
    
