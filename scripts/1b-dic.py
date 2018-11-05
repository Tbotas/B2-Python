#!/usr/bin/env python3

# title: 1b-dic
# description: Listes 101
# date: 15/10/2018
# author: HAY Théo

noms = []

read = input('Veuillez entrer des prénoms, 1 par ligne.\n')

while read != "q":
    noms.append(read)
    read = input('')

print(sorted(noms, key=str.lower))