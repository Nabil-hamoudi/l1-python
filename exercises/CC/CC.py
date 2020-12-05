def carre_decroissant(n):
    a = []
    for i in range(1, n+1):
        temp = list(range(n+1-i, 2*n-1*i+1))
        a.append(temp)
    return a

print(carre_decroissant(10))