"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    single_list = []

    for i in range(len(items)):
        if type(items[i]) != "str":
            items[i] = str(items[i])

    for i in range(len(items)):
        if not(items[i] in single_list):
            single_list.append(items[i])
            frequencies[str(items[i])] = 1
        else:
            frequencies[str(items[i])] +=1
    return frequencies
