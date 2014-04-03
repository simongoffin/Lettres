#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from Tkinter import *
from core import *
import random


def calcul():
    arg1=ent1.get()
    arg2=ent2.get()
    arg3=ent3.get()
    arg4=ent4.get()
    arg5=ent5.get()
    arg6=ent6.get()
    arg7=ent7.get()
    arg8=ent8.get()
    arg9=ent9.get()
    tuple=(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9)
    connexion = sqlite3.connect('dico.db')
    v=run(tuple,connexion)
    if len(v)<5:
        for i in range(len(v),5):
            v.append('')
    affichage1['text'] = v[0]
    affichage2['text'] = v[1]
    affichage3['text'] = v[2]
    affichage4['text'] = v[3]
    affichage5['text'] = v[4]
    
def aleatoire():
    lettres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    voyelles=['a','e','i','o','u','y']
    consonnes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    ent1.delete(0,END)
    arg1=ent1.insert(0,lettres[random.randrange(0,26)])
    ent2.delete(0,END)
    arg2=ent2.insert(0,voyelles[random.randrange(0,6)])
    ent3.delete(0,END)
    arg3=ent3.insert(0,lettres[random.randrange(0,26)])
    ent4.delete(0,END)
    arg4=ent4.insert(0,lettres[random.randrange(0,26)])
    ent5.delete(0,END)
    arg5=ent5.insert(0,lettres[random.randrange(0,26)])
    ent6.delete(0,END)
    arg6=ent6.insert(0,lettres[random.randrange(0,26)])
    ent7.delete(0,END)
    arg7=ent7.insert(0,voyelles[random.randrange(0,6)])
    ent8.delete(0,END)
    arg8=ent8.insert(0,lettres[random.randrange(0,26)])
    ent9.delete(0,END)
    arg9=ent9.insert(0,lettres[random.randrange(0,26)])
    affichage1['text'] = ''
    affichage2['text'] = ''
    affichage3['text'] = ''
    affichage4['text'] = ''
    affichage5['text'] = ''
    
def reset():
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)
    ent7.delete(0,END)
    ent8.delete(0,END)
    ent9.delete(0,END)
    affichage1['text'] = ''
    affichage2['text'] = ''
    affichage3['text'] = ''
    affichage4['text'] = ''
    affichage5['text'] = ''
    
    

application = Tk()
application.title("Résolution")

frame1 = Frame(application, bg="white", width=300, height=150)
frame1.pack(side=TOP,fill=Y)

frame3 = Frame(application, bg="white", width=300, height=150)
frame3.pack(side=BOTTOM,fill=Y)

frame2 = Frame(application, bg="white",width=300, height=150)
frame2.pack(side=BOTTOM, fill=Y)



w=2

lab1 = Label(frame1, text="*").grid(row=0,column=0)
ent1 = Entry(frame1,width=w)
ent1.grid(row=0,column=1)
lab2 = Label(frame1, text="*" ).grid(row=0,column=2)
ent2 = Entry(frame1,width=w)
ent2.grid(row=0,column=3)
lab3 = Label(frame1, text="*").grid(row=0,column=4)
ent3 = Entry(frame1,width=w)
ent3.grid(row=0,column=5)
lab4 = Label(frame1, text="*").grid(row=0,column=6)
ent4 = Entry(frame1,width=w)
ent4.grid(row=0,column=7)
lab5 = Label(frame1, text="*" ).grid(row=0,column=8)
ent5 = Entry(frame1,width=w)
ent5.grid(row=0,column=9)
lab6 = Label(frame1, text="*").grid(row=0,column=10)
ent6 = Entry(frame1,width=w)
ent6.grid(row=0,column=11)
lab7 = Label(frame1, text="*").grid(row=0,column=12)
ent7 = Entry(frame1,width=w)
ent7.grid(row=0,column=13)
lab8 = Label(frame1, text="*").grid(row=0,column=14)
ent8 = Entry(frame1,width=w)
ent8.grid(row=0,column=15)
lab9 = Label(frame1, text="*").grid(row=0,column=16)
ent9 = Entry(frame1,width=w)
ent9.grid(row=0,column=17)


valeur = Button(frame2, text =' run', command=calcul)
valeur.pack()

valeur = Button(frame2, text =' clear', command=reset)
valeur.pack()

rand = Button(frame2, text =' random', command=aleatoire)
rand.pack()

affichage1 = Label(frame3, width=30)
affichage1.pack()
affichage2 = Label(frame3, width=30)
affichage2.pack()
affichage3 = Label(frame3, width=30)
affichage3.pack()
affichage4 = Label(frame3, width=30)
affichage4.pack()
affichage5 = Label(frame3, width=30)
affichage5.pack()

application.mainloop()