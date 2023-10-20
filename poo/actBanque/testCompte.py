import compte as c


comptes = []

for i in range(9):
    comptes.append(c.Compte())

for co in range(len(comptes)):
    comptes[co].credit(200 + (100*co))

for co in range(len(comptes)):
    for i in range(co+1, len(comptes)):
        comptes[co].virement(comptes[i], 20)

for co in comptes:
    print(co)
    