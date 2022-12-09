from affichage import *
import point as point

cree_fenetre(1000,800)


animationtrocool(1,(400,400),80)

def interaction_clavier():
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == 'Quitte':
        ferme_fenetre()



def main():
    while True:
        mise_a_jour()

        point.update_points()

        interaction_clavier()



main()