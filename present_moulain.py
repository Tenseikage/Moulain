from fltk import *
from menudujeu import*


cree_fenetre(1000,800)

def presentation(centre,taille_x,taille_y): # centre : position centrale du rectangle
    '''Cette fonction permet d'avoir un menue avant que le jeu ne se lance''' # creation de la fenêtre
    rectangle(centre[0]-taille_x,centre[1]-taille_y,centre[0]+taille_x,centre[1]+taille_y,couleur= 'blue', remplissage = 'blue',
    	      tag = 'Rectangle')
    
def present_text(string,centre,taille_x,taille_y):
        a= centre[0]-taille_x
        b= centre[1]-taille_y
        c = centre[0]+taille_x
        d = centre[1]+taille_y
        texte(a+(c-a)//2,b+(d-b)//2,chaine=string,taille=50,couleur= 'black', ancrage='center',
    	      tag = 'text')
        
        

presentation((500,200),300,100)
present_text('Jeu du moulin ',(500,200),300,100)
menu(Button(500, 600, 250, 75, 'jouer.gif', 'jouer'),Button(500, 500, 250, 75, 'quitter.gif', 'quitter'))


