#!/usr/bin/env python

# A word is autological if it describes itself.
# e.g. pentasyllabic, awkwardnessful.
# otherwise we call a word heterological

def autological(x):
    if x is autological:
        return True
    return x(x)

def heterological(x):
    return not autological(x)

# Now, what happens here?

# print autological(autological)
print heterological(heterological)
