def liste_vide():
    return None

def ajoute(lc, e):
    return(e, lc)

def valeur(lc):
    return lc[0]

def suite(lc):
    return lc[1]

def est_vide(lc):
    return lc is None

def longueur(lc):
    li = lc
    c = 0
    while(est_vide(li) == False):
        c = c+1
        li = suite(li)
    return c

def li_print(lc):
    li = lc
    while(est_vide(li) == False):
        print(str(valeur(li)))
        li = suite(li)


a= liste_vide()

a= ajoute(a, 31)

a= ajoute(a, 32)

a= ajoute(a, 33)

a= ajoute(a, 31)

a= ajoute(a, 32)

a= ajoute(a, 33)


print(longueur(a))

