from affichage import *
from point import Point

cree_fenetre(1000,800)


animationtrocool(1,(400,400),80)


def main():
    while True:
        mise_a_jour()
        for position in Point.liste_objet:
            position.mouse_over()

        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'Quitte':
            break


    ferme_fenetre()



main()