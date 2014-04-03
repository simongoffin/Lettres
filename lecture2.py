#!/usr/bin/python

import pickle

f = open('Dictionnaire.txt','r')
lignes  = f.readlines()
f.close()

dico={}

doublons=set(lignes)
for ligne in doublons:
    taille=len(ligne)
    if taille<=10:
        ligne=ligne[0:taille-1]
        dico[ligne]=1
        

with open('DICO', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(dico)