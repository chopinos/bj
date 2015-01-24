#!/usr/bin/python

import random
import numpy as np
import matr
import os
import situations as sit

PL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DL_V=0
PL_V=0
BET=10
CASH=1000
deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

#return numerical value !problem with aces!
def numerical_value(card):
    if card not in ["J","Q","K","A"]:
        card = int(card)
    elif (card == "A"):
        card = 1
    else:
        card = 10
    return card

#print values
def print_val():
    print os.system("clear")
    print "DEALER:"
    print "%s" % DL[0]
    print "\nPLAYER:"
    print "%s %s" % (PL[0], PL[1])

#check which matrice is valid, precheck has to done to determine if there is bj
def check_matrice(PL):
    if PL[0] == PL[1]:
        return "matrice_c.dat"
    elif (PL[0] == "A") or (PL[1] == "A"):
        return "matrice_b.dat"
    else:
        return "matrice_a.dat" 

#check for proper play
def prop_play(PL, DL):
    if check_matrice(PL) == "matrice_a.dat":
        return matr.ch_matrice_a(PL, DL)
    elif check_matrice(PL) == "matrice_b.dat":
        return matr.ch_matrice_b(PL, DL)
    elif check_matrice(PL) == "matrice_c.dat":
        return matr.ch_matrice_c(PL, DL) 
    else: 
        print "Error with determination of proper play"

def precheck(PL, DL):
    if PL_V == 21 and DL_V != 21:
        BET = BET * 1.5
    	CASH = CASH + BET
    elif PL_V == 21: 
    	CASH = CASH 
    else:
    	True

#return overall value of cards
#def p_val():
#    print PL_V
#    for x in xrange(9):
#        PL_V = PL_V + PLv[x] 
#        return PL_V

#toss for random cards
#DL[0] = random.choice(deck)
#DL[1] = random.choice(deck)
#PL[0] = random.choice(deck)
#PL[1] = random.choice(deck)
sit.hit(PL)
sit.hit(PL)
sit.hit(DL)

print PL 
print DL
#get numerical values of cards
for x in xrange(9):
    PLv[x] = numerical_value(PL[x]) 
    DLv[x] = numerical_value(DL[x])
    #print PLv[x]

print_val()

PL_V = PLv[0] + PLv[1] #calculates overall numerical value for player
DL_V = DLv[0] + DLv[1] #calculates overall numerical value for dealer

#check which matrice to use
print "\nProper matrice: "
print check_matrice(PL)

print "\nProper play: "
print prop_play(PL[:], DL[:])

print PL
print DL
