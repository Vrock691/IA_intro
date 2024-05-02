import pandas as pd

def generateDataset(rawDatasetPath):
    '''
    definition: Cette fonction converti le fichier .data en table pandas
    input: Le chemin d'accès au fichier .data
    output: Table panda
    '''

    # Création des variables nécéssaire à la création de la table
    attributes = ["name","green","root","flower","fruit",
                  "leaf","seed","aromatic","tuber",
                  "bulb","stems","white","orange","season"]
    parsedInstancesName = []
    parsedValues = []
    
    # Ouverture du fichier data
    rawData = open(rawDatasetPath, "r")
    lines = rawData.readlines()

    # On obtient les instances pour chaque ligne
    for line in lines:
        # On obtient les valeurs de l'instance parcouru
        values = line.split(',')

        # Ajout des données dans les variables de création
        data = {}
        for i in range(len(attributes)):
            label = attributes[i]
            if label == "name":
                parsedInstancesName.append(values[i])
            else :
                data[label] = int(values[i])
        parsedValues.append(data)

    # Création et renvoie du dataset sous forme de tableau panda
    dataset = pd.DataFrame(parsedValues, index=parsedInstancesName)
    print(dataset)
    return dataset