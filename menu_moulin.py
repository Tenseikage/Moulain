from fltk import *
from menudujeu import*
from random import *


def presentation(centre,taille_x,taille_y): # centre : position centrale du rectangle
    '''Cette fonction permet d'avoir un menue avant que le jeu ne se lance''' # creation de la fenêtre
    colors = ['blue','yellow' , 'pink', 'purple','cyan']
    rectangle(centre[0]-taille_x,centre[1]-taille_y,centre[0]+taille_x,centre[1]+taille_y,couleur= choice(colors), remplissage = choice(colors) ,
    	      tag = 'Rectangle')
    
def present_text(string,centre,taille_x,taille_y):
        a= centre[0]-taille_x
        b= centre[1]-taille_y
        c = centre[0]+taille_x
        d = centre[1]+taille_y
        texte(a+(c-a)//2,b+(d-b)//2,chaine=string,taille=60,couleur= 'black', ancrage='center',
    	      tag = 'text')
