import json

class Warrior():
    def __init__(self, name) -> None:
        self.name = name
        self.inFight = True
        self.force = 1
        self.life_capital = 10
        pass

    def __repr__(self):
        data = {"name" : self.name, "inFight": self.inFight, "force": self.force, "life_capital" : self.life_capital}
        return json.dumps(data)
        
