import json
import warrior

class Clan:
    def __init__(self, color):
        self.color = color


        self.warriors_list = []

    def __str__(self) -> str:
        data = {"color" : self.color, "warriors_list" : str(self.warriors_list)}
        return json.dumps(data)
        pass

    def addWarrior(self, w):
        self.warriors_list.append(w)

    def __len__(self) -> int:
        return len(self.warriors_list)
    
    def __lt__(self, u):
        if len(self.warriors_list < u):
            return True
        else:
            return False
        
    def __contains__(self, x):
        if x in self.warriors_list:
            return True
        else:
            return False
        
    def __repr__(self):
        data = {"color" : self.color, "warriors_list" : str(self.warriors_list)}
        return json.dumps(data)
    
    def inFightWarriors(self):
        ifw = []

        for w in self.warriors_list:
            if w.inFight ==True:
                ifw.append(w)
        return ifw
    
    def outFightWarriors(self):
        ofw = []

        for w in self.warriors_list:
            if w.inFight ==False:
                ofw.append(w)
        return ofw
    
    
