import dataset
import questions

def findRelevantQuestion(datasetAvailable, alreadyAskedQuestions, alreadyReviewedAttributes): 
    # On parcours tout les attributs disponibles
    for attribute in dataset.attributes:

        # Si un attribut n'a pas été parcouru, alors aucune question n'a été posée dessus, 
        # donc on cherche des différences dans la colonne pour départager les instances
        if attribute not in alreadyReviewedAttributes and attribute != "name": # Le nom ne compte pas

            # Valeur à comparer, la première du tableau
            valueToCompare = datasetAvailable[attribute][0]

            # On parcours la colonne
            for i in range(len(datasetAvailable[attribute])):
                if valueToCompare != datasetAvailable[attribute][i]:
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

                    # On prend la question trouvée
                    foundedQuestion = questionsFiltered[1]

                    # On voit si la question n'a pas déjà été induite
                    if foundedQuestion not in alreadyAskedQuestions:
                        return foundedQuestion # et on renvoie
                       
                # Si la condition n'est pas remplie, on passe au prochaines valeurs
            # Toute les valeurs sont les mêmes à la fin de la boucle on passe au prochain attribut

    # Si pas d'attribut restant disponible à part le nom, on renvoie la question sur un légume spécifique en partant de la première ligne
    vegetable = datasetAvailable[0]
    question = {
        "id": None,
        "message": "Votre légume est-il le suivant : " + vegetable + " ?",
        "attribute": "name",
        "responsesAvailables": {
            "oui": {
                "query": "",
                "eliminate": None,
                "fatal": True,
            },
            "non": {
                "query": 0,
                "eliminate": None,
                "fatal": False,
            },
        },
    }

    return 1