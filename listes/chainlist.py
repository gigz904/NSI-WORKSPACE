def liste_vide():
    return None

def ajoute(lc, e):
    return (e, lc)

def valeur(lc):
    return lc[0]

def suite(lc):
    return lc[1]

def est_vide(lc):
    return lc is None

def copier(lc):
    if est_vide(lc):
        return None
    else:
        return(valeur(lc), copier(suite(lc)))

    return nl

def li_print(lc):
    li = lc
    while(est_vide(li) == False):
        val_li = valeur(li)
        print(str(val_li))
        li = suite(li)


a = liste_vide()

a = ajoute(a, 13)
a = ajoute(a, 94)
a = ajoute(a, 88)
a = ajoute(a, 78)

li_print(a)

n = copier(a)

li_print(n)