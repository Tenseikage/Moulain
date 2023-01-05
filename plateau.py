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



def deplacer_pion(coords, nwcoords, joueur, plateau):
    """
    Déplace un pion dans le plateau de jeu
    """
    x, y = coords
    x1, y1 = nwcoords
    plateau[x][y].state = ''
    plateau[x1][y1] = joueur


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

def moulin_joueur(plateau,joueur):
    moulin = 0
    for carre in plateau:
        moulin = moulin + moulin_dans_un_carre(carre,joueur)
        #(1,3,4,6):
    if len(plateau) == 3:
        for i in (1, 3, 4, 6):
            if plateau[0][i].state == plateau[1][i].state == plateau[2][i].state == joueur:
                moulin += 1

    if diag_a_check:
        moulin += moulin_diagonal(plateau,joueur)
    return moulin

def moulin(plateau):
    return moulin_joueur(plateau,'b') + moulin_joueur(plateau,'n')

def moulin_diagonal(plateau,joueur):
    moulin_diag = 0
    for i in (0, 2, 5, 7):
        if plateau[0][i].state == plateau[1][i].state == plateau[2][i].state == joueur:
            moulin_diag += 1
    return moulin_diag