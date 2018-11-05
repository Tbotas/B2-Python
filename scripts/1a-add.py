#!/usr/bin/env python3

# title: 1a-add
# description: Ajoute deux nombres
# date: 15/10/2018
# author: HAY Théo



def convertInt(param):
    try:
        return int(param)
    except ValueError:
        print("Vous n'avez pas entré un nombre !")
        exit() 

nb1 = convertInt(input('Veuillez entrer le premier nombre.\n'))
nb2 = convertInt(input('Veuillez entrer le second nombre.\n'))

print("Voilà l'addition de vos nombres : " + str(nb1 + nb2))



