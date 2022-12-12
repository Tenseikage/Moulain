from point import Point

def creer_liste(type_plat):
    nb_carre = len(Point.liste_objet)/8
    nb_carre = int(nb_carre)
    if type_plat == 3:
        plateau = [['', '', '']*3]
        for point in Point.liste_objet:
            x, y = point.coord
            plateau[x][y] = point
    else:
        plateau = [['','','','','','','','']]*nb_carre
        for point in Point.liste_objet:
            x, y = point.coord
            plateau[x][y] = point
    return plateau


def afficher_plateau(plateau):
    """
    Affiche le plateau
    """
    print(plateau)


def placer_pion(coords, joueur, plateau):
    """
    Place un pion dans le plateau de jeu
    """
    x, y = coords
    plateau[x][y] = joueur
    return plateau


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
    if plateau[x][y] == '':
        return True


def moulin_ligne(coords, plateau, type_plat):
    x, y = coords
    for i in [0, 5]:
        if plateau[x][i].state == plateau[x][i+1].state == plateau[x][i+2].state:
            return True
    if type_plat > 8:
        if plateau[0][3].state == plateau[1][3].state == plateau[2][3].state:
            return True


def moulin_colonne(coords, plateau, type_plat):
    x, y = coords
    if plateau[x][0].state == plateau[x][3].state == plateau[x][5].state:
        return True
    if plateau[x][2].state == plateau[x][4].state == plateau[x][7].state:
        return True
    if type_plat > 8:
        for i in [1, 6]:
            if plateau[0][i].state == plateau[1][i].state == plateau[2][i].state:
                return True


def moulin_diagonale(coords, plateau, type_plat):
    x, y = coords
    if type_plat == 12:
        for i in [0, 2, 5, 7]:
            if plateau[0][i].state == plateau[1][i].state == plateau[2][i].state:
                return True
