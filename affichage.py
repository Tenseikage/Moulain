from fltk import rectangle, ligne, efface, mise_a_jour
from point import Point
from random import random

def carre(centre,taille,id_carre,dummy,tag):
    '''
    Affiche un carré avec les parametres centre et taille
    avec des points interactifs sur les cotés (grace au objets de la classe point)
    '''
    #faire le carré
    rectangle(centre[0]-taille, centre[1]-taille, centre[0]+taille, centre[1]+taille, 'black', '', 7, tag)
    #creer les points sur le carré
    id_point = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                point = Point((centre[0] + taille * j, centre[1] + taille * i),(id_carre,id_point), dummy)
                id_point += 1
                point.affiche()

class Plateau:
    def __init__(self,centre,taille,type,dummy):
        self.centre = centre
        self.taille = taille
        self.dummy = dummy
        self.type = type
        self.tag = str(random()) #tag unique pour fltk

    def affiche(self):  # basique
        '''
        Affiche la plateforme du jeu basique avec des points interactifs
        '''
        rectangle(self.centre[0] - self.taille * 3, self.centre[1] - self.taille * 3, self.centre[0] + self.taille * 3,self.centre[1] + self.taille * 3, '', '#eee1c6', 0, self.tag)

        if self.type == 1:

            ligne(self.centre[0], self.centre[1] - 3 * self.taille, self.centre[0], self.centre[1] - self.taille, couleur='black', epaisseur=7,tag=self.tag)
            ligne(self.centre[0], self.centre[1] + 3 * self.taille, self.centre[0], self.centre[1] + self.taille, couleur='black', epaisseur=7,tag=self.tag)
            ligne(self.centre[0] - 3 * self.taille, self.centre[1], self.centre[0] - self.taille, self.centre[1], couleur='black', epaisseur=7,tag=self.tag)
            ligne(self.centre[0] + 3 * self.taille, self.centre[1], self.centre[0] + self.taille, self.centre[1], couleur='black', epaisseur=7,tag=self.tag)
        id_carre = 3
        for i in range(3):
            id_carre -= 1
            carre(self.centre, self.taille * (i + 1), id_carre, self.dummy, self.tag)

        if self.type == 2:
            # lignes
            for i in (0, 1, -1):
                for j in (-1, 1, 0):
                    ligne(self.centre[0] + 3 * i * self.taille, self.centre[1] + 3 * j * self.taille, self.centre[0] + i * self.taille, self.centre[1] + j * self.taille, 'black', 7, self.tag)
            id_carre = 3
            for i in range(3):
                id_carre -= 1
                carre(self.centre, self.taille * (i + 1), id_carre, self.dummy, self.tag)

        if self.type == 3:
            # lignes
            ligne(self.centre[0], self.centre[1] - 2 * self.taille*3/2, self.centre[0], self.centre[1] - self.taille*3/2, couleur='black', epaisseur=7,tag=self.tag)
            ligne(self.centre[0], self.centre[1] + 2 * self.taille*3/2, self.centre[0], self.centre[1] + self.taille*3/2, couleur='black', epaisseur=7,tag=self.tag)
            ligne(self.centre[0] - 2 * self.taille*3/2, self.centre[1], self.centre[0] - self.taille*3/2, self.centre[1], couleur='black', epaisseur=7,tag=self.tag)
            ligne(self.centre[0] + 2 * self.taille*3/2, self.centre[1], self.centre[0] + self.taille*3/2, self.centre[1], couleur='black', epaisseur=7,tag=self.tag)

            id_carre = 2
            for i in range(2):
                id_carre -= 1
                carre(self.centre, self.taille * 3 / 2 * (i + 1), id_carre, self.dummy, self.tag)

        if self.type == 4:
            rectangle(self.centre[0] - self.taille * 3 , self.centre[1] - self.taille * 3 ,self.centre[0] + self.taille * 3, self.centre[1] + self.taille * 3, 'black', '', 7,self.tag)

            ligne(self.centre[0], self.centre[1] - 3 * self.taille, self.centre[0], self.centre[1],couleur='black', epaisseur=7, tag=self.tag)
            ligne(self.centre[0], self.centre[1] + 3 * self.taille, self.centre[0], self.centre[1],couleur='black', epaisseur=7, tag=self.tag)
            ligne(self.centre[0] - 3 * self.taille, self.centre[1], self.centre[0], self.centre[1],couleur='black', epaisseur=7, tag=self.tag)
            ligne(self.centre[0] + 3 * self.taille, self.centre[1], self.centre[0], self.centre[1],couleur='black', epaisseur=7, tag=self.tag)

            ligne(self.centre[0] - 3 * self.taille, self.centre[1] - 3 * self.taille, self.centre[0] + 3 * self.taille, self.centre[1] + 3 * self.taille, couleur='black',epaisseur=7, tag=self.tag)
            ligne(self.centre[0] + 3 * self.taille, self.centre[1] - 3 * self.taille, self.centre[0] - 3 * self.taille, self.centre[1] + 3 * self.taille, couleur='black', epaisseur=7, tag=self.tag)

            for i in range(-1, 2):
                for j in range(-1, 2):
                    point = Point((self.centre[0] + self.taille * 3 * i, self.centre[1] + self.taille * 3 * j),
                                  (j + 1, i + 1), self.dummy)
                    point.affiche()


    def affiche_animation(self):
        '''
        Anime l'aparition du plateau
        '''
        for i in range(self.taille):
            self.taille = i + 1
            self.affiche()
            mise_a_jour()

            for p in Point.liste_objet:
                p.efface()
                del p
            Point.liste_objet = []
            efface(self.tag)

        self.affiche()