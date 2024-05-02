import numpy as np
import pandas as pd
import re
import csv 
import random

# Génération du dataset
import dataset
rawDatasetPath = "ProjetFinal/rawDataset/vegetables.data"
dataset = dataset.generateDataset(rawDatasetPath)

# Début du script
prompt = ""
treeStep = 0
print('IA > Je vais essayer de deviner à quel légume vous pensez.')

while (prompt == ""):
    # Début de la boucle
    prompt = input("   > ")
    
    # Affichage de l'étape de l'arbre
    

    # Fin de la boucle
    prompt = ""

print("Merci d'avoir joué !")