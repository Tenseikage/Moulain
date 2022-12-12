import fltk as tk
from random import choice




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
    Menu de jeu
    """
    buttonjouer = Button(500, 500, 250, 75, 'jouer.gif', 'jouer')
    buttonquitter = Button(500, 600, 250, 75, 'quitter.gif', 'quitter')
    buttonjouer.create_button()
    buttonquitter.create_button()
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
                return False
    tk.ferme_fenetre()

def presentation(centre,taille_x,taille_y): # centre : position centrale du rectangle
    '''Cette fonction permet d'avoir un menu du jeu''' # creation de la fenêtre
    colors = ['blue','yellow' , 'pink', 'purple','cyan']
    tk.rectangle(centre[0]-taille_x,centre[1]-taille_y,centre[0]+taille_x,centre[1]+taille_y,couleur= choice(colors), remplissage = choice(colors) ,
    	      tag = 'Rectangle')
    present_text('Jeu du moulin ', (500, 200), 300, 100)


def present_text(string,centre,taille_x,taille_y):
        a= centre[0]-taille_x
        b= centre[1]-taille_y
        c = centre[0]+taille_x
        d = centre[1]+taille_y
        tk.texte(a+(c-a)//2,b+(d-b)//2,chaine=string,taille=60,couleur= 'black', ancrage='center',
    	      tag = 'text')
        
        




