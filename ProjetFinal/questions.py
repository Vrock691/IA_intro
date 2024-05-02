questionsAvailables = [
    {
        "id": 1,
        "message": "A quelle saison votre légume est il majoritairement rattaché ?",
        "attribute": "season",
        "responsesAvailables": {
            "printemps": {
                "query": "season == 1",
                "drop": None,
                "eliminate": [1],
                "fatal": False,
            },
            "été|ete": {
                "query": "season == 2",
                "drop": None,
                "eliminate": [1],
                "fatal": False,
            },
            "automne": {
                "query": "season == 3",
                "drop": None,
                "eliminate": [1],
                "fatal": False,
            },
            "hiver": {
                "query": "season == 4",
                "drop": None,
                "eliminate": [1],
                "fatal": False,
            },
        },
    },
    {
        "id": 2,
        "message": "Votre légume est-il majoritairement vert ?",
        "attribute": "green",
        "responsesAvailables": {
            "yes|oui": {
                "query": "green == 1",
                "drop": None,
                "eliminate": [2],
                "fatal": False,
            },
            "no|non": {
                "query": "green == 0",
                "drop": None,
                "eliminate": [2],
                "fatal": False,
            },
        },
    },
    {
        "id": 3,
        "message": "Votre légume est-il une racine ?",
        "attribute": "root",
        "responsesAvailables": {
            "yes|oui": {
                "query": "root == 1",
                "drop": None,
                "eliminate": [3],
                "fatal": False,
            },
            "no|non": {
                "query": "root == 0",
                "drop": None,
                "eliminate": [3],
                "fatal": False,
            },
        },
    },
    {
        "id": 4,
        "message": "Votre légume est-il une fleur ?",
        "attribute": "flower",
        "responsesAvailables": {
            "yes|oui": {
                "query": "flower == 1",
                "drop": None,
                "eliminate": [4],
                "fatal": False,
            },
            "no|non": {
                "query": "flower == 0",
                "drop": None,
                "eliminate": [4],
                "fatal": False,
            },
        },
    },
]