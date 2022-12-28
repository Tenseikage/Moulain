from fltk import cercle,abscisse_souris,ordonnee_souris,efface
from random import random

class Point:
    liste_objet=[]
    def __init__(self,pos,coord,dummy):
        self.pos = pos
        self.color = 'black'
        self.state = ''
        self.coord = coord
        self.tag = str(random())
        self.dummy = dummy
        if not dummy:
            Point.liste_objet.append(self)

    def affiche(self):
        cercle(self.pos[0], self.pos[1], 13, couleur=self.color ,remplissage=self.color, tag=self.tag)

    def efface(self):
        efface(self.tag)

    def update(self):
        self.efface()
        self.affiche()

    def mouse_over(self):
        if self.pos[0] - 13 < abscisse_souris() < self.pos[0] + 13 and self.pos[1] - 13 < ordonnee_souris() < self.pos[1] + 13:
            self.color = 'red'
            self.update()
            return True
        else:
            self.color = 'black'
            self.update()
            return False

def update_points():
    for position in Point.liste_objet:
        if position.mouse_over():
            position.color = 'red'
        else:
            position.color = 'black'
        position.update()