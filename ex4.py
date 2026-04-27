#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:08:28 2023

@author: amelie
"""

from tkinter import *
import numpy as np
import math


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


def dessiner_sommet(canvas,coord_sommet,label_sommet):
    dessine_cercle(canvas,coord_sommet[0],coord_sommet[1],10)
    ecrire_texte(canvas,coord_sommet,label_sommet)
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


def generer_coordonnees(matrice_graphe):
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


def dessiner_graphe(canvas,matrice_graphe,coordonnees_sommets):
    N_sommets=len(matrice_graphe)
    graphe_non_oriente= True #Booléen valant True si le graphe défini par matrice_graphe est non_orienté et False sinon 
    for i in range(N_sommets):
        for j in range(N_sommets):
            if matrice_graphe[i][j] != matrice_graphe[j][i]:
                graphe_non_oriente = False
                break#On commence par afficher tous les arcs/arêtes

    if graphe_non_oriente :
        for i in range(N_sommets):
            for j in range(i+1,N_sommets):
                if matrice_graphe[i][j]:
                    dessiner_arc(canvas, coordonnees_sommets[i], coordonnees_sommets[j])
            if matrice_graphe[i][i]: 
                dessiner_boucle(canvas,coordonnees_sommets[i])
    else : 
        for i in range(N_sommets):
            for j in range(N_sommets):
                if matrice_graphe[i][j]:
                    if i!=j :
                        dessiner_arc(canvas,coordonnees_sommets[i],coordonnees_sommets[j], True)
                    else:
                        dessiner_boucle(canvas,coordonnees_sommets[i])
    

                    
    for i in range(N_sommets):
    	dessiner_sommet(canvas,coordonnees_sommets[i],i)

    return




matrice_graphe=np.array([[0,1,1,1,0],
                          [0,1,0,1,0],
                          [1,0,0,1,1],
                          [0,1,0,1,1],
                          [1,1,1,1,0]])


matrice_graphe2=np.array([[0,1,1,0],
                          [1,0,1,0],
                          [1,1,1,1],
                          [0,0,1,1]])

#génération des coordonnées des sommets sur une grille
#coordonnees_sommets=generer_coordonnees(matrice_graphe)
#alternativement, on peut générer les coordonnées en plaçant les sommets sur un cercle : avec la fonction generer_coordonnees_cercle
coordonnees_sommets=generer_coordonnees_cercle(matrice_graphe2)

interface=Tk()
interface.minsize(500, 500)

bquit=Button(interface,text='Quitter',command=interface.destroy)
bquit.place(x=410,y=450) 

zone_dessin=Canvas(interface,width=400, height=400, bg="white")
zone_dessin.pack(padx=10, pady=10)

dessiner_graphe(zone_dessin,matrice_graphe2,coordonnees_sommets)

interface.mainloop()
