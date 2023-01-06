import fltk as tk
import plateau as plat
from point import update_points
import menudujeu as menu
import sys
from affichage import Plateau

tk.cree_fenetre(1000, 800)

def switch_player(joueur):
    tk.efface('joueur')
    if joueur == 'b':
        tk.texte(730, 65, 'Noir', couleur='black', ancrage='nw', police='Helvetica', taille=20, tag='joueur')
        return 'n'
    else:
        tk.texte(730, 65, 'Blanc', couleur='black', ancrage='nw', police='Helvetica', taille=20, tag='joueur')
        return 'b'

def coup(coord_clic,joueur,plateau):
    plateau, coup_valide = plat.placer_pion(coord_clic, joueur, plateau)
    if coup_valide:
        nv_joueur = switch_player(joueur)
        print('tour de', nv_joueur)
    else:
        print('fils de pute mauvai truc')
        nv_joueur = joueur
    return plateau, coup_valide, nv_joueur

def attendre_enlever_pion(plateau,joueur_a_enlever_pion):
    if joueur_a_enlever_pion == 'b':
        joueur = 'blanc'
    else:
        joueur = 'noir'
    tk.texte(730, 90, 'Enlever un pion '+joueur, couleur='red', ancrage='nw', police='Helvetica', taille=20, tag='pion_remove')

    pion_adverse_non_enleve = True
    while pion_adverse_non_enleve:
        interaction_clavier()
        tk.mise_a_jour()

        clic = update_points()
        if clic != None:
            x, y = clic
            if plateau[x][y].state == joueur_a_enlever_pion:
                plat.enlever_pion(clic,plateau)
                pion_adverse_non_enleve = False
    tk.efface('pion_remove')

def attendre_deplacement_de_pion(deplace,plateau,selected,type_plat):
    while deplace:
            interaction_clavier()
            tk.mise_a_jour()

            clic = update_points()
            if clic != None:
                if plat.deplacer_pion(clic, selected, plateau,type_plat):
                    plateau[clic[0]][clic[1]].selected = False
                    plateau[selected[0]][selected[1]].selected = False
                    deplace = not deplace
                else:
                    clic = None
    return deplace, plateau      


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
    tk.rectangle(700, 0, 1000, 1000, '', '#cccccc', 2, 'background')
    tk.rectangle(0, 600, 1000, 1000, '', '#bbbbbb', 2, 'background')
    tk.texte(730, 65, 'Noir', couleur='black', ancrage='nw', police='Helvetica', taille=20, tag='joueur')

    tk.texte(730, 30, 'Tour du joueur :', couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='background')

    plate = Plateau((350,300),80,type_plat,False)
    plate.affiche_animation()
    plateau = plat.creer_liste(type_plat)
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

def main_jeu(plateau,nb_pion,type_plat):
    '''
    gère la boucle du jeu principal
    '''
    phase = 'placement pion'
    tour_joueur = 'n'
    pion_b_dispo = nb_pion
    pion_n_dispo = nb_pion
    nb_moulins = 0
    deplace = False
    while phase == 'placement pion':
        interaction_clavier()
        tk.mise_a_jour()

        coord_clic = update_points() #detecte click gauche sur position de pions
        if coord_clic != None:
            ancient_joueur = tour_joueur
            plateau, coup_valide, tour_joueur = coup(coord_clic,tour_joueur,plateau)
            #metre -1 au nombre de pion et switch tour joueur
            if coup_valide and ancient_joueur == 'n':
                pion_n_dispo += -1
            elif coup_valide and ancient_joueur == 'b':
                pion_b_dispo += -1
            nb_ancien_moulins = nb_moulins
            nb_moulins = plat.moulin(plateau,type_plat)
            if nb_moulins - nb_ancien_moulins > 0:
                attendre_enlever_pion(plateau,tour_joueur)

        if pion_n_dispo == 0 and pion_b_dispo == 0:
            phase = 'deplacement pion'








    while phase == 'deplacement pion':
        interaction_clavier()
        tk.mise_a_jour()

        clic = update_points()
        if clic != None:
            if not plat.verif_place(clic,plateau):
                selected = clic
                deplace = not deplace
                plateau[clic[0]][clic[1]].selected = True
                deplace , plateau = attendre_deplacement_de_pion(deplace,plateau,selected,type_plat)
      

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
    main_jeu(plateau,nombre_pion,plat)


main()
