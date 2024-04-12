**État initial :**

L'état initial du problème est défini en termes des propositions étendues données comme suit :

- `aventurier.position(0,5) = True`, où `(x, y)` est la position initiale de l'aventurier.
- `aventurier.etat(0) = True`, car l'aventurier n'a pas trouvé la bijou au début.
- `joyau.position(7,4) = True`, où `(X, Y)` est la position de la bijou.

**État final :**

L'état final du problème est défini comme suit :

- `aventurier.position(7,4) = True`, où `(X, Y)` sont les positions du bijou.
- `aventurier.etat(1) = True`, car l'aventurier a trouvé le bijou.
- `joyau.position(7,4) = True`, où `(X, Y)` est la position de la bijou (elle ne change pas).

**Opérateurs :**

Les opérateurs possibles pour passer d'un état à un autre sont les quatre directions cardinales (haut, bas, gauche, droite) que l'aventurier peut prendre :

- `move_up(X, Y) = (X, Y - 1)`
- `move_down(X, Y) = (X, Y + 1)`
- `move_left(X, Y) = (X - 1, Y)`
- `move_right(X, Y) = (X + 1, Y)`