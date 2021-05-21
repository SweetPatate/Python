def occurrence(texte):
    x = 0
    alphab = "abcdefghijklmnopqrstuvwxyz" # alphabet
    mondico = dict.fromkeys(alphab,0) #
    texte = texte.lower() # affiche le texte sans majuscules

    for i in range(len(texte)): # on parcoure le texte
        if texte[i] in mondico: # si un element du texte est dans mondico
            mondico.update({texte[i]:mondico.get(texte[i])+1})
    for i in range(len(alphab)):
        if mondico[alphab[i]] == 0:
            del mondico[alphab[i]]
            x = 1
    if x == 1:
        print("Ce n'est pas un pangramme")
    else:
        print("C'est un pangramme")
    print(mondico)

print("Un pangramme est une phrase comportant toutes les lettres de l'alphabet.")
#texte = "azertyuiopqsdfghjklmwxcvbn"
texte = input("Insérer votre phrase :")
occurrence(texte)