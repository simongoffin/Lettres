# -*-coding:utf-8 -*
#!/usr/bin/python
import sys
import os
import time
import pickle

root = os.path.dirname(__file__)
rel_path = os.path.join("", "aima-python")
abs_path = os.path.join(root, rel_path)
sys.path.append(abs_path)
from search import *

class LettresProblem(Problem):


    def __init__(self,init,words):
        self.w=words
        self.dico={}
        self.symetrie=0
        self.solution=''
        goal=''
        Problem.__init__(self, init, goal)

    
    def goal_test(self, state):
        return False
            
    def successor(self, state):
        for valeur1 in state:
            temp=state[:]
            temp=temp[0:temp.index(valeur1)]+temp[temp.index(valeur1)+1:len(temp)]
            for valeur2 in temp:
                if len(valeur2)==1:
                    if not valeur1+valeur2 in self.dico:
                        self.dico[valeur1+valeur2]=1
                        check=possible(valeur1,valeur2,self.w)
                        self.symetrie+=1
                        if check[0]:
                            newmove=temp[:]
                            newmove=newmove[0:newmove.index(valeur2)]+newmove[newmove.index(valeur2)+1:len(newmove)]
                            newmove=newmove+(valeur1+valeur2,)
                            if check[1]>=len(self.solution):
                                self.solution=check[2]
                                print self.solution
                            etape=valeur1+' '+'+'+' '+valeur2+' '+'='+' '+valeur1+valeur2
                            yield (etape,newmove)
                        else: continue
                    
def possible(valeur1,valeur2,w):
    r=False
    for key, value in w.iteritems():   # iter on both keys and values
        if key.startswith(valeur1+valeur2):
            r=True
            break
    if r:
        if valeur1+valeur2 in w:
            MOT=valeur1+valeur2
            return [True,len(MOT),MOT]
        return [True,0,valeur1+valeur2]
    else:
        return [False,0,'']
        
def run(tuple,words):
    
    problem=LettresProblem(tuple,words)
    #example of bfs search
    debut=time.time()
    node=breadth_first_graph_search(problem)
    resultat=problem.solution
    fin=time.time()
    print fin-debut
    print problem.symetrie
    return resultat
    
    
if __name__ == "__main__":
    with open('DICO', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        words = mon_depickler.load()    
    tuple=('r','e','q','u','i','n','s','a')
    v=run(tuple,words)
    print v
    