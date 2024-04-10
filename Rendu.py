import pandas as pd
import re



# On définis les variables globales au programme
userName = ""
userinput = ""
fatal = False



# On définie la fonction de reconnaissance de régles
def findRule(prompt):
    """
    Cette fonction fouilles dans la liste de régles et va vérifier si 
    un motif est trouvé dans une chaine de caractères
    """

    # On importe les règles
    rules = ruleset
    
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



# Fonction de calculs dans les règles
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



# la liste des règles
ruleset = [
    # Règle par défaut quand le bot ne connais pas de réponse paramétrée
    { 
        "id": "Je sais pas",
        "rule": ".*",
        "response": "Désolé %NAME%, je n'ai pas compris votre demande.",
        "score": 0,
        "fatal": False,
        "function":None,
    },
    # Autres règles
    {
        "id": "Bonjour",
        "rule": "bonjour",
        "response": "Bonjour %NAME%, je suis votre spécialiste en burger, en quoi puis-je vous aider ?",
        "score": 1,
        "fatal": False,
        "function": None,
    }, 
    {
        "id": "Aurevoir",
        "rule": "(au revoir)|(aurevoir)",
        "response": "Ravi d'avoir pu vous aider %NAME%",
        "score": 1,
        "fatal": True,
        "function": None,
    }, 
    {
        "id": "Salut",
        "rule": "(salut|hello)",
        "response": "Salut, comment va tu ? Une question sur les burgers ?",
        "score": 1,
        "fatal": False,
        "function": None,
    }, 
    {
        "id":"apropos",
        "rule":"(?:(qu'est ce qu'|c'est quoi |qu'est ce que c'est |Qu'est ce que c'est qu')un (burger|hamburger).*)|(?:.*(ou|où) vient le (burger|hamburger).*)",
        "response":"Un hamburger, ou par aphérèse burger, est un sandwich d'origine allemande, composé de deux pains de forme ronde1 (bun) généralement garnis d'une galette de steak haché (généralement du bœuf) et de crudités, salade, tomate, oignon, cornichon (pickles) ainsi que de sauce. D'autres question à ce propos ?",
        "score":4,
        "fatal":False,
        "function":None,
        
    },
    {
        "id":"date",
        "rule":".*(donne moi)|(quelle est) l'année (d'apparition|d'invention)|(de quand date)|(date (d'invention|de création|d'apparition))|(du|le) (burger|hamburger).*",
        "response":"Le burger est inventé en 1758 en Allemagne à Hambourg. N'hésitez pas à me poser des questions sur l'hétymologie du mot hamburger.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"ethymo",
        "rule":".*étymologie (du mot|de) (burger|hamburger).*",
        "response":"Hamburger fait référence à la ville de Hambourg, en Allemagne. Il n'existe aucun rapport étymologique entre le hamburger et le jambon (en anglais : ham), puisque le nom de la ville de Hambourg a une étymologie différente. Une question sur la date d'invention du burger ?",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"découverte",
        "rule":".*(donne moi un (exemple de|)|est le) (burger|hamburger) (le plus |)connu.*",
        "response":"Le burger le plus connu est certainement le Big Mac, de la chaine de restauration rapide McDonald's. Mais je peux vous trouver un burger plus original si vous me le demandez.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"original",
        "rule":".*(donne moi un (exemple de|)|est le) (burger|hamburger) (le plus |)(original|spécial|innatendu).*",
        "response":"Bien sûr !  L’Atomic Fallout, l’emblématique burger servi à l’Atomic Burger de Bristol, est tellement pimenté que les clients doivent signer une exonération de responsabilité, porter des gants de protection, ou encore prouver qu’ils ont plus de 18 ans et sont sobres avant de se mettre à table. Mais il est loin d'être le plus gros burger du monde...",
        "score":1,
        "fatal":False,
        "function":None, 
    }, 
    {
        "id":"biggest",
        "rule":".*(donne moi un (exemple de|)|est le) (burger|hamburger) (le plus |)(grand|gros|énorme).*",
        "response":"C'est le Black Bear Casino Resort de Carlton dans le Minnesota aux Etats-Unis. Le double bacon cheeseburger comprend 27 kg de bacon, 22 kg de laitue et de 18 kg de fromage et cornichons pour un total de 913 kilos et près de quatre millions de calories.",
        "score":1,
        "fatal":False,
        "function":None, 
    }, 
    {
        "id":"where",
        "rule":".*quel est le (premier|tout premier)|(restaurant|resto|lieu|lieux) à (servir|préparer|cuisiner|proposer) (des|un|le|les) (hamburger|burger|hamburgers|burgers).*",
        "response":"En 1904, Fletcher Davis originaire d’Athens au Texas, vend des sandwichs au steak de Hambourg à la foire de Saint-Louis. C’est un véritable succès qui semble marquer la vraie naissance du hamburger actuel. C'était le premier lieu à servir des hamburger comme on l'entend aujourd'hui.",
        "score":2,
        "fatal":False,
        "function":None, 
    }, 
    {
        "id":"firstmcdo",
        "rule":".*(quand|quelle est la date)|(ouvre|a ouvert|d'ouverture)|(le|du)|(tout premier|premier)|(mcdo|mc'do|mcdonald|mcdonalds|mcdonald's).*",
        "response":"Le premier McDonald's ouvre en 1955 dans la banlieue de Chicago, Illinois.",
        "score":1,
        "fatal":False,
        "function":None, 
    }, 
    {
        "id":"sum",
        "rule":"(?:fait|additionne) ([0-9]*) (?:plus|et|par) ([0-9]*).*",
        "response":"Bien j'additionne ces deux nombres",
        "score":1,
        "fatal":False,
        "function":Sum, 
    }, 
    {
        "id":"moins",
        "rule":"(?:fait|soustrait) ([0-9]*) (?:moins|et|par) ([0-9]*).*",
        "response":"Bien je soustrait ces deux nombres",
        "score":1,
        "fatal":False,
        "function":Soustraction, 
    }, 
    {
        "id":"multi",
        "rule":"(?:fait|multiplie) ([0-9]*) (?:x|fois|et|par) ([0-9]*).*",
        "response":"Bien je multiplie ces deux nombres",
        "score":1,
        "fatal":False,
        "function":Multiplication, 
    }, 
    {
        "id":"quotient",
        "rule":"(?:fait|divise) ([0-9]*) (?:/|divisé par|et|par) ([0-9]*).*",
        "response":"Bien je divise ces deux nombres",
        "score":1,
        "fatal":False,
        "function":Divide, 
    }, 
    {
        "id":"consommation",
        "rule":".*(quelle est|donne moi) la consommation de (burgers|burger|hamburgers|hamburger) annuelle (des américains|aux états-unis|en amérique).*",
        "response":"Les Américains consomment en moyenne 50 milliards de burgers par an.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"ventes",
        "rule":".*(quel est|combien|donne moi) (le montant des ventes|les recettes|de dollars|ont rapporté) la vente de (burgers|burger|hamburgers|hamburgers) (aux états-unis|en amérique).*",
        "response":"Les ventes de burgers aux États-Unis ont atteint plus de 100 milliards de dollars.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"journée",
        "rule":".*(quelle est|donne moi) la date de la journée nationale du (burger|hamburger).*",
        "response":"Le 28 mai est la journée nationale du burger aux états-Unis.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"record",
        "rule":".*(quel est|donne moi) le record du plus grand nombre de (burgers|hamburgers|burger|hamburger) (mangés|avalés) en (quelques minutes|très peu de temps|peu de temps).*",
        "response":"Le record de consommation de burgers est de 26 hamburgers en 10 minutes, établi lors du concours annuel de l'Association des mangeurs de hot-dogs.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"garniture",
        "rule":".*(quel est|de quel type) (la garniture|d'aliments) (des|les) (burgers|burgers|hamburgers|hamburgers) (sont t'il remplis|remplis|garnis|constitués).*",
        "response":"Les burgers peuvent être garnis de divers ingrédients tels que des œufs, du bacon, des avocats, des oignons, des champignons, et bien d'autres encore.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"cuisson",
        "rule":".*quelles sont les (différentes façons|différentes manières|méthodes|façons|manières) (de|pour) (cuire|cuisson) des (burgers|burger|hamburger|hamburgers).*",
        "response":"Les burgers peuvent être cuits de différentes manières, notamment grillés, saisis, frits ou cuits au barbecue.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"japon",
        "rule":".*donne moi (un|une) (exemple|variation) de (burger|burgers|hamburgers|hamburger) (qui existe|présente|présent) (dans|à) (un autre pays|un pays étranger|l'étranger|en asie).*",
        "response":"Au Japon, les burgers peuvent être garnis de tempura, de wasabi ou même de ramen.",
        "score":2,
        "fatal":False,
        "function":None,
    },
    {
        "id":"nvelle zelande",
        "rule":".*donne moi (un|une) (exemple|variation) de (burger|burgers|hamburgers|hamburger) (qui existe|présente|présent) (dans|à) (un autre pays|un pays étranger|l'étranger|un pays du sud).*",
        "response":"En Nouvelle-Zélande, un burger est souvent garni d'un œuf frit et d'une tranche de betterave.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"sauce",
        "rule":".*(est t'il possible de|peut on) (remplir|garnir) (nos|des|les|dans) (burgers|burger|hamburger|hamburgers) (de|d'une|une) (sauces|sauce spéciale|sauce.*)",
        "response":"En effet, certains burgers sont garnis de sauces spéciales, comme la sauce barbecue, la mayonnaise épicée ou le ketchup maison.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"sucre",
        "rule":".*(peut on|est il possible) (mettre|garnir|de mettre|de garnir) (des choses sucrées|de choses sucrées|de sucreries) (les|des|dans) (burgers|burger|hamburgers|hamburgers).*",
        "response":"Certains burgers sont garnis de condiments et d'ingrédients sucrés, comme le bacon caramélisé ou la confiture de figues, créant un mélange de saveurs sucrées et salées.",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"personalisation",
        "rule":".*(peut on|est il possible de) (modifier|choisir|changer|personnaliser) (la|les) (composition|recette|ingrédients|éléments) (de son|d'un|du) (burger|burgers|hamburgers|hamburgers).*",
        "response":"En effet, les burgers sont souvent personnalisables, permettant aux clients de choisir leurs garnitures préférées parmi une liste d'options.",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"vegetarien",
        "rule":".*(quand|a quelle date|en quelle année) (a été inventé|est apparu|a vu le jour) (le burger végétarien|le premier burger végétarien).*",
        "response":"Le premier hamburger végétarien a été inventé en 1981 par Gregory Sams.",
        "score":1,
        "fatal":False,
        "function":None,
    }, 
    {
        "id":"name",
        "rule":".*(je m'appelle|mon nom est|mon prénom est).*",
        "response":"J'enregistre votre prénom %NAME%! Posez-moi des questions sur l'histoire du hamburger.",
        "score":3,
        "fatal":False,
        "function":None,
    },
    {
        "id":"capitale",
        "rule":".*(quelle|quelle ville) (est|est considérée comme) (la capitale|la ville principale|la ville la plus importante) (pour|du) (burger|burgers|hamburger|hamburgers).*",
        "response":"La ville de Seymour, Wisconsin, est considérée comme la capitale du hamburger.",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"burger king",
        "rule":".*(quand|en quelle année|a quelle date) (a été crée|a été fondée|est apparue|sont apparu) (burger king|la chaîne burger king|l'entreprise burger king|les restaurants rapides burger king|les restaurants burger king).*",
        "response":"Burger King, une des plus grandes chaînes de restauration rapide, a été fondée en 1954.",
        "score":1,
        "fatal":False,
        "function":None,
    },
]



# Print de notre premier message
print("Bonjour, je suis Clint, votre spécialiste dans l'histoire du burger, comment vous appelez-vous ?")

# Démarrage de la boucle du chatbot
while not fatal:
    # On demande le prompt de l'utilisateur
    userinput = input("> ")

    # On cherche un motif à partir de la liste de règles
    rule = findRule(userinput)

    # Si la requette concerne le prénom, on met à jour la variable
    if rule["id"] == "name":
        userName = re.search(r"(?i)(?:je m'appelle|mon nom est|mon prénom est)\s+(\w+)", userinput).group(1)

    # On envoie la réponse de la règle selectionnée
    print(rule['response'].replace("%NAME%", userName))

    # On execute la fonction liée a la règle si elle existe
    if (rule['function'] != None):
        print(rule['function'](userinput))
    
    # On termine le programme si la commande est fatale
    if (rule['fatal']):
        fatal = True