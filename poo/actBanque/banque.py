import compte as c

class Banque():
    def __init__(self) -> None:
        self.comptes = []

    def getCompteByNom(self, nom) -> c.Compte:
        for c in self.comptes:
            if c.nom == nom:
                return c
            
    def createCompte(self, nom):
        self.comptes.append(c.Compte(nom))
            
    def getTab(self):
        gTab = []
        for c in self.comptes:
            cTab = [c.nom, str(c._sold)]
            gTab.append(cTab)
        return gTab

    