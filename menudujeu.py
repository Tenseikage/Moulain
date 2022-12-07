import fltk as tk

tk.cree_fenetre(400,400)


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
        return self.coordxplace - self.xtaille / 2, self.coordyplace - self.ytaille / 2


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
            self.xtaille()[0] and self.get_coords()[1] < y <
            self.get_coords()[1] + self.ytaille()[1]):
            return True


def menu():
    """
    Menu de jeu
    """
    buttonjouer = Button(400, 200, 250, 75, 'jouer.gif', 'jouer')
    buttonquitter = Button(400, 275, 250, 75, 'quitter.gif', 'quitter')
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
            if buttonjouer.is_touched((coords_clickx, coords_clicky)):
            # Regarde si le clique à été effectué sur le bouton jouer
                buttonjouer.destroy_button()
                buttonquitter.destroy_button()
                return True
            if buttonquitter.is_touched():
            # Regarde si le bouton quitter a été appuyé
                tk.ferme_fenetre()


buttonjouer = Button(400, 200, 250, 75, 'jouer.gif', 'jouer')
buttonjouer.create_button()
tk.attend_ev()
tk.ferme_fenetre()