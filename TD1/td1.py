import pandas as pd
import csv
import re

document = open("TD1/elysee.csv")
lines = document.readlines()

short_content = []
full_content = []
author = []
date = []
affiliations = []

for line in lines :
    data = line.split('\t')
    short_content.append(data[1])
    full_content.append(data[2])
    author.append(data[3])
    date.append(data[4])
    affiliations.append(data[5])

short_content.pop(0)
full_content.pop(0)
author.pop(0)
date.pop(0)
affiliations.pop(0)
DataFrame = {
    "short_content": short_content,
    "full_content": full_content,
    "author": author,
    "date": date,
    "affiliations": affiliations
}

# print(pd.value_counts(DataFrame["date"]))

pattern = re.compile("2020")
results = []

indice = 0
for item in DataFrame['date']: 
    for iter in pattern.finditer(item) :
        results.append(indice)
        iter.start
    indice += 1

def trouveMotif(pattern, content):
    p = re.compile(pattern)
    results = []

    indice = 0
    for item in content: 
        for iter in p.finditer(item) :
            if indice not in results:
                results.append(indice)
        indice += 1

    return results

"""
print("Pour le pattern 2020")
print(trouveMotif("2020", DataFrame['full_content']))

print("Pour le pattern Monsieur")
print(trouveMotif("Monsieur", DataFrame['full_content']))

print("Pour le pattern Monsieur ou monsieur")
print(trouveMotif("Monsieur|monsieur", DataFrame['full_content']))

print("Pour le pattern 4")
print(trouveMotif("[0-9]+", DataFrame['full_content']))

print("Pour le pattern 5")
print(trouveMotif("[0-9]+\s[0-9]+", DataFrame['full_content']))

print("Pour le pattern 6")
print(trouveMotif("[0-9]+\s[0-9]+\seuros", DataFrame['full_content']))
"""

def trouveMotifAvecAffichage(pattern, content):
    p = re.compile(pattern)
    results = []

    indice = 0
    for item in content: 
        for iter in p.finditer(item) :
            print(iter)
        indice += 1

    return results

print(trouveMotifAvecAffichage("2020", DataFrame['full_content']))