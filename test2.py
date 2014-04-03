#!/usr/bin/python

import pickle
import time

with open('DICO', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    dico = mon_depickler.load()
    
debut=time.time()
if 'requin' in dico:
    fin=time.time()
    print fin-debut
    print 'requin'
    
    
debut=time.time()
result = [(key, value) for key, value in dico.iteritems() if key.startswith("requin")]
fin=time.time()
print fin-debut
print result

