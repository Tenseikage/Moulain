from point import Point

def creer_liste(type_plat):
    nb_carre = len(Point.liste_objet)/8
    nb_carre = int(nb_carre)
    if type_plat == 4:
        plateau = list([['', '', ''] for _ in range(3)])
        for point in Point.liste_objet:
            x, y = point.coord
            plateau[x][y] = point
    else:
        plateau = [['','','','','','','',''] for _ in range(nb_carre)]
        for point in Point.liste_objet:
            x, y = point.coord
            plateau[x][y] = point
    return plateau


def placer_pion(coords, joueur, plateau):
    """
    Place un pion dans le plateau de jeu
    retourne le plateau et la validité du coup
    plateau inchangé si coup non valide
    """
    if verif_place(coords, plateau):
        x, y = coords
        plateau[x][y].state = joueur
        return (plateau,True)
    else:
        return (plateau,False)

def point_adjacent(type_plat,poin1,poin2):
    adj_memm_carre = {
        0:(1,3),
        1:(0,2),
        2:(1,4),
        3:(0,5),
        4:(2,7),
        5:(3,6),
        6:(5,7),
        7:(6,4)
    }
    x,y = poin1
    u,v = poin2
    if abs(x-u) == 2:
        return False
    if x-u == 0 and v in adj_memm_carre[y]:
        return True
    if abs(x-u) == 1:
        if type_plat == 2 and y == v:
            return True
        else:
            return (y in (1,3,4,6) and y==v)
    return False

print(point_adjacent(2,(1,1),(0,2)))

def deplacer_pion(coords, nwcoords, plateau,type_plat):
    """
    Déplace un pion dans le plateau de jeu
    """
    if type_plat == 4:
        return True
    if not point_adjacent(type_plat,coords,nwcoords):
        return False
    x, y = coords
    x1, y1 = nwcoords
    if plateau[x][y].state == '':
       plateau[x][y].state, plateau[x1][y1].state = plateau[x1][y1].state,plateau[x][y].state
       return True
    else:
        return False


def enlever_pion(coords, plateau):
    """
    Enlève un pion dans le plateau de jeu
    """
    x, y = coords
    plateau[x][y].state = ''


def verif_place(coords, plateau):
    """
    Regarde si l'endroit choisi dans le plateau est libre ou non
    """
    x, y = coords
    if plateau[x][y].state == '':
        return True
    return False

def moulin_dans_un_carre(carre,joueur):
    nb_moulin = 0
    if carre[0].state == carre[1].state == carre[2].state == joueur:
        nb_moulin += 1
    elif carre[5].state == carre[6].state == carre[7].state == joueur:
        nb_moulin += 1
    elif carre[2].state == carre[4].state == carre[7].state == joueur:
        nb_moulin += 1
    elif carre[0].state == carre[3].state == carre[5].state == joueur:
        nb_moulin += 1
    return nb_moulin

def moulin_joueur(plateau,joueur,type_plat):
    moulin = 0
    for carre in plateau:
        moulin = moulin + moulin_dans_un_carre(carre,joueur)
    if len(plateau) == 3:
        for i in (1, 3, 4, 6):
            if plateau[0][i].state == plateau[1][i].state == plateau[2][i].state == joueur:
                moulin += 1

    if type_plat == 2:
        moulin += moulin_diagonal(plateau,joueur)
    return moulin

def moulin(plateau,type_plat):
    if type_plat == 4:
        return moulin_variante_4(plateau)
    return moulin_joueur(plateau,'b',type_plat) + moulin_joueur(plateau,'n',type_plat)

def moulin_diagonal(plateau,joueur):
    moulin_diag = 0
    for i in (0, 2, 5, 7):
        if plateau[0][i].state == plateau[1][i].state == plateau[2][i].state == joueur:
            moulin_diag += 1
    return moulin_diag

def moulin_variante_4(plateau):
    moulin = 0
    for i in range(3):
        if plateau[i][0].state == plateau[i][1].state == plateau[i][2].state != '':
            moulin += 1
    for i in range(3):
        if plateau[0][i].state == plateau[1][1].state == plateau[2][i].state != '':
            moulin += 1
    if plateau[0][0].state == plateau[1][1].state == plateau[2][2].state != '':
        moulin += 1
    if plateau[0][2].state == plateau[1][1].state == plateau[2][0].state != '':
        moulin += 1
    return moulin








    

