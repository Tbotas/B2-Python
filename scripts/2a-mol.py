#!/usr/bin/env python3

# title: 1d-mol
# description: Jeu du plus ou moins en tant que service en python
# date: 02/11/2018
# author: HAY Théo

from random import randrange
from time import sleep
import signal
import re


def printLose(sig, frame):
    print("Dommage :( La solution était " + str(solution))
    exit()


signal.signal(signal.SIGINT, printLose)


def convertInt(param):
    try:
        return int(param)
    except ValueError:
        return -1


def printWin():
    print("Bravo vous avez gagné !")
    exit()


def writeFile(text):
    """Fonction utile pour écrire dans un fichier
    """
    file = None
    try:
        file = open("repondre.txt", "w+")
    except PermissionError:
        sleep(0.5)
        writeFile(text)

    file.write(text)
    file.close()


def readFile():
    file = None
    try:
        file = open("repondre.txt", "r")
    except PermissionError:
        return None

    line = file.readline()
    nb = re.findall(r'\d+', line)
    file.close()

    if len(nb) == 1:
        return nb[0]

    return None


solution = randrange(0, 100)

writeFile('Veuillez entrer un nombre entre 0 et 100.')

while True:
    read = readFile()

    if read is None:
        sleep(0.5)
        continue

    read = convertInt(read)

    if read < 0 or read > 100:
        writeFile("Veuillez entrer un nombre entre 0 et 100")
        continue

    if read == solution:
        printWin()
    elif read < solution:
        writeFile("Plus grand !")
    else:
        writeFile("Plus petit !")
