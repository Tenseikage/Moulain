import affichage as aff
import fltk as tk
import plateau as plat
from point import update_points
import menudujeu as menu
import sys

tk.cree_fenetre(1000, 800)


def interaction_clavier():
    ev = tk.donne_ev()
    tev = tk.type_ev(ev)
    if tev == 'Quitte':
        sys.exit()


def initialisation_jeu():
    '''
    ah
    '''
    aff.animation_plat(1, (400, 400), 80, False)

    plateau = plat.creer_liste()
    nb_blanc = 0
    nb_noir = 0
    return plateau, nb_blanc, nb_noir


def attend_apui_bouton():
    '''
    Cree le menu ensuite,
    Attend qu'un bouton a été apuiyé dans le menu
    si oui, efface le menu et laisse le jeu ce jouer
    '''
    menu.presentation((100, 100), 2000, 2000)
    if menu.menu():
        tk.efface_tout()


def main_jeu():
    while True:
        tk.mise_a_jour()
        update_points()
        interaction_clavier()


def main():
    attend_apui_bouton()

    initialisation_jeu()
    main_jeu()

main()
