def creer_plateau_vide912():
    """
    Créer un plateau vide pour la variante à 9 et 12 pions
    """
    return [['', '', ''],
            ['', '', ''],
            ['', '', '', '', '', ''],
            ['', '', ''],
            ['', '', '']]


def creer_plateau_vierge3():
    """
    Créer un plateau vide pour la variante 3
    """
    return [['', '', ''] for _ in range(3)]


def creer_plateau_vierge6():
    """
    Créer un plateau vide pour la variante 6
    """
    return [['', '', ''],
            ['', '', ''],
            ['', '', '', ''],
            ['', '', ''],
            ['', '', '']]


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
    plateau[x][y] = ''
    plateau[x1][y1] = joueur


def enlever_pion(coords, plateau):
    """
    Enlève un pion dans le plateau de jeu
    """
    x, y = coords
    plateau[x][y] = ''


def check_place(coords, plateau):
    """
    Regarde si l'endroit choisi dans le plateau est libre ou non
    """
    x, y = coords
    if plateau[x][y] == '':
        return True
