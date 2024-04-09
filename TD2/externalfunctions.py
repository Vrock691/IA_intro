import re

# Fonction de calculs
def Sum(prompt): 
    matches = re.findall('([0-9]+)', prompt)
    if len(matches) >= 2:
        n1 = int(matches[0])
        n2 = int(matches[1])
        sum = n1+n2
        return "> " + str(n1) + " + " + str(n2) + " = " + str(sum)
    else:
        return "Il me semble qu'il manque un nombre pour faire cet addition"
    
def Divide(prompt):
    matches = re.findall('([0-9]+)', prompt)
    if len(matches) >= 2:
        n1 = int(matches[0])
        n2 = int(matches[1])
        if n1 and n2!=0:
            return n1/n2
        else:
            return "Division par 0 impossible !"
    else:
        return "Division impossible, chiffre manquant"

def Multiplication(prompt):
    matches = re.findall('([0-9]+)', prompt)
    if len(matches) >= 2:
        n1 = int(matches[0])
        n2 = int(matches[1])
        prod = n1*n2
        return "> " + str(n1) + " x " + str(n2) + " = " + str(prod)
    else:
        return "Il me semble qu'il manque un nombre pour faire cette multiplication"

def Soustraction(prompt):
    matches = re.findall('([0-9]+)', prompt)
    if len(matches) >= 2:
        n1 = int(matches[0])
        n2 = int(matches[1])
        dif = n1-n2
        return "> " + str(n1) + " - " + str(n2) + " = " + str(dif)
    else:
        return "Il me semble qu'il manque un nombre pour faire cet addition"

def RecordNewResponse(prompt):
    return "Enregistré"