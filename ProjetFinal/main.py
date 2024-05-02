import numpy as np
import pandas as pd
import re
import csv 
import random

prompt = ""
treeStep = 0
print('IA > Je vais essayer de deviner à quel Framework JS vous pensez.')

while (prompt == ""):
    # Début de la boucle
    prompt = input("   > ")
    
    # Affichage de l'étape de l'arbre
    printTreeStep(treeStep)

    # Fin de la boucle
    prompt = ""

print("Merci d'avoir joué !")