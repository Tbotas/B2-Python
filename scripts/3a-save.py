#!/usr/bin/env python3
# 3a-save.py
# Script de sauvegarde
# PALLARD, HAY
# 09/11/2018

# Tous les imports
import shutil
import gzip
import os
import sys
import signal

# Fonction créer une archive
def creerArchive(archiveName, destData, baseDir):
    shutil.make_archive(archiveName, 'gztar', destData, baseDir)

# Fonction pour supprimer l'archive créée
def delArchive(completePath):
    if os.path.exists(completePath):
        os.remove(completePath)


# Fonction anti ctrl c
def quitterScript(sig, frame):
    delArchive()
    sys.exit(0)


signal.signal(signal.SIGINT, quitterScript)

destData = './data'
archive = 'testArchivage'
baseDir = './TestArchivage'

# Créer le dossier data s'il n'existe pas
if not os.path.exists('./data/'):
    os.makedirs('./data')

# Vérifier qu'on ai les droits
if os.access(destData, os.R_OK and os.W_OK):
    if os.path.exists(baseDir):
        # Si une archive existe déjà, les comparer
        # Si elles sont identiques, quitter, sinon remplacer l'ancienne
        if os.path.exists('{0}/{1}.tar.gz'.format(destData, archive)):
            delArchive('{0}/{1}.tar.gz'.format(destData, archive))
            sys.stderr.write('L\'archive existe déjà.\n')
            creerArchive(archive, destData, baseDir)
            sys.stderr.write('Sauvegarde effectuée\n')
        else:
            creerArchive(archive, destData, baseDir)
            sys.stderr.write('Sauvegarde effectuée\n')
    else:
        sys.stderr.write("Le dossier à archiver n'existe pas.")
else:
    sys.stderr.write('Vous n\'avez pas les droits sur le répertoire data\n')