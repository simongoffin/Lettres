# -*-coding:utf-8 -*
#!/usr/bin/python
import sys
import os
import time
import sqlite3

root = os.path.dirname(__file__)
rel_path = os.path.join("", "aima-python")
abs_path = os.path.join(root, rel_path)
sys.path.append(abs_path)
from search import *

class LettresProblem(Problem):


    def __init__(self,init,connexion):
        self.conn=connexion
        self.c = self.conn.cursor()
        self.dico={}
        self.symetrie=0
        self.solution=['']
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
                        check=possible(valeur1,valeur2,self.c)
                        self.symetrie+=1
                        if check[0]:
                            newmove=temp[:]
                            newmove=newmove[0:newmove.index(valeur2)]+newmove[newmove.index(valeur2)+1:len(newmove)]
                            newmove=newmove+(valeur1+valeur2,)
                            if check[1]>len(self.solution[0]):
                                self.solution=[]
                                self.solution.append(check[2])
                            elif check[1]==len(self.solution[0]):
                                self.solution.append(check[2])
                            etape=valeur1+' '+'+'+' '+valeur2+' '+'='+' '+valeur1+valeur2
                            yield (etape,newmove)
                        else: continue
                    
def possible(valeur1,valeur2,c):
    c.execute("SELECT * FROM Mots where Mot like "+"\'"+valeur1+valeur2+"%"+"\'"+" LIMIT 1;")
    r=c.fetchall()
    if len(r)>0:
        c.execute("SELECT * FROM Mots where Mot like "+"\'"+valeur1+valeur2+"\'"+";")
        mot=c.fetchall()
        if len(mot)>0:
            MOT=valeur1+valeur2
            return [True,len(MOT),MOT]
        return [True,-1,valeur1+valeur2]
    else:
        return [False,-1,'']
        
def run(tuple,connexion):
    
    problem=LettresProblem(tuple,connexion)
    #example of bfs search
    #debut=time.time()
    node=breadth_first_graph_search(problem)
    resultat=problem.solution
    #fin=time.time()
    #print fin-debut
    problem.conn.commit()
    problem.c.close()
    return resultat
    
    
if __name__ == "__main__":    
    tuple=('v','o','e','u','n','b','e','t','l')
    connexion = sqlite3.connect('dico.db')
    v=run(tuple,connexion)
    print v
    