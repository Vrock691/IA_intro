questionsAvailables = [
    {
        "id": 1,
        "message": "A quelle saison votre légume est il majoritairement rattaché ?",
        "attribute": "season",
        "responsesAvailables": {
            "printemps": {
                "query": "season == 1",
                "drop": None,
                "eliminate": ["season"],
                "fatal": False,
            },
            "été|ete": {
                "query": "season == 2",
                "drop": None,
                "eliminate": ["season"],
                "fatal": False,
            },
            "automne": {
                "query": "season == 3",
                "drop": None,
                "eliminate": ["season"],
                "fatal": False,
            },
            "hiver": {
                "query": "season == 4",
                "drop": None,
                "eliminate": ["season"],
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
                "eliminate": ["white", 'green', 'orange'],
                "fatal": False,
            },
            "no|non": {
                "query": "green == 0",
                "drop": None,
                "eliminate": ["white", 'green', 'orange'],
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
                "eliminate": ["root"],
                "fatal": False,
            },
            "no|non": {
                "query": "root == 0",
                "drop": None,
                "eliminate": ["root"],
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
                "eliminate": ["flower"],
                "fatal": False,
            },
            "no|non": {
                "query": "flower == 0",
                "drop": None,
                "eliminate": ["flower"],
                "fatal": False,
            },
        },
    },
    {
        "id": 5,
        "message": "Votre légume est-il un légume-fruit ?",
        "attribute": "fruit",
        "responsesAvailables": {
            "yes|oui": {
                "query": "fruit == 1",
                "drop": None,
                "eliminate": ["fruit"],
                "fatal": False,
            },
            "no|non": {
                "query": "fruit == 0",
                "drop": None,
                "eliminate": ["fruit"],
                "fatal": False,
            },
        },
    },
    {
        "id": 5,
        "message": "Votre légume est-il un légume-feuille ?",
        "attribute": "leaf",
        "responsesAvailables": {
            "yes|oui": {
                "query": "leaf == 1",
                "drop": None,
                "eliminate": ["leaf"],
                "fatal": False,
            },
            "no|non": {
                "query": "leaf == 0",
                "drop": None,
                "eliminate": ["leaf"],
                "fatal": False,
            },
        },
    },
    {
        "id": 6,
        "message": "Votre légume est-il une graine ?",
        "attribute": "seed",
        "responsesAvailables": {
            "yes|oui": {
                "query": "seed == 1",
                "drop": None,
                "eliminate": ["seed"],
                "fatal": False,
            },
            "no|non": {
                "query": "seed == 0",
                "drop": None,
                "eliminate": ["seed"],
                "fatal": False,
            },
        },
    },
    {
        "id": 7,
        "message": "Votre légume est-il un légume aromatique ?",
        "attribute": "aromatic",
        "responsesAvailables": {
            "yes|oui": {
                "query": "aromatic == 1",
                "drop": None,
                "eliminate": ["aromatic"],
                "fatal": False,
            },
            "no|non": {
                "query": "aromatic == 0",
                "drop": None,
                "eliminate": ["aromatic"],
                "fatal": False,
            },
        },
    },
    {
        "id": 8,
        "message": "Votre légume est-il un tubercule ?",
        "attribute": "tuber",
        "responsesAvailables": {
            "yes|oui": {
                "query": "tuber == 1",
                "drop": None,
                "eliminate": ["tuber"],
                "fatal": False,
            },
            "no|non": {
                "query": "tuber == 0",
                "drop": None,
                "eliminate": ["tuber"],
                "fatal": False,
            },
        },
    },
    {
        "id": 9,
        "message": "Votre légume est-il un bulbe ?",
        "attribute": "bulb",
        "responsesAvailables": {
            "yes|oui": {
                "query": "bulb == 1",
                "drop": None,
                "eliminate": ["bulb"],
                "fatal": False,
            },
            "no|non": {
                "query": "bulb == 0",
                "drop": None,
                "eliminate": ["bulb"],
                "fatal": False,
            },
        },
    },
    {
        "id": 10,
        "message": "Votre légume est-il une tige ?",
        "attribute": "stems",
        "responsesAvailables": {
            "yes|oui": {
                "query": "stems == 1",
                "drop": None,
                "eliminate": ["stems"],
                "fatal": False,
            },
            "no|non": {
                "query": "stems == 0",
                "drop": None,
                "eliminate": ["stems"],
                "fatal": False,
            },
        },
    },
    {
        "id": 10,
        "message": "Votre légume est-il majoritairement blanc ?",
        "attribute": "white",
        "responsesAvailables": {
            "yes|oui": {
                "query": "white == 1",
                "drop": None,
                "eliminate": ["white", 'green', 'orange'],
                "fatal": False,
            },
            "no|non": {
                "query": "white == 0",
                "drop": None,
                "eliminate": ["white"],
                "fatal": False,
            },
        },
    },
    {
        "id": 10,
        "message": "Votre légume est-il majoritairement orange ?",
        "attribute": "orange",
        "responsesAvailables": {
            "yes|oui": {
                "query": "orange == 1",
                "drop": None,
                "eliminate": ["white", 'green', 'orange'],
                "fatal": False,
            },
            "no|non": {
                "query": "orange == 0",
                "drop": None,
                "eliminate": ["orange"],
                "fatal": False,
            },
        },
    },
]