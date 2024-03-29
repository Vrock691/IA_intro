# Fonction de calculs
def Sum(): 
    n1 = int(input("Entrez le premier nombre : "))
    n2 = int(input("Entrez le deuxième nombre : "))
    return n1 + n2

def Divide(n1, n2):
    if n1 and n2!=0:
        return n1/n2
    else:
        return "Division par 0 impossible !"


