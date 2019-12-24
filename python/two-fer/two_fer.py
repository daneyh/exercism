def two_fer(name=None):
    if not name:
        return "One for you, one for me."
    else:
        return "One for %s, one for me." % (name)
    raise Exception("Problem in two_fer function")