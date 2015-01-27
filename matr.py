#!/usr/bin/python
#assume that all figure (except A) are transfered to 10 value
#precheck of matrice is required

import math
import numpy as np
#PL[9] -> no of card
#PL[10] -> to play or not

PL = [9, 'A', 0, 0, 0, 0, 0, 0, 0, 1, 0]
DL = [4, 'J', 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

    if DL[0] == "A": #check if dealer card is A, then assign value
        DL[0] = 11
    DL[0] = numerical_value(DL[0])

    for x in xrange(9):
       PL[x] = numerical_value(PL[x])
    PL_V = sum(PL[0:8]) #take sum, assume that there are no A or other fig.
    if PL_V > 17:
        PL_V = 17
    
    if (data[PL_V - 4][DL[0] - 1] == 'D') and (PL[9] > 2):
        decision = 'H'
    else:
        decision = data[PL_V - 4][DL[0] - 1]
    return decision

def ch_matrice_b(PL, DL):
    data = np.genfromtxt("matrice_b.dat",delimiter="|",dtype=str) #get matrice
    if DL[0] == "A": #check if dealer card is A, then assign value
        DL[0] = 11
    DL[0] = numerical_value(DL[0])

    #check which card is A
    if PL[0] == "A":
        PL[1] = numerical_value(PL[1])
        return data[PL[1] - 1][DL[0] - 1]
    elif PL[1] == "A":
        PL[0] = numerical_value(PL[0])
        return data[PL[0] - 1][DL[0] - 1]

def ch_matrice_c(PL, DL):
    data = np.genfromtxt("matrice_c.dat",delimiter="|",dtype=str) #get matrice
    if DL[0] == "A": #check if dealer card is A, then assign value
        DL[0] = 11
    DL[0] = numerical_value(DL[0])

    for x in xrange(9):
        PL[x] = numerical_value(PL[x])

    return data[PL[0]][DL[0] - 1]

#print ch_matrice_b(PL, DL)
