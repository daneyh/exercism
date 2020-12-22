import re
def count_words(sentence):
    
    dictionary = {}
    p = re.finditer(r'[A-Z0-9]+(\'[A-Z0-9])?', sentence, re.IGNORECASE)
    for x in p:
        dictionary[x[0].lower()] = dictionary.get(x[0].lower(),0) + 1

            
    return dictionary


