#!/usr/bin/env python3

# title: 1c-moy
# description: Affiche la moyenne et le top 5 d'un dictionnaire de noms et notes
# date: 15/10/2018
# author: HAY Théo

import operator

def convertInt(param):
    try:
        return int(param)
    except ValueError:
        return -1

dico = {}

print('Veuillez entrer un prénom et une note (séparés par un espace).')

while True:
    read = input('')

    if read == "q":
        break

    read = str(read).split(' ')

    if len(read) < 2:
        print("Je vous ai dit de mettre un espace !")
        continue

    nom = read[0]
    note = convertInt(read[1])
    
    if note == -1:
        print("Êtes-vous sûr d'avoir entré un nombre ?")
        continue

    if nom in dico:
        print("Vous avez déjà mis une note pour " + nom)
        continue

    dico[nom] = note

moyenne = sum(dico.values()) / float(len(dico)) # Calcul la moyenne ( somme sur les valeurs du dico et divise pas le nombre d'entrées dans le dico

print("Moyenne: " + str(moyenne))
print(sorted(dico.items(), key=operator.itemgetter(1), reverse = True)[:5]) # Trie le dictionnaire par ses valeurs, dans l'ordre décroissant, puis coupe les 5 premières valeurs



