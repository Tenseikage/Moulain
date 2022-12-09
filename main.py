from affichage import *
import point as point
from plateau import creer_liste


cree_fenetre(1000,800)


animationtrocool(3,(400,400),80)

def interaction_clavier():
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == 'Quitte':
        ferme_fenetre()



def main():
    print(creer_liste())
    while True:
        mise_a_jour()

        point.update_points()

        interaction_clavier()



main()