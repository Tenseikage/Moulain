import fltk as tk
import plateau as plat
from point import update_points
import menudujeu as menu
import sys
from affichage import Plateau

tk.cree_fenetre(1000, 800)


def interaction_clavier():
    '''
    gere les interactions
    (evenements fltk)
    '''
    ev = tk.donne_ev()
    tev = tk.type_ev(ev)
    if tev == 'Quitte':
        sys.exit()


def initialisation_jeu(type_plat):
    '''
    affiche et cree le plateau
    ainsi que cree les
    variable du nombre de pions
    '''
    tk.rectangle(0, 0, 1000, 1000, '','#999999', 0, 'background')

    plate = Plateau((300,300),80,type_plat,False)
    plate.affiche_animation()
    if plate.type !=4:
        plateau = plat.creer_liste()
    else:
        plateau = ''
        pass #creer lliste de plateau croisé (a voir comment vous voulez faire la logique de celui la)
    return plateau

def attend_apui_bouton():
    '''
    Cree le menu ensuite,
    Attend qu'un bouton a été apuiyé dans le menu
    si oui, efface le menu et laisse le jeu ce jouer
    '''
    menu.presentation((100, 100), 2000, 2000)
    if menu.menu(): #la fonction menu contien une boucle tans qu'un bouton n'est pas apuiyé
        tk.efface_tout()
        #menu.present_text('Choisissez votre plateau ', (500, 200), 300, 100,'text')
        return menu.menu2()

def main_jeu():
    '''
    gère la boucle du jeu principal
    '''
    while True:
        tk.mise_a_jour()
        update_points()
        interaction_clavier()

def main():
    '''
    gère la logique du programe
    (logique du menu)
    '''

    a = attend_apui_bouton() # variable permettant d'afficher le type de plateau
    initialisation_jeu(a)
    main_jeu()


main()
