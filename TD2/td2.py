import pandas as pd
import re
import finder
import externalfunctions

# On définis les variables globales au programme
userinput = ""
fatal = False

# Démarrage de la boucle 
while not fatal:
    # On demande le prompt de l'utilisateur
    userinput = input("> ")

    # On cherche un motif à partir de la liste de règles
    rule = finder.findRule(userinput)

    # On envoie la réponse de la règle selectionnée
    print("> " + rule['response'])

    # On execute la fonction liée a la règle si elle existe
    if (rule['function'] != None):
        print(rule['function'](userinput))
    
    # On termine le programme si la commande est fatale
    if (rule['fatal']):
        fatal = True