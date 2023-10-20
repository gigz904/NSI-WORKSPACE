import clan as c
import warrior as w
import fight as f
import duel as d

clan1 = c.Clan('blue')

clan1.addWarrior(w.Warrior('Dussopt'))
clan1.addWarrior(w.Warrior('Borne'))
clan1.addWarrior(w.Warrior('Darmanin'))

clan2 = c.Clan('red')

clan2.addWarrior(w.Warrior('Ruffin'))
clan2.addWarrior(w.Warrior('Boyard'))
clan2.addWarrior(w.Warrior('Martinez'))

print(clan1)

print(clan2)

f.fight(clan1, clan2)