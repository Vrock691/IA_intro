import externalfunctions
# On importe les fonctions nécéssaire à certaines règles 

# la liste des règles
rules = [
    {
        "id": "Je sais pas",
        "rule": ".*",
        "response": "Désolé, je ne sais pas.",
        "score": 0,
        "fatal": False,
        "function": None,
    },
    {
        "id": "Bonjour",
        "rule": "Bonjour .*",
        "response": "Bonjour, comment puis-je vous aider ?",
        "score": 1,
        "fatal": False,
        "function": None,
    },
    {
        "id": "Aurevoir",
        "rule": "Au revoir .*",
        "response": "Ravi d'avoir pu vous aider",
        "score": 1,
        "fatal": True,
        "function": None,
    },
    {
        "id": "Salut",
        "rule": "Salut .*",
        "response": "Salut, comment va tu ?",
        "score": 1,
        "fatal": False,
        "function": None,
    },
    {
        "id": "Hello",
        "rule": "Hello .*",
        "response": "Hello, comment puis-je t'aider ?",
        "score": 1,
        "fatal": False,
        "function": None,
    },
    {
        "id":"addition",
        "rule":"Peut tu me faire une addition ? .*",
        "response":"Bien sûr !",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"Division",
        "rule":"Peut tu me faire une division ? .*",
        "response":"Bien sûr !, tappez donc x/y",
        "score":1,
        "fatal":False,
        "function":None,
    },
    {
        "id":"x/y",
        "rule":"x/y .*",
        "response":"Voilà le résultat de votre division",
        "score":1,
        "fatal":False,
        "function": externalfunctions.Divide
    },
    {
        "id":"x+y",
        "rule":"extern",
        "response":"Voilà le résultat de votre addition",
        "score":1,
        "fatal":False,
        "function": externalfunctions.Sum
    },
]