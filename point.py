from fltk import cercle,abscisse_souris,ordonnee_souris,efface
from random import random

class Point:
    liste_objet=[]
    def __init__(self,pos,coord):
        self.pos = pos
        self.color = 'black'
        self.state = ''
        self.coord = coord
        self.tag = str(random())
        Point.liste_objet.append(self)

    def affiche(self):
        cercle(self.pos[0], self.pos[1], 10, couleur=self.color ,remplissage=self.color, tag='plato')

    def efface(self):
        efface(self.tag)

    def update(self):
        self.efface()
        self.affiche()

    def mouse_over(self):
        if self.pos[0] - 10 < abscisse_souris() < self.pos[0] + 10 and self.pos[1] - 10 < ordonnee_souris() < self.pos[1] + 10:
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