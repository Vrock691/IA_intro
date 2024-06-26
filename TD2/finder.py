import re
import ruleset

def findRule(prompt):
    """
    Cette fonction fouilles dans la liste de régles et va vérifier si 
    un motif est trouvé dans une chaine de caractères
    """

    # On importe les règles
    rules = ruleset.rules
    
    # On selectionne la régle je ne sais pas par défaut
    selectedRule = rules[0]

    # On parcours la liste de règles disponibles
    for rule in rules:
        # On compile le motif de la règle parcouru
        pattern = re.compile(rule["rule"])

        # On cherche le motif dans la chaine
        results = pattern.finditer(prompt.lower())

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
