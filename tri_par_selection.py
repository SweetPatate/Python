# Ecrire une procédure réalisant le tri par sélection d’une liste de données numériques

def tri_selection(l):
    for i in range(len(l)-1):
        indice_min=i
        for j in range(i+1, len(l)):
            if l[j] < l[indice_min]:
                indice_min=j
            l[i], l[indice_min]=l[indice_min], l[i]
    return l

maListe = [i for i in range(20, 0, -1)]
print(maListe)
tri_selection(maListe)
print(maListe)