import fltk as tk
import plateau as plat
from point import update_points
import menudujeu as menu
import sys
from affichage import Plateau

tk.cree_fenetre(1000, 800)

def switch_player(joueur):
    if joueur == 'b':
        return 'n'
    else:
        return 'b'

def coup(coord_clic,tour_joueur,plateau):
    plateau, coup_valide = plat.placer_pion(coord_clic, tour_joueur, plateau)
    if coup_valide:
        print('tour de', switch_player(tour_joueur))
    else:
        print('fils de pute mauvai truc')
    return plateau, coup_valide

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

def main_jeu(plateau,nb_pion):
    '''
    gère la boucle du jeu principal
    '''
    phase = 'placement pion'
    tour_joueur = 'n'
    pion_b_dispo = nb_pion
    pion_n_dispo = nb_pion
    while phase == 'placement pion':
        interaction_clavier()
        tk.mise_a_jour()

        coord_clic = update_points() #detecte click gauche sur position de pions
        if coord_clic != None:
            plateau, coup_valide = coup(coord_clic,tour_joueur,plateau)
            #metre -1 au nombre de pion et switch tour joueur
            if coup_valide and tour_joueur == 'n':
                pion_n_dispo += -1
                tour_joueur = switch_player(tour_joueur)
            elif coup_valide and tour_joueur == 'b':
                pion_b_dispo += -1
                tour_joueur = switch_player(tour_joueur)

        if pion_n_dispo == 0 and pion_b_dispo == 0:
            phase = 'deplacement pion'

def main():
    '''
    gère la logique du programe
    (logique du menu)
    '''

    dico_nb_pion = {
        1 : 9,
        2 : 12,
        3 : 6,
        4 : 3}

    plat = attend_apui_bouton() #type de plateau

    nombre_pion = dico_nb_pion[plat]

    plateau = initialisation_jeu(plat)
    main_jeu(plateau,nombre_pion)


main()
