import math

class Angle():
    def __init__(self, m):
        self.m = m

    def __str__(self):
        return(str(self.m) +' degrés')
    
    def ajoute(self, a):
        self.m = self.m + a.m
    
    def sin(self):
        return math.sin(self.m)
    
    def cos(self):
        return math.cos(self.m)