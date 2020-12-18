def is_isogram(string):
    isogram = True
    for x in string.replace(' ','').replace('-','').upper():
        occurance = string.upper().count(x)
        if occurance > 1:
            isogram = False
    return isogram
