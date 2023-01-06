import fltk as tk
from random import choice, randint
import affichage as aff
import sys
from point import Point



class Button:
    """
    Classe permettant de gérer les boutons
    """

    def __init__(self, coordxplace, coordyplace, xtaille, ytaille, image_button, tag):
        self.coordxplace = coordxplace
        self.coordyplace = coordyplace
        self.xtaille = xtaille
        self.ytaille = ytaille
        self.image_button = image_button
        self.tag = tag


    def get_coordsplace(self):
        """
        Retourne les coordonnées x (abcisses) et y (ordonée) de là où est placé le bouton
        """
        return self.coordxplace, self.coordyplace


    def get_coords(self):
        """
        Renvoie les coordonnées x et y minimale du bouton
        """
        return self.coordxplace - self.xtaille // 2, self.coordyplace - self.ytaille // 2


    def get_taille(self):
        """
        Renvoie la taille de l'image
        """
        return self.xtaille, self.ytaille


    def create_button(self):
        """
        Créer le button à partir d'une image avec pour point d'ancrage le milieu
        """
        tk.image(self.coordxplace, self.coordyplace, self.image_button, 'center', self.tag)


    def destroy_button(self):
        """
        Efface le bouton
        """
        tk.efface(self.tag)

    
    def is_touched(self, coords):
        """
        Vérifie si le boutton est cliqué
        
        """
        x, y = coords
        if (self.get_coords()[0] < x < self.get_coords()[0] +
            self.xtaille and self.get_coords()[1] < y <
            self.get_coords()[1] + self.ytaille):
            return True


def menu():
    """
    Menu de jeu avec création des boutons jouer et quitter 
    et gestion des évènements des souris lors du clic sur un des boutons
    """
    buttonjouer = Button(500, 500, 250, 75, 'images_jeu/jouer.gif', 'jouer')
    buttonquitter = Button(500, 600, 250, 75, 'images_jeu/quitter.gif', 'quitter')
    buttonjouer.create_button() # creation du bouton jouer
    buttonquitter.create_button() # creration du bouton quitter
    tk.mise_a_jour()
    choosing_event = True
    while choosing_event:
        event = tk.donne_ev()
        tev = tk.type_ev(event)
        tk.mise_a_jour()
        if tev == "ClicGauche": # Regarde si le clique gauche a été apuuyé
            coords_clickx, coords_clicky = tk.abscisse(event), tk.ordonnee(event)
            if buttonjouer.is_touched((coords_clickx,coords_clicky)):
            # Regarde si le clique à été effectué sur le bouton jouer
                buttonjouer.destroy_button()
                buttonquitter.destroy_button()
                return True
            if buttonquitter.is_touched((coords_clickx,coords_clicky)):
            # Regarde si le bouton quitter a été appuyé
                buttonjouer.destroy_button()
                buttonquitter.destroy_button()
                sys.exit()
    tk.ferme_fenetre()

def menu2():
    """
    Menu du jeu avec ajout d'un fond pour le plateau et 
    de boutons pour permettre au joueur de choisir le jeu
    """
    tk.rectangle(0, 0, 1000, 1000, '', '#eee2b0', 0, 'background')
    present_text('Choisissez un plateau ', (500, 200), 300, 400,60)
    buttonred = []
    variante = [9,12,6,3]
    for i in range(4):
        button = Button(140 + 240*i, 500, 201, 201, 'images_jeu/red.png', 'red')
        button.create_button()
        buttonred.append(button)
        plat = aff.Plateau((140+240*i,500), 28, i+1, True)
        plat.affiche_animation()
        present_text(f'Variante à \n {variante[i]} pions', (150+240*i, 650), 200, 100,20)
    present_text(f'(Saut quelconque)', (150+240*3, 720), 200, 100,20)                         
    tk.mise_a_jour()
    choosing_event = True
    while choosing_event:
        event = tk.donne_ev()
        tev = tk.type_ev(event)
        tk.mise_a_jour()
        if tev == "ClicGauche": # Regarde si le clique gauche a été apuuyé
            coords_clickx, coords_clicky = tk.abscisse(event), tk.ordonnee(event)
            if buttonred[0].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                return 1
            if buttonred[1].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                return 2
            if buttonred[2].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                return 3
            if buttonred[3].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                return 4
    tk.ferme_fenetre()
    


def presentation(centre,taille_x,taille_y): # centre : position centrale du rectangle
    '''Cette fonction permet d'avoir un menu du jeu''' # creation de la fenêtre
    colors = ['blue','yellow' , 'pink', 'purple','cyan']
    tk.rectangle(centre[0]-taille_x,centre[1]-taille_y,centre[0]+taille_x,centre[1]+taille_y,couleur= choice(colors), remplissage = choice(colors) ,
    	      tag = 'Rectangle')
    present_text('Jeu du moulin  ', (500, 200), 300, 100,60)
    present_text('(version oreo)',(500,300),200,135,20)
    tk.image(200,228,'images_jeu/oreo_n.png')
    tk.image(785,206,'images_jeu/oreo_b.png')
    


def present_text(string,centre,taille_x,taille_y,police):
        """Cette fonction permet de cadrer le texte de présentation"""
        a= centre[0]-taille_x
        b= centre[1]-taille_y
        c = centre[0]+taille_x
        d = centre[1]+taille_y
        tk.texte(a+(c-a)//2,b+(d-b)//2,chaine=string,taille=police,couleur= 'black', ancrage='center',
    	      tag = 'text')
        
def game_background():
    tk.rectangle(0, 0, 1000, 1000, '','#999999', 0, 'background')
    tk.rectangle(700, 0, 1000, 1000, '', '#cccccc', 2, 'background')
    tk.rectangle(0, 600, 1000, 1000, '', '#bbbbbb', 2, 'background')
    tk.texte(730, 65, 'Noir', couleur='black', ancrage='nw', police='Helvetica', taille=20, tag='joueur')
    tk.texte(730, 30, 'Tour du joueur :', couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='background')
    tk.texte(20, 630, 'Phase :', couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='background')
    tk.texte(137, 630, 'placez vos pions', couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='phase') 


def fin(gagnan):
    tk.efface_tout()
    Point.liste_objet = []
    tk.rectangle(0, 0, 1000, 1000, '', '#00aa00', 2, 'background')
    if gagnan == 'b':
        gagnan = 'blanc'
    else:
        gagnan = 'noir'
    present_text('Bravo!, les pions ' + gagnan +' ont gagné !',(500,300),100,100,40)
    return menu()



