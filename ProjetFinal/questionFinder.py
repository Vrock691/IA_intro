import dataset
import questions

def findRelevantQuestion(datasetAvailable, alreadyAskedQuestions, alreadyReviewedAttributes): 
    # On parcours tout les attributs disponibles
    for attribute in dataset.attributes:

        if datasetAvailable.empty:
            return {
                "id": 0,
                "message": "Votre légume est inconnu à la base de donnée (ok)",
                "attribute": "name",
                "responsesAvailables": {
                    ".*": {
                        "query": None,
                        "drop": None,
                        "eliminate": None,
                        "fatal": True,
                    },
                },
            }

        # Si un attribut n'a pas été parcouru, alors aucune question n'a été posée dessus, 
        # donc on cherche des différences dans la colonne pour départager les instances
        if attribute not in alreadyReviewedAttributes and attribute != "name": # Le nom ne compte pas

            # Valeur à comparer, la première du tableau
            valueToCompare = datasetAvailable[attribute].iloc[0]

            # On parcours la colonne
            for i in range(len(datasetAvailable[attribute])):
                if valueToCompare != datasetAvailable[attribute].iloc[i]:
                    # Un élément est différent et peux permettre de départager deux instances
                    # On trouve une question qui concerne cet élément 

                    # On cherche la question ou l'attribue matche avec celui recherché
                    def criteria(question):
                        if question["attribute"] == attribute:
                            return True
                        else:
                            return False
                    
                    # On filtre les questions
                    questionsFiltered = filter(criteria, questions.questionsAvailables)
                    foundedQuestion = {
                        "attribute": None
                    }

                    # On prend la question trouvée
                    for question in questionsFiltered:
                        foundedQuestion = question

                    # On voit si la question n'a pas déjà été induite
                    if foundedQuestion not in alreadyAskedQuestions and foundedQuestion["attribute"] == attribute:
                        return foundedQuestion # et on renvoie
                       
                # Si la condition n'est pas remplie, on passe au prochaines valeurs
            # Toute les valeurs sont les mêmes à la fin de la boucle on passe au prochain attribut

    # Si pas d'attribut restant disponible à part le nom, on renvoie la question sur un légume spécifique en partant de la première ligne
    # Dans le cas ou le dataset est vide, alors on renvoie une commande fatale pour un légume inconnu
    
    vegetable = datasetAvailable.iloc[0].name
    question = {
        "id": 0,
        "message": "Votre légume est-il le suivant : " + vegetable + " ?",
        "attribute": "name",
        "responsesAvailables": {
            "oui": {
                "query": None,
                "drop": None,
                "eliminate": None,
                "fatal": True,
            },
            "non": {
                "query": None,
                "drop": vegetable,
                "eliminate": None,
                "fatal": False,
            },
        },
    }

    return question