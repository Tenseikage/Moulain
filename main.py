from affichage import *
from point import *
from plateau import creer_liste
from menudujeu import *
import sys 

cree_fenetre(1000,800)


def interaction_clavier():
    ev = donne_ev()
    tev = type_ev(ev)
    if tev == 'Quitte':
        sys.exit(0)
        



def main():
    while True:
        mise_a_jour()
        update_points()
        interaction_clavier()



presentation((100,100),2000,2000)
present_text('Jeu du moulin ',(500,200),300,100)
if menu():
    efface_tout()
    animation_plat(3,(400,400),80)
    main()

    