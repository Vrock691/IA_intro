import re
import questionFinder

# Génération du dataset
import dataset
RAWDATASETPATH = "ProjetFinal/rawDataset/vegetables.data"
dataset = dataset.generateDataset(RAWDATASETPATH)

# Début du script
PROMPT = ""
print('IA > Je vais essayer de deviner à quel légume vous pensez.')

alreadyAskedQuestions = []
alreadyReviewedAttributes = []

# Début de la boucle
while PROMPT != None:    
    # Recherche de la question la plus pertinente
    question = questionFinder.findRelevantQuestion(dataset, alreadyAskedQuestions, alreadyReviewedAttributes)
    print("IA > " + question['message'])

    # Attente de la réponse
    PROMPT = input("   > ")

    # Comparaison de la réponse avec les motifs disponibles
    for regex in question["responsesAvailables"].keys():

        # Établissement d'un motif regex
        pattern = re.compile(regex)
        results = pattern.finditer(str(PROMPT).lower())

        # Découverte des résultats en tant que liste
        positions = [result.span() for result in results]

        # Si des occurences sont trouvés, on affiche la fonction correspondante
        if len(positions) > 0:

            # On enregistre la question comme étant posée
            alreadyAskedQuestions.append(question)
            alreadyReviewedAttributes.append(question['attribute'])
            if question["responsesAvailables"][regex]["eliminate"] is not None:
                alreadyReviewedAttributes.extend(list(question["responsesAvailables"][regex]["eliminate"])) # On élimine les autres questions liés

            # Si une action de tri query est requise, on l'effectue
            if question["responsesAvailables"][regex]["query"] is not None:
                newdataset = dataset.query(question["responsesAvailables"][regex]["query"])
                dataset = newdataset

            # Si une action de suppression est requise, on l'effectue
            if question["responsesAvailables"][regex]["drop"] is not None:
                newdataset = dataset.drop(index=question["responsesAvailables"][regex]["drop"])
                dataset = newdataset

            # Fin de la boucle
            if question["responsesAvailables"][regex]['fatal'] is True:
                PROMPT = None

print("Merci d'avoir joué !")