# classe Compte
class Compte:
    def __init__(self, nom):
        self.nom = nom
        self._sold = 0

    def credit(self,montant):
        self._sold = self._sold + montant

    def debit(self,montant):
        self._sold = self._sold - montant

    def virement(self, cible, montant):
        cible.credit(montant)
        self.debit(montant)

    def getSold(self):
        return self._sold

    def __str__(self):
        return("SOLDE DE "+ self.nom + ": " + str(self.getSold()))

