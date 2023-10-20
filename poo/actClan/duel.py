import clan as c
import warrior as w
import random as r

def hit(hitter:w.Warrior, victim:w.Warrior):
    hitter.force = r.randint(1,3)
    #print(hitter.name + " TAPE " + str(victim.name) + " QUI A " + str(victim.life_capital) + " VIES AVEC UNE FORCE DE " + str(hitter.force))
    victim.life_capital = victim.life_capital - hitter.force

def round(w1:w.Warrior, w2:w.Warrior) -> w.Warrior:
    w1.life_capital = 10
    w2.life_capital = 10
    while(w1.life_capital >= 0 and w2.life_capital>= 0):
            if(r.randint(1,2) == 1):
                hit(w1, w2)
            else:
                hit(w2, w1)
    
    if(w1.life_capital<0):
         print (w2.name + " GAGNE")
         return w2
    
    if(w2.life_capital<0):
         print(w1.name + " GAGNE")
         return w1


def duel(w1:w.Warrior, w2:w.Warrior) -> w.Warrior:


        print("DUEL " + w1.name + " VS " + w2.name)
        

        if(r.randint(1,2) == 1):
            hit(w1, w2)
        else:
            hit(w2, w1)

        winners = []
        
        while(len(winners) != 3):
            winners.append(round(w1,w2))


        if(winners.count(w1) > winners.count(w2)):
            print(w1.name + " GAGNE LE DUEL")
            return w1
        else:
            print(w2.name + " GAGNE LE DUEL")
            return w2

        
