def occurrence(texte):
    alphab = "abcdefghijklmnopqrstuvwxyz" # alphabet
    mondico = dict.fromkeys(alphab,0) # mondico import l'alphabet et lui attribut la valeur 0 pour chaque caractére
    texte = texte.lower() # affiche le texte sans majuscules

    for i in range(len(texte)): # on parcoure le texte
        if texte[i] in mondico: # si un element du texte est dans mondico
            mondico.update({texte[i]:mondico.get(texte[i])+1})
    for i in range(len(alphab)): # on parcoure l'alphabet
        if mondico[alphab[i]] == 0:
            del mondico[alphab[i]]
    print(mondico)

texte = "Il fait beau ce matin"
print(texte)
occurrence(texte)