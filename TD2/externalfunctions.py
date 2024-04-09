import re

# Fonction de calculs
def Sum(prompt): 
    matches = re.search('[0-9].', prompt)
    print(matches.group(0))
    n1 = matches[0]
    n2 = matches[1]
    return "> " + (n1 + n2) + ""
    
def Divide(prompt):
    if n1 and n2!=0:
        return n1/n2
    else:
        return "Division par 0 impossible !"

def Multiplication(prompt):
    n1 = int(input("Entrez le premier nombre : "))
    n2 = int(input("Entrez le deuxième nombre : "))
    return n1 * n2

def Soustraction(prompt):
    n1 = int(input("Entrez le premier nombre : "))
    n2 = int(input("Entrez le deuxième nombre : "))
    return n1 - n2

def RecordNewResponse(prompt):
    return "Enregistré"