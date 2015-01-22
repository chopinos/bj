#!/usr/bin/python

import random
import numpy as np
import matr
import os

PL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DL1_v=0
DL2_v=0
PL1_v=0
PL1_v=0
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
def check_matrice(pl1, pl2):
    if pl1 == pl2:
        return "matrice_c.dat"
    elif (pl1 == "A") or (pl2 == "A"):
        return "matrice_b.dat"
    else:
        return "matrice_a.dat" 

#check for proper play
def prop_play(pl1, pl2, dl1):
    check_matrice(pl1, pl2)
    if check_matrice(pl1, pl2) == "matrice_a.dat":
        return matr.ch_matrice_a(dl1, pl1, pl2)
    elif check_matrice(pl1, pl2) == "matrice_b.dat":
        return matr.ch_matrice_b(dl1, pl1, pl2)
    elif check_matrice(pl1, pl2) == "matrice_c.dat":
        return matr.ch_matrice_c(dl1, pl1, pl2) 
    else: 
        print "Error with determination of proper play"

def precheck(pl0, pl1, dl0):
    if PL_V == 21 AND DL_V != 21:
        BET = BET * 1.5
	CASH = CASH + BET
    elif PL_V == 21 
	CASH = CASH 
    else 
	True

#toss for random cards
DL[0] = random.choice(deck)
DL[1] = random.choice(deck)
PL[0] = random.choice(deck)
PL[1] = random.choice(deck)

#get numerical values of cards
DL0_v = numerical_value(DL[0])
DL1_v = numerical_value(DL[1])
PL0_v = numerical_value(PL[0])
PL1_v = numerical_value(PL[1])

print_val()

PL_V = PL0_v + PL1_v #calculates overall numerical value for player
DL_V = DL0_v + DL1_v #calculates overall numerical value for dealer

#check which matrice to use
#print "Proper matrice: "
#print check_matrice(PL1, PL2)

print "\nProper play: "

print prop_play(PL0_v, PL1_v, DL0_v)
print prop_play(10, 10, 10)
