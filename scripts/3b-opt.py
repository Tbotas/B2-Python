#!/usr/bin/env python3
# 3b-opt.py
# Script de sauvegarde
# PALLARD, HAY
# 11/11/2018


# Tous les imports
import shutil
import gzip
import os
import sys
import signal
import argparse
from functools import partial

# Fonction pour supprimer l'archive créée
def delArchive(completePath):
    if os.path.exists(completePath):
        os.remove(completePath)


# Fonction anti ctrl c
def quitterScript(completePath, sig, frame):
    delArchive(completePath)
    sys.exit(0)

def printError(msg):
    sys.stderr.write(msg)

def addArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Dossier de destination', required=True)
    parser.add_argument('-i', '--input', nargs='+', help='Dossier(s) a archiver', required=True)
    return parser.parse_args()

def verifyArg(arg, readOnly):
    droits = os.R_OK and (0 if readOnly else os.W_OK)

    if not os.access(arg, droits):
        printError("ERREUR: Pas les droits de lecture ou d'écriture sur {0}".format(arg))
        return False
    
    if not os.path.exists(arg):
        printError("ERREUR: Le dossier {0} n'existe pas !".format(arg))
        return False

    return True
        
def addSlashToEndOfArg(arg):
    return arg if arg[-1:] == '/' else arg + '/'


def archiveAndCopyToDest(archiveName, baseDir):
    shutil.make_archive(archive, 'gztar', destination) 

args = addArguments()

args.output = addSlashToEndOfArg(args.output)

if not verifyArg(args.output, False):
    printError("Erreur sur le dossier d'écriture, au revoir :)")

destination = args.output

archiveName = 'testArchive'
completePath = destination + archiveName + '.tar.gz'

signal.signal(signal.SIGINT, partial(quitterScript, completePath))

for arg in args.input:
    arg = addSlashToEndOfArg(arg)
    if verifyArg(arg, True):
        archiveAndCopyToDest(archiveName, arg)