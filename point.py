from fltk import cercle,abscisse_souris,ordonnee_souris,efface,donne_ev,type_ev,image
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
        if self.state == '':
            cercle(self.pos[0], self.pos[1], 13, couleur=self.color ,remplissage=self.color, tag=self.tag)
        elif self.state == 'n':
                image(self.pos[0]+30,self.pos[1]+30, 'Moulain/images_jeu/oreo6.png', tag=self.tag) #78% 
        elif self.state == 'b':
            image(self.pos[0]+3,self.pos[1]+3, 'Moulain/images_jeu/orero1.png', tag=self.tag)

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
            ev = donne_ev()
            tev = type_ev(ev)
            if tev == 'ClicGauche':
                print(position.coord)
                return position.coord
        else:
            position.color = 'black'
        position.update()