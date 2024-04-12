# Co-authored-by: nezuraa <nezuraa@users.noreply.github.com>
# Co-authored-by: Davidbld <Davidbld@users.noreply.github.com>
# Co-authored-by: Kez0x <Kez0x@users.noreply.github.com>

import mapParser
map = mapParser.parseMap("TD4/map.txt")

aventurier = {"position" : (0,5), "etat" : 0,}
joyau = {"position" : (7,4)}

def print_map(map, aventurier, joyau):
    """
    Entrée : la map sous forme de matrice, aventurier : un dictionnaire avec la position de l'aventurier et l'état de l'aventurier, joyau : un dictionnaire avec la postion du joyau
    Sortie : la map afficher correctement
    """
    display = ""
    for y in range(len(map)):
        line = map[y]
        for x in range(len(line)):
            element = line[x]
            if (x, y) == aventurier['position']:
                display += "A "
            elif (x, y) == joyau['position']:
                display += "* "
            elif element == 0:
                display += "- "
            else:
                display += "X "
        display += '\n'
    return display


moves = {'up' : (0,-1), 'left' : (-1,0), 'right' : (1,0), 'down' : (0,1)}

def get_positions_possibles(aventurier):
    possibilitiesArray = []
    for possibilites in moves:
        possibilitiesArray.append((aventurier['position'][0] + moves[possibilites][0], aventurier['position'][1] + moves[possibilites][1]))
    return possibilitiesArray

def est_autorisee(position):
    rep = True
    if position[0]<0 or position[0]>len(map)-1 or position[1]<0 or position[1]>len(map)-1:
        rep = False
    elif map[position[1]][position[0]]==1:
        rep = False
    return rep

def prochaine_pos(a_explorer,deja_explorer):
    for positions in get_positions_possibles(aventurier):
            if est_autorisee(positions) and positions not in deja_explorer:
                a_explorer.append(positions)
    


def start():
    touch = ""
    a_explorer = []
    deja_explorer = []
    while touch!='Q':
        touch = str(input("Choisissez une action : "))
        print(print_map(map, aventurier, joyau))
        
        
    
start()
