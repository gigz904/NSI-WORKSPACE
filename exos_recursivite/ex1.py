def puissance(x, n):

    if n==0:
        return 1
    else:
        return x*puissance(x, n-1)

def produit(m,n):

    if(n==0):
        return 0
    else:
        return m + produit(m, n-1)
print(produit(2, 4))