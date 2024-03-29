import re

def findRule(prompt, rules):
    """
    Cette fonction fouilles dans la liste de régles et va vérifier si 
    un motif est trouvé dans une chaine de caractères
    """
    
    selectedRule = rules[0]

    # On parcours la liste de régles disponibles
    for rule in rules:
        # On compile le motif de la régle parcouru
        pattern = re.compile(rule["rule"])

        # On cherche le motif dans la chaine
        results = pattern.finditer(prompt)

        # On synthétises en liste les motifs trouvés
        positions = [result.span() for result in results]

        if (len(positions) > 0):
            # Si un résultat ou plus est trouvé dans le prompt 
            # on l'enregistre en tant que réponse selectionné
            # On vérifie que la réponse précédemment enregistré n'a
            # pas un score plus important, auxquel cas, on l'abandonne
            if rule['score'] >= selectedRule['score']:
                selectedRule = rule
    
    # On retourne la régle selectionnée
    return selectedRule
