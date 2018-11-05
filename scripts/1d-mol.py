#!/usr/bin/env python3

# title: 1d-mol
# description: Jeu du plus ou moins en python
# date: 01/11/2018
# author: HAY Théo

from random import randrange
import signal

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

	
solution = randrange(0, 100)

print('Veuillez entrer un nombre entre 0 et 100. (q pour quitter)')

while True:
	read = input('')

	if read == "q":
		printLose(None, None)

	read = convertInt(read)
	
	if read < 0 or read > 100:
		print("Veuillez entrer un NOMBRE entre ZERO et CENT !")
		continue

	if read == solution:
		printWin()
	elif read < solution:
		print("Plus grand !")
	else:
		print("Plus petit !")
