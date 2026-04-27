

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random


    
def Find_naif(x,dict_indices):
    return dict_indices[x]

def Union_naif(x,y,dict_indices):
    #si x et y sont déjà dans le même ensemble, on ne fait rien

    #sinon ...
    if Find_naif(x, dict_indices) != Find_naif(y, dict_indices) :
        for i in range(len(dict_indices)):
            if dict_indices[i] == x:
                dict_indices[i] = y

    

def Test_Union_Find_naif(N, printing=False):
    #d'abord nous construisons la structure naïve
    dict_indices=dict()
    for i in range(N):
        dict_indices[i]=i
    if printing :
        print(dict_indices)    
    
    #puis nous appliquons N opérations "UNION" sur des paires de sommets aléatoires
    for i in range(N):
        x,y=random.sample(range(N),2)
        Union_naif(x,y,dict_indices)
        if printing :
            print("Union de "+str((x,y)))
            print(dict_indices)
    return



class Arbre_simple :
    def __init__(self,parent,nom):
        self.parent=parent
        self.nom=nom #ce nom ne servira que pour l'affichage
        return
    def str_chaine_racines(self): 
    #cette fonction peut servir à afficher les racines d'un arbres pour débugger
    #NB : cette fonction n'affiche pas l'arbre complet
        if not self.parent:
            return str(self.nom)
        else :
            return self.parent.str_chaine_racines()+"->"+str(self.nom)
    
def Find_arbre_simple(x):
    if x.parent == None:
        return x
    return Find_arbre_simple(x.parent)

def Union_arbre_simple(x,y,classes):
    #si x et y sont déjà dans le même ensemble, on ne fait rien
    xRacine= Find_arbre_simple(classes[x])
    yRacine= Find_arbre_simple(classes[y])
    if xRacine != yRacine:
        xRacine.parent = yRacine

    return 

def Test_Union_Find_arbre_simple(N, printing=False):
    #aboard nous construisons la structure arborescente simple
    classes=[Arbre_simple(None,i) for i in range(N)]  
    if printing :
        for j in range(N):
            print(classes[j].str_chaine_racines(), end=" , ")    
        print()
    
    #puis nous appliquons N opérations "UNION" sur des paires de sommets aléatoires
    for i in range(N):
        x,y=random.sample(range(N),2)
        Union_arbre_simple(x,y,classes)
        if printing :
            print("Union de "+str((x,y)))
            for j in range(N):
                print(classes[j].str_chaine_racines(),end=" , ")
            print()
    return



class Arbre_by_rank :
    def __init__(self,parent,rang, nom):
        self.parent=parent
        self.rang=rang
        self.nom=nom #ceci ne servira que pour l'affichage
        return
    def str_chaine_racines(self): 
    #cette fonction peut servir à afficher les racines d'un arbres pour débugger
    #le rang de la racine de l'arbre est également affiché
    #NB : cette fonction n'affiche pas l'arbre complet
        if not self.parent:
            return "("+str(self.nom)+",r="+str(self.rang)+")"
        else :
            return self.parent.str_chaine_racines()+"->"+str(self.nom)

def Find_arbre_by_rank(x):
    if x.parent == None:
        return x
    return Find_arbre_by_rank(x.parent)

def Union_arbre_by_rank(x,y,classes):
    xRacine = Find_arbre_by_rank(classes[x])
    yRacine = Find_arbre_by_rank(classes[y])

    #si x et y sont déjà dans le même ensemble, on ne fait rien
    
    #sinon, ...
    if xRacine != yRacine:
        if xRacine.rang < yRacine.rang:
            xRacine.parent = yRacine
        else:
            yRacine.parent = xRacine
            if xRacine.rang == yRacine.rang:
                xRacine.rang = xRacine.rang + 1
            

    return

def Test_Union_Find_arbre_by_rank(N, printing=False):
    #d'abord nous construisons la structure arborescente simple
    classes=[Arbre_by_rank(None,0,i) for i in range(N)]
    if printing :
        for j in range(N):
            print(classes[j].str_chaine_racines(), end=" , ")    
        print()
    
    #puis nous appliquons N opérations "UNION" sur des paires de sommets aléatoires
    for i in range(N):
        x,y=random.sample(range(N),2)
        Union_arbre_by_rank(x,y,classes)
        if printing :
            print("Union de "+str((x,y)))
            for j in range(N):
                print(classes[j].str_chaine_racines(),end=" , ")
            print()
    return


if __name__=="__main__":
    #Quelques tests basiques avec affichage pour vérifier si tout fonctionne comme prévu :
    print("Test Union-Find naif : ")
    Test_Union_Find_naif(5, printing=True)
    print()
    print("Test Union-Find arbre simple : ")
    Test_Union_Find_arbre_simple(5, printing=True)
    print()
    print("Test Union-Find arbre_by_rank : ")
    Test_Union_Find_arbre_by_rank(5, printing=True)
    print()
    
    print("Comparaison des temps d'execution des trois version de Union-Find : \n")
    for N in [1000,5000,10000]:
        print("N = "+str(N))
        start_time = time.time()
        Test_Union_Find_naif(N)
        print("Union-Find naif : %s seconds " % (time.time() - start_time))
        start_time = time.time()
        Test_Union_Find_arbre_simple(N)
        print("Union-Find arbre simple : %s seconds " % (time.time() - start_time))
        start_time = time.time()
        Test_Union_Find_arbre_by_rank(N)
        print("Union-Find arbre by rank : %s seconds \n" % (time.time() - start_time))


