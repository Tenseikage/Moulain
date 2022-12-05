from affichage import *
from point import Point

cree_fenetre(1000,800)


#affiche_plateforme1((400,400),100)

while True:
    for i in range(100):
        affiche_plateforme2((400, 400), i)
        for p in Point.liste_objet:
            p.efface()
        Point.liste_objet = []
        mise_a_jour()
        efface_tout()


def main():
    while True:
        mise_a_jour()
        for position in Point.liste_objet:
            position.mouse_over()





main()