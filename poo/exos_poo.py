from random import *
import pygame

class Escargot:
    def __init__ (self, c):
        self.couleur = c
        self.position = 0
        self.vitesse = 1

    def etat(self):
        return ('position : ' + str(self.position)) + (' ; vitesse : ' + str(self.vitesse))
    
    def avance(self, pas):
        self.position = self.position + pas

bob = Escargot('red')
henry = Escargot('blue')

bob.vitesse = 20
henry.vitesse = 10

finish= False
winner=None
while(finish==False):
    bob.avance(randint(1,10))
    henry.avance(randint(1,10))
    
    print("BOB ", bob.etat())
    print("HENRY ", henry.etat())
    if bob.position >= 200:
        winner = bob
        finish=True
    elif henry.position >=200:
        winner = henry
        finish=True

print("WINNER : ", winner.couleur)

