#!/usr/bin/python
#assume that all figure (except A) are transfered to 10 value
#precheck of matrice is required

import math
import numpy as np
#PL[9] -> no of card
#PL[10] -> to play or not

PL = [5, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0]
DL = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DL_V=0
PL_V=0

def numerical_value(card):
    if card not in ["J","Q","K","A"]:
        card = int(card)
    elif (card == "A"):
        card = 1
    else:
        card = 10
    return card

def ch_matrice_a(PL, DL):
    data = np.genfromtxt("matrice_a.dat",delimiter="|",dtype=str) #get matrice
    for x in xrange(9):
       PLv[x] = numerical_value(PL[x])
       DLv[x] = numerical_value(DL[x])
    PL_V = sum(PL[0:8]) #take sum, assume that there are no A or other fig.
    DL_V = sum(DL)

    if DL[0] == "A": #check if dealer card is A, then assign value
        DL[0] = 11
    if PL_V > 17:
        PL_V = 17
    else: 
        True
    
    if (data[PL_V - 4][DL_V - 1] == 'D') and (PL[9] > 1):
        decision = 'H'
    else:
        decision = data[PL_V - 4][DL_V - 1]
    return decision

def ch_matrice_b(PL, DL):
    data = np.genfromtxt("matrice_b.dat",delimiter="|",dtype=str) #get matrice
    if DL[0] == "A": #check if dealer card is A
        DL[0] = 11
    
    #check which card is A
    if PL[0] == "A":
        return data[PL[1] - 1][DL[0] - 1]
    elif PL[1] == "A":
        return data[PL[0] - 1][DL[1] - 1]

def ch_matrice_c(PL, DL):
    data = np.genfromtxt("matrice_c.dat",delimiter="|",dtype=str) #get matrice
    if DL[0] == "A":
        DL[0] = 11
    if PL[0] == "A": #check if cards are As
        PL[1] = 1
    return data[PL[0]][DL[0] - 1]

print ch_matrice_a(PL, DL)
