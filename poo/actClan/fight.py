import clan as c
import warrior as w
import duel as d
import random as r 

def fight(c1:c.Clan, c2:c.Clan):

    while(len(c1.warriors_list) != 0 or len(c2.warriors_list)!= 0):
        w1 = c1.warriors_list[r.randint(0,len(c1)-1)]
        w2 = c2.warriors_list[r.randint(0,len(c2)-1)]
        win = d.duel(w1, w2)
        if(d.duel == w1):
            c2.warriors_list.remove(w2)
        else:
            c1.warriors_list.remove(w1)

    if(len(c1.warriors_list) == 0):
        print("LE CLAN" + c2.color + " GAGNE")
        return c2
    else:
        print("LE CLAN" + c1.color + " GAGNE")
        return c1