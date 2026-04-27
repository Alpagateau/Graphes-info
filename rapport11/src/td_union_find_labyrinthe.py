#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ex1 import Arbre_by_rank, Find_arbre_by_rank, Union_arbre_by_rank
from tkinter import *
import random
from math import sqrt


def generer_grille_complete(N):
    #on genere la grille complete de taille NxN
    #V contiendra la liste des sommets et E la liste des arêtes
    V,E=[],[]
    for i in range(N):
        for j in range(N):
            V += [(i, j)]
            if i < N-1:
                E += [((i, j), (i+1, j))]
            if j < N-1:
                E += [((i, j), (i, j+1))]
    return V,E

def fisher_yates(E):
    #renvoie une permutation aléatoire de la liste E
    E_permut=list(E)
    for i in range(len(E)-1):
        j=random.randint(i, len(E)-1)
        E_permut[i], E_permut[j] = E_permut[j], E_permut[i]

    return E_permut

def generer_labyrinthe(N):
    #Generer le graphe grille complet
    V,E=generer_grille_complete(N)
    #Permuter les aretes de E
    E=fisher_yates(E)
    #Au debut E' est vide (tous les murs sont présents)
    E_prime=[]
    
    #Chaque sommet est initialement isole des autres
    classes=[Arbre_by_rank(None,0,i) for i in range(N**2)]
    
    #Pour chacune des "m" aretes de E, tester si ses extrémités sont dans des classes différentes
    for ((x1,y1), (x2, y2)) in E:
        if Find_arbre_by_rank(classes[x1*N + y1]) != Find_arbre_by_rank(classes[x2*N + y2]):
            #Si oui, ajouter l'arete a E' (autrement dit, retirer le mur)
            E_prime.append(((x1, y1), (x2,y2)))
            Union_arbre_by_rank(x1*N + y1, x2*N + y2, classes)


    return V,E_prime

def dessiner_graphe(canvas,sommets,aretes):
    largeur_grille=int(sqrt(len(sommets)))
    ratio = 400/(largeur_grille+2)
    canvas.create_rectangle(ratio,ratio,400-ratio,400-ratio,fill='black',outline='black', width=1)
    for s in sommets :
        x,y=s
        canvas.create_rectangle((x+1)*ratio+1,(y+1)*ratio+1,(x+2)*ratio-1,(y+2)*ratio-1,fill='white',outline='white')
    for a in aretes :
        x1,y1=a[0]
        x2,y2=a[1]
        canvas.create_rectangle((x1+2)*ratio-1,(y1+2)*ratio-1,(x2+1)*ratio+1,(y2+1)*ratio+1,fill='white',outline='white')
    return

def dessiner_grille_initiale():
    zone_dessin.create_rectangle(0,0,400,400,fill='white',outline='white')
    N=int(entry.get())
    V,E=generer_grille_complete(N)
    #Pour une grille sans mur, garder E tel quel (commenter la ligne suivante)
    #Pour afficher les murs, vider E (garder la ligne suivante)
    E=[]
    dessiner_graphe(zone_dessin,V,E)
    return

def dessiner_labyrinthe_aleatoire():
    zone_dessin.create_rectangle(0,0,400,400,fill='white',outline='white')
    N=int(entry.get())
    V,E=generer_labyrinthe(N)
    dessiner_graphe(zone_dessin,V,E)
    return

interface=Tk()
interface.minsize(500, 500)

bquit=Button(interface,text='Quitter',command=interface.destroy)
bquit.place(x=410,y=470) 

label_N = Label(interface, text="Taille N de la grille (entier):")
label_N.place(x=10,y=430) 
entry= Entry(interface, width=5)
entry.insert(END, 10)
entry.place(x=230,y=430) 

bgrille=Button(interface,text='Grille initiale',command=dessiner_grille_initiale)
bgrille.place(x=10,y=450) 
blabyrinthe=Button(interface,text='Labyrinthe',command=dessiner_labyrinthe_aleatoire)
blabyrinthe.place(x=210,y=450) 

zone_dessin=Canvas(interface,width=400, height=400, bg="white")
zone_dessin.pack(padx=10, pady=10)


interface.mainloop()
