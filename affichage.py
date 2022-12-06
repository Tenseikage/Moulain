from fltk import *
from point import Point


def carre(centre,t):
    rectangle(centre[0]-t, centre[0]-t,centre[1]+t,centre[1]+t, couleur='black', remplissage='', epaisseur=5, tag='plato')

    #creer les points
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or j != 0:
                point = Point((centre[0] + t*j,centre[1] + t*i))
                point.affiche()


def affiche_plateforme1(centre,taille): #basique
    rectangle(centre[0] - taille*3, centre[0] - taille*3, centre[1] + taille*3, centre[1] + taille*3, couleur='', remplissage='#eee1c6', epaisseur=0,tag='plato')
    for i in range(3):
        carre(centre,taille*(i+1))
    #lignes
    ligne(centre[0], centre[1] - 3*taille, centre[0], centre[1] - taille, couleur='black', epaisseur=5, tag='')
    ligne(centre[0], centre[1] + 3 * taille, centre[0], centre[1] + taille, couleur='black', epaisseur=5, tag='')
    ligne(centre[0]- 3 * taille, centre[1],centre[0]- taille, centre[1], couleur='black', epaisseur=5, tag='')
    ligne(centre[0] + 3 * taille, centre[1], centre[0] + taille, centre[1], couleur='black', epaisseur=5, tag='')

def affiche_plateforme2(centre,taille): # a 12
    rectangle(centre[0] - taille*3, centre[0] - taille*3, centre[1] + taille*3, centre[1] + taille*3, couleur='', remplissage='#eee1c6', epaisseur=0,tag='plato')
    for i in range(3):
        carre(centre,taille*(i+1))
    #lignes
    for i in (0,1,-1):
        for j in (-1,1,0):
            ligne(centre[0] + 3*i * taille, centre[1] + 3*j * taille, centre[0] + i * taille, centre[1] + j * taille, couleur='black', epaisseur=5, tag='')


def affiche_plateforme3(centre,taille): # petit
    taille = 3/2 * taille
    rectangle(centre[0] - taille*2, centre[0] - taille*2, centre[1] + taille*2, centre[1] + taille*2, couleur='', remplissage='#eee1c6', epaisseur=0,tag='plato')
    for i in range(2):
        carre(centre,taille*(i+1))
    #lignes
    ligne(centre[0], centre[1] - 2 * taille, centre[0], centre[1] - taille, couleur='black', epaisseur=5, tag='')
    ligne(centre[0], centre[1] + 2 * taille, centre[0], centre[1] + taille, couleur='black', epaisseur=5, tag='')
    ligne(centre[0] - 2 * taille, centre[1], centre[0] - taille, centre[1], couleur='black', epaisseur=5, tag='')
    ligne(centre[0] + 2 * taille, centre[1], centre[0] + taille, centre[1], couleur='black', epaisseur=5, tag='')

def affiche_plateforme4(centre,taille): #croisé
    taille *= 3/2
    rectangle(centre[0] - taille, centre[0] - taille, centre[1] + taille, centre[1] + taille, couleur='', remplissage='#eee1c6', epaisseur=0,tag='plato')
    carre(centre, taille)
    point = Point(centre)
    point.affiche()
    ligne(centre[0] - taille, centre[0] - taille, centre[1] + taille, centre[1] + taille, couleur='black', epaisseur=5,tag='plato')
    ligne(centre[0], centre[0] - taille, centre[1], centre[1] + taille, couleur='black', epaisseur=5,tag='plato')
    ligne(centre[0] + taille, centre[0] - taille, centre[1] - taille, centre[1] + taille, couleur='black', epaisseur=5,tag='plato')
    ligne(centre[0] - taille, centre[0], centre[1] + taille, centre[1], couleur='black', epaisseur=5,tag='plato')


def animationtrocool(plat,centre,taille):
    if plat == 0:
        lol = affiche_plateforme1()
    elif plat == 1:
        lol = affiche_plateforme2
    elif plat == 3:
        lol = affiche_plateforme3
    else:
        lol = affiche_plateforme4

    for i in range(taille):
        lol(centre, i)
        for p in Point.liste_objet:
            p.efface()
        Point.liste_objet = []
        mise_a_jour()
        efface_tout()
    lol(centre, taille)