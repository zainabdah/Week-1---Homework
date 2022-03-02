def PGCD(n,m):
    reste=1
    while reste!=0:
        grand=max(n,m)
        petit=min(n,m)
        quotient=grand//petit
        reste=grand%petit
        n=petit
        m=reste
    return petit

n=int(input("entrer le premier nombre : "))
m=int(input("entrer le deuxieme nombre : "))
print(PGCD(n,m))