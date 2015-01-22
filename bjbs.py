#!/usr/bin/python

import random
import numpy as np
import matr
import os

DL1=0 #do not change values to numerical fot these variables which do not have _v in their name
DL1_v=0
DL2=0
DL2_v=0
PL1=0
PL2=0
PL1_v=0
PL1_v=0
DL_V=0
PL_V=0
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
    print "%s" % DL1
    print "\nPLAYER:"
    print "%s %s" % (PL1, PL2)

#check which matrice is valid, precheck has to done to determine if there is bj
def check_matrice(pl1, pl2):
    if PL1 == PL2:
        return "matrice_c.dat"
    elif (PL1 == "A") or (PL2 == "A"):
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

#toss for random cards
DL1 = random.choice(deck)
DL2 = random.choice(deck)
PL1 = random.choice(deck)
PL2 = random.choice(deck)

#get numerical values of cards
DL1_v = numerical_value(DL1)
DL2_v = numerical_value(DL2)
PL1_v = numerical_value(PL1)
PL2_v = numerical_value(PL2)

print_val()

PL_V = PL1_v + PL2_v #calculates overall numerical value for player
DL_V = DL1_v + DL2_v #calculates overall numerical value for dealer

#check which matrice to use
#print "Proper matrice: "
#print check_matrice(PL1, PL2)

print "\nProper play: "
#print str.center(12, 'Proper play:')
#str = "this is string example....wow!!!";
#print str.center(100)


print prop_play(PL1_v, PL2_v, DL1_v)
print prop_play(10, 10, 10)
