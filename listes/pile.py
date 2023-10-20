class Pile:
       def __init__(self, valeur=None, pile=None):
              self._tableau = [None]*taille_max
              self._sommet = 0

       def empiler(self, valeur):
              self._sommet += 1
              self._tableau[self._sommet] = valeur
       def depiler(self):
              valeur = self._tableau[self._sommet]
              self._sommet -= 1
              return valeur
       def est_vide(pile):
              return pile._sommet == 0
       

p1 = Pile(2, 3)

p1.empiler(654)
p1.empiler(65)
p1.empiler(6)



while (Pile.est_vide(p1) == False):
       print(p1._sommet)
       p1.depiler()