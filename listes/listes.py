class Cellule:
    def __init__(self, valeur, suivant):
        self._valeur = valeur
        self._suivant = suivant

    

class Liste:
    def __init__(self, c):
        self.cellule = c

    def valeur(self):
        return self.cellule._valeur

    def suite(self):
        return Liste(self.cellule._suivant)

    def est_vide(self):
        if self.cellule == None:
            return True
        else:
            return False

    def ajouter(self, a):
        self.cellule = Cellule(a, self.cellule)

    def longueur(self):
        if est_vide():
            return 0
        else:
            return 1 + self.suite.longueur()

    def __repr__(self):
        
        liste = self
        l = ""
        
        while(liste.est_vide() == False):
            l = l +  str(liste.valeur()) +";"
            liste = liste.suite()

        return l

    def inverse(self):
        liste = self
        l = Liste(Cellule(None, None))
        while(liste.est_vide() == False):
            if(liste.suite() != None and liste.valeur() != None ):
                l.ajouter(liste.valeur())
            liste = liste.suite()
        return l


        
    

li = Liste(Cellule(1,None))
li.ajouter(48)
li.ajouter(45)
li.ajouter(59)
li.ajouter(7)
li.ajouter(36)
li.ajouter(91)
print(li.inverse())


