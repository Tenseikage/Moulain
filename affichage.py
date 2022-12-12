from fltk import *
from point import Point


def carre(centre,taille,id_carre):
    '''
    Affiche un carré avec les parametres centre et taille
    avec des points interactifs sur les cotés (grace au objets de la classe point)
    '''
    #faire le carré
    rectangle(centre[0]-taille, centre[0]-taille, centre[1]+taille, centre[1]+taille, 'black', '', 5, 'plato')
    #creer les points sur le carré
    id_point = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                point = Point((centre[0] + taille * j, centre[1] + taille * i),(id_carre,id_point))
                id_point += 1
                point.affiche()


def affiche_plateforme1(centre,taille):#basique
    '''
    Affiche la plateforme du jeu basique avec des points interactifs
    '''
    rectangle(centre[0] - taille*3, centre[0] - taille*3, centre[1] + taille*3, centre[1] + taille*3, '', '#eee1c6', 0,'plato')

    id_carre = 3
    for i in range(3):
        id_carre -= 1
        carre(centre,taille*(i+1),id_carre)
    #lignes
    ligne(centre[0], centre[1] - 3*taille, centre[0], centre[1] - taille, couleur='black', epaisseur=5, tag='plato')
    ligne(centre[0], centre[1] + 3 * taille, centre[0], centre[1] + taille, couleur='black', epaisseur=5, tag='plato')
    ligne(centre[0]- 3 * taille, centre[1],centre[0]- taille, centre[1], couleur='black', epaisseur=5, tag='plato')
    ligne(centre[0] + 3 * taille, centre[1], centre[0] + taille, centre[1], couleur='black', epaisseur=5, tag='plato')

def affiche_plateforme2(centre,taille): # a 12
    '''
    Affiche la plateforme de la variante du jeu a 12
    avec des points interactifs
    '''
    rectangle(centre[0] - taille*3, centre[0] - taille*3, centre[1] + taille*3, centre[1] + taille*3, couleur='', remplissage='#eee1c6', epaisseur=0,tag='plato')
    id_carre = 3
    for i in range(3):
        id_carre -= 1
        carre(centre,taille*(i+1),id_carre)
    #lignes
    for i in (0,1,-1):
        for j in (-1,1,0):
            ligne(centre[0] + 3*i * taille, centre[1] + 3*j * taille, centre[0] + i * taille, centre[1] + j * taille, couleur='black', epaisseur=5, tag='plato')


def affiche_plateforme3(centre,taille): # petit
    '''
    Affiche la plateforme de la variante du jeu avec petite plateforme
    avec des points interactifs
    '''
    taille *= 3/2
    id_carre = 2
    rectangle(centre[0] - taille*2, centre[0] - taille*2, centre[1] + taille*2, centre[1] + taille*2, couleur='', remplissage='#eee1c6', epaisseur=0,tag='plato')
    for i in range(2):
        id_carre -= 1
        carre(centre,taille*(i+1),id_carre)
    #lignes
    ligne(centre[0], centre[1] - 2 * taille, centre[0], centre[1] - taille, couleur='black', epaisseur=5, tag='plato')
    ligne(centre[0], centre[1] + 2 * taille, centre[0], centre[1] + taille, couleur='black', epaisseur=5, tag='plato')
    ligne(centre[0] - 2 * taille, centre[1], centre[0] - taille, centre[1], couleur='black', epaisseur=5, tag='plato')
    ligne(centre[0] + 2 * taille, centre[1], centre[0] + taille, centre[1], couleur='black', epaisseur=5, tag='plato')

def affiche_plateforme4(centre,taille): #croisé
    '''
    Affiche la plateforme de la variante du jeu a 3 pion
    avec des points interactifs
    '''
    taille *= 3/2
    rectangle(centre[0] - taille, centre[0] - taille, centre[1] + taille, centre[1] + taille, couleur='', remplissage='#eee1c6', epaisseur=0,tag='plato')
    carre(centre, taille,0)
    point = Point(centre,(1,1))
    point.affiche()
    ligne(centre[0] - taille, centre[0] - taille, centre[1] + taille, centre[1] + taille, couleur='black', epaisseur=5,tag='plato')
    ligne(centre[0], centre[0] - taille, centre[1], centre[1] + taille, couleur='black', epaisseur=5,tag='plato')
    ligne(centre[0] + taille, centre[0] - taille, centre[1] - taille, centre[1] + taille, couleur='black', epaisseur=5,tag='plato')
    ligne(centre[0] - taille, centre[0], centre[1] + taille, centre[1], couleur='black', epaisseur=5,tag='plato')


def animation_plat(plat,centre,taille):
    affiche_plat = [affiche_plateforme1, affiche_plateforme2 ,
                    affiche_plateforme3, affiche_plateforme4]

    for i in range(taille):
        affiche_plat[plat-1](centre, i)
        for p in Point.liste_objet:
            p.efface()
            del p

        Point.liste_objet = []
        mise_a_jour()
        efface('plato')
    affiche_plat[plat-1](centre, taille)
