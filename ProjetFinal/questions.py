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
]