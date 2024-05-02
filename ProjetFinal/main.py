import numpy as np
import pandas as pd
import re
import csv 
import random
import questionFinder

# Génération du dataset
import dataset
rawDatasetPath = "ProjetFinal/rawDataset/vegetables.data"
dataset = dataset.generateDataset(rawDatasetPath)

# Début du script
prompt = ""
print('IA > Je vais essayer de deviner à quel légume vous pensez.')

alreadyAskedQuestions = []
alreadyReviewedAttributes = []

# Début de la boucle
while (prompt == ""):
    
    # Recherche de la question la plus pertinente
    question = questionFinder.findRelevantQuestion(dataset, alreadyAskedQuestions, alreadyReviewedAttributes)
    print("IA > " + "question['message']")

    # Attente de la réponse    
    prompt = input("   > ")

    # Comparaison de la réponse avec les motifs disponibles
    for regex in question["responsesAvailables"].keys():
        pattern = re.compile(regex)
        results = pattern.finditer(prompt.lower())
        positions = [result.span() for result in results]
        if (len(positions) > 0):
            alreadyAskedQuestions.append(question)
            alreadyReviewedAttributes.append(question['attribute'])
            newdataset = dataset.query()

    # Fin de la boucle
    prompt = ""

print("Merci d'avoir joué !")