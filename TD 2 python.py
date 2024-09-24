Exercice 3
Trace d'exécution
                    Ligne actuel    Ligne suivante  i   resultat
                    1               2               -       0
                    2               3               1       0
                    3               2               1       3
                    2               3               2       3
                    3               2               2       6
                    2               3               3       6
                    3               2               3       9
                    2               3               4       9
                    3               2               4       12
                    2               3               5       12
                    3               2               5       15
                    2               4               6       15
                    4               -               6       15

Exercice 4
suffrage=100000
siege=25
quotient=suffrage/siege
voix_a=73000
siege_a=voix_a//quotient
voix_b=suffrage-voix_a
siege_b=voix_b//quotient


if siege_a+siege_b!=siege:
    if (voix_a/quotient)-siege_a>(voix_b/quotient)-siege_b:
        siege_a=siege_a+1
        if siege_a>siege_b:
            print("La liste A est en tête avec",siege_a,"voix contre",siege_b,"voix pour la liste B"  )
        else :
            print("La liste B est en tête avec",siege_b,"voix contre",siege_a,"voix pour la liste A"  )
    else :
        siege_b=siege_b+1
        if siege_a>siege_b:
            print("La liste A est en tête avec",siege_a,"voix contre",siege_b,"voix pour la liste B"  )
        else:
            print("La liste B est en tête avec",siege_b,"voix contre",siege_a,"voix pour la liste A"  )
else :
    if siege_a>siege_b:
        print("La liste A est en tête avec",siege_a,"voix contre",siege_b,"voix pour la liste B"  )
    else :
        print("La liste B est en tête avec",siege_b,"voix contre",siege_a,"voix pour la liste A"  )


Exercice 5

print("hello")
print(7)
x=(7,"hello")
print(x)

Exerice 6

for i in range (1,51):
    print(i)

i=0
while i!=51:
     print(i)
     i=i+1

i=50
while i>0:
    if i==1:
        print ("Il reste",i,"seconde")
        i=i-1
    else :
        print("Il reste",i,"secondes")
        i=i-1
print("Boom")


Exercice 7

n=25
print("*"*n)

OU 

a=""
for i in range(0,15):
    a=a+"*"
print(a)

Exercice 8

n=5
while n>0 :
    print("*")
    n=n-1

Exercice 9

