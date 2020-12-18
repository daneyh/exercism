def abbreviate(words):
    acronymResult = ""
    for x in words.split(" ","-","_"):
        if x.isalpha():
            acronymResult += x[0].upper()

    return(acronymResult)
    
