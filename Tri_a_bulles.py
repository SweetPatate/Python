# Ecrire une procédure réalisant le tri à bulles d’une liste de données numériques

def tri_a_bulles(liste):
    for j in range(len(liste)-1):
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    print(liste)

liste = [5,8,2,9,5]
liste = tri_a_bulles(liste)

# ou
def tri(liste):
    while max(liste) != liste[len(liste) - 1] or min(liste) != liste[0]:
        for i in range(len(liste)):
            if i != len(liste) - 1:
                if liste[i] > liste[i + 1]:
                    liste[i + 1], liste[i] = liste[i], liste[i + 1]
    print(liste)


liste = [1, 3, 6, 2, 4, 1, 2, 3, 4, 6, 2, 3, 2, 2, 1, 0]
tri(liste)

# ou encore
def tri(l):
    again = True
    while again:
        again = False
        for i in range(0, len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                again = True
    print(l)


liste = [12, 4, 8, -2, 1]
tri(liste)