Intermg = (3,0)
Intercg = (3,0)
Interbg = (1,0)

init_state = (3, 3, 1)
final_state = (0, 0, 0)

possible_move = [
    (-1,-1,-1),
    (-2,0,-1),
    (0,-2,-1),
    (-1,0,-1),
    (0,-1,-1),
    (2,0,1),
    (1,1,1),
    (0,2,1),
    (1,0,1),
    (0,1,1),
]

forbidden_move = [
    (1,0,0),
    (0,0,1),
    (1,0,1),
    (1,3,0),
    (1,2,0),
    (2,1,0),
    (2,0,0),
    (1,3,1),
    (1,2,1),
    (2,1,1),
    (2,0,1),
    (2,3,0),
    (2,3,1)
]

def validation(state):
    if state in forbidden_move or state[0] > Intermg[0] or state[0]  < Intermg[1] or state[1] > Intercg[0] or state[1] < Intercg[1] or state[2] > Interbg[0] or state[2] < Interbg[1]:
        rep = False
    else : 
        rep = True
    return rep

def change_state(state, moves):
    # Création du nouvel état
    mg = state[0] + moves[0]
    cg = state[1] + moves[1]
    bg = state[2] + moves[2]
    new_state = (mg, cg, bg)
    return new_state   

a_explorer = [init_state]
deja_explore = []
etat_parent = {}

while len(a_explorer) != 0:
    for move in possible_move:
        new_state = change_state(a_explorer[0],move)
        if validation(new_state):
            etat_parent[new_state] = a_explorer[0]
            a_explorer.append(new_state)
    deja_explore.append(a_explorer.pop(0))
        
def affiche_solution(state):
    for elements in etat_parent:
        if etat_parent[elements] == state:
            print(elements)

affiche_solution(final_state)