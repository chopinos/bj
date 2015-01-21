#!/usr/bin/python
#assume that all figure (except A) are transfered to 10 value
#precheck of matrice is required

import math
import numpy as np

DL1 = "A"
PL1 = "A"
PL2 = "A"

def ch_matrice_a(dl1, pl1, pl2):
    data = np.genfromtxt("matrice_a.dat",delimiter="|",dtype=str) #get matrice
    pl_v = pl1 + pl2 #take sum, assume that there are no A or other fig.

    if dl1 == "A": #check if dealer card is A, then assign value
        dl1 = 11

    if pl1 == "A":
        pl1 = 11
    elif pl2 == "A":
        pl2 = 11
    elif pl_v > 17:
        pl_v = 17
    else: 
        True
    
    if dl1 == "A":
        dl1 = 11

    print data[pl_v - 4][dl1 - 1]
    return data[pl_v - 4][dl1 - 1]

def ch_matrice_b(dl1, pl1, pl2):
    data = np.genfromtxt("matrice_b.dat",delimiter="|",dtype=str) #get matrice
    
    if dl1 == "A": #check if dealer card is A
        dl1 = 11
    
    #check which card is A
    if pl1 == "A":
        print data[pl2 - 1][dl1 - 1]
        return data[pl2 - 1][dl1 - 1]
    elif pl2 == "A":
        print data[pl1 - 1][dl1 - 1]
        return data[pl1 - 1][dl1 - 1]
    else: 
        True


def ch_matrice_c(dl1, pl1, pl2):
    data = np.genfromtxt("matrice_c.dat",delimiter="|",dtype=str) #get matrice

    if dl1 == "A":
        dl1 = 11

    if pl1 == "A": #check if cards are As
        pl1 = 1
    else: 
        True

    print data[pl1][dl1 - 1]
    return data[pl1][dl1 - 1]

#ch_matrice_b(DL1, PL1, PL2)
ch_matrice_c(DL1, PL1, PL2)
