def diviseurs(n):
    diviseurs=[]
    for i in range (1,n+1):
        if n%i==0:
            diviseurs.append(i)
    return diviseurs

n=int(input("entrer le nombre : "))
print(diviseurs(n))
