#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:08:28 2023

@author: amelie
"""

from tkinter import *
import numpy as np
import math
import random
import time


def dessine_cercle(canvas,x_centre,y_centre,rayon,contour='black',interieur='white'):
    A=(x_centre-rayon, y_centre-rayon)
    B=(x_centre+rayon, y_centre+rayon)
    canvas.create_oval(A,B, fill=interieur, outline=contour)
    return

def dessine_ligne(canvas,x_debut,y_debut,x_fin,y_fin,epaisseur=3,couleur='black',fleche=False):
    if fleche:
        canvas.create_line(x_debut,y_debut,x_fin,y_fin, width=epaisseur, fill=couleur,arrow='last')
    else : 
        canvas.create_line(x_debut,y_debut,x_fin,y_fin, width=epaisseur, fill=couleur)
    return

def ecrire_texte(canvas,coordonnees,texte,couleur='black'):
    canvas.create_text(coordonnees, text=texte, fill=couleur, font="Arial 15 bold")
    return

def generer_coordonnees_grille(matrice_graphe):
    N_sommets=len(matrice_graphe)
    return

def dessiner_sommet(canvas,coord_sommet,label_sommet,couleur='white'):
    dessine_cercle(canvas,coord_sommet[0],coord_sommet[1],10,interieur=couleur)
    if couleur!='black':
        ecrire_texte(canvas,coord_sommet,label_sommet)
    else:
        ecrire_texte(canvas,coord_sommet,label_sommet,couleur='white')
    return

def dessiner_arc(canvas,coord_sommet_1,coord_sommet_2,fleche=False):
    if fleche==False:
        dessine_ligne(canvas,coord_sommet_1[0],coord_sommet_1[1],coord_sommet_2[0],coord_sommet_2[1])
    else : 
        #deplacer la fin de ligne pour que la fleche soit visible
        L=np.sqrt((coord_sommet_2[0]-coord_sommet_1[0])**2+(coord_sommet_2[1]-coord_sommet_1[1])**2)
        x_fin=coord_sommet_1[0]+(coord_sommet_2[0]-coord_sommet_1[0])*(L-10)/L
        y_fin=coord_sommet_1[1]+(coord_sommet_2[1]-coord_sommet_1[1])*(L-10)/L
        dessine_ligne(canvas,coord_sommet_1[0],coord_sommet_1[1],x_fin,y_fin,fleche=True)
    return

def dessiner_boucle(canvas,coord_sommet,fleche=False):
    x_centre,y_centre=coord_sommet[0],coord_sommet[1]-18
    rayon=10
    A=(x_centre-rayon, y_centre-rayon)
    B=(x_centre+rayon, y_centre+rayon)
    
    canvas.create_arc(A, B, outline="red", extent=320, start=-90, width=3,style=ARC)
    
    if fleche==True:
        fA=(x_centre+1, y_centre+3)
        fB=(x_centre+15, y_centre+7)
        fC=(x_centre+5, y_centre+15)
        canvas.create_polygon(fA, fB, fC, fill='red')

    return


def generer_coordonnees_grille(matrice_graphe):
    N_sommets=len(matrice_graphe)
    largeur_grille=math.ceil(np.sqrt(N_sommets))
    
    coordonnees=[]
    for k in range(N_sommets):
        ligne,colonne=k//largeur_grille,k%largeur_grille
        coordonnees.append(((colonne+1)*int(400/(largeur_grille+1)),(ligne+1)*int(400/(largeur_grille+1))))
    return coordonnees

def generer_coordonnees_cercle(matrice_graphe):
    N_sommets=len(matrice_graphe)
    rayon_cercle=150
    centre_cercle=(200,200)
    
    coordonnees=[]
    for k in range(N_sommets):
        angle=2*math.pi/N_sommets*k
        coordonnees.append((centre_cercle[0]+math.cos(angle)*rayon_cercle,centre_cercle[1]+math.sin(angle)*rayon_cercle))
    return coordonnees

def graphe_matrice2liste(matrice_graphe):
    N_sommets=len(matrice_graphe)
    liste_graphe=[[] for i in range(N_sommets)]
    for i in range(N_sommets):
        for j in range(N_sommets):
            if matrice_graphe[i,j]==1:
                liste_graphe[i].append(j)
    return liste_graphe

def dessiner_graphe(canvas,matrice_graphe,coordonnees_sommets,coloration=None):
    N_sommets=len(matrice_graphe)
    symetrie=(matrice_graphe==matrice_graphe.T).all()
    
    if symetrie :
        for i in range(N_sommets):
            if matrice_graphe[i,i]==1:
                dessiner_boucle(canvas,coordonnees_sommets[i]) 
            for j in range(i+1,N_sommets):
                if matrice_graphe[i,j]==1:
                    dessiner_arc(canvas,coordonnees_sommets[i],coordonnees_sommets[j])    
    else : 
        for i in range(N_sommets):
            for j in range(N_sommets):
                if matrice_graphe[i,j]==1 and i!=j:
                    dessiner_arc(canvas,coordonnees_sommets[i],coordonnees_sommets[j],fleche=True)
                if matrice_graphe[i,j]==1 and i==j:
                    dessiner_boucle(canvas,coordonnees_sommets[i],fleche=True)
                    
    for i in range(N_sommets):
        if not coloration:
            dessiner_sommet(canvas,coordonnees_sommets[i],str(i+1))    
        else:
            dessiner_sommet(canvas,coordonnees_sommets[i],str(i+1),couleur=coloration[i])   
    return

def update_dessin_et_labels():
    global date,label_date,coloration,dGRIS,label_dGRIS,dNOIR,label_dNOIR
    
    label_date.config(text = "Date : "+str(date))
    label_dGRIS.config(text = "dGRIS : "+str(dGRIS))
    label_dNOIR.config(text = "dNOIR : "+str(dNOIR))
    dessiner_graphe(zone_dessin,matrice_graphe,coordonnees_sommets,coloration=coloration)
    return

def reinitialiser():
    global date,label_date,coloration,dGRIS,label_dGRIS,dNOIR,label_dNOIR,binit,bsuivant
    
    date=0
    coloration=['white','white','white','white','white']
    dGRIS=[0,0,0,0,0]
    dNOIR=[0,0,0,0,0]
    
    update_dessin_et_labels()
    binit.config(state=DISABLED)
    bsuivant.config(state=NORMAL)
    return

def parcours_profondeur():
    global date,label_date,coloration,dGRIS,label_dGRIS,dNOIR,label_dNOIR,binit,bsuivant
    
    N_sommets=len(matrice_graphe)
    liste_sommets=list(range(N_sommets))
    random.shuffle(liste_sommets)
    for sommet in liste_sommets:
        if coloration[sommet]=='white':
            visiter(sommet)
    
    binit.config(state=NORMAL)
    bsuivant.config(state=DISABLED)
    return

def visiter(sommet):
    global interface,date,label_date,coloration,dGRIS,label_dGRIS,dNOIR,label_dNOIR
    
    
    #Pour metter à jour le dessin
    update_dessin_et_labels()
    interface.update()
    time.sleep(2)

    return

matrice_graphe=np.array([[0,0,0,1,0],
                          [0,1,0,1,0],
                          [1,0,0,1,0],
                          [0,1,0,0,1],
                          [0,0,0,0,0]])

liste_graphe=graphe_matrice2liste(matrice_graphe)
coordonnees_sommets=generer_coordonnees_cercle(matrice_graphe)

date=0
coloration=['white','white','white','white','white']
dGRIS=[0,0,0,0,0]
dNOIR=[0,0,0,0,0]




interface=Tk()
interface.minsize(500, 600)

bquit=Button(interface,text='Quitter',command=interface.destroy)
bquit.place(x=410,y=450) 

binit=Button(interface,text='Reinitialiser',command=reinitialiser, state= DISABLED)
binit.place(x=10,y=450) 

bsuivant=Button(interface,text='Parcours profondeur',command=parcours_profondeur)
bsuivant.place(x=150,y=450) 

label_date = Label(interface, text = "Date : "+str(date))
label_date.place(x=10,y=500)

label_dGRIS = Label(interface, text = "dGRIS : "+str(dGRIS))
label_dGRIS.place(x=10,y=520)

label_dNOIR = Label(interface, text = "dNOIR : "+str(dNOIR))
label_dNOIR.place(x=10,y=540)

zone_dessin=Canvas(interface,width=400, height=400, bg="white")
zone_dessin.pack(padx=10, pady=10)

dessiner_graphe(zone_dessin,matrice_graphe,coordonnees_sommets,coloration=coloration)


interface.mainloop()