#!/usr/bin/python

import random
import numpy as np

DL1=0
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
    print "DEALER:"
    print "%s" % DL1
    print "\nPLAYER:"
    print "%s %s" % (PL1, PL2)

#check which matrice is valid, precheck has to be for bj
def check_matrice(PL1, DL1, DL2):
    if PL1 == PL2:
        return 3
    elif (PL1 == "A") or (PL2 == "A"):
        return 2
    else:
        return 1

DL1 = random.choice(deck)
PL1 = random.choice(deck)
PL2 = random.choice(deck)

DL1_v = numerical_value(DL1)
DL2_v = numerical_value(DL2)

PL1_v = numerical_value(PL1)
PL2_v = numerical_value(PL2)

print_val()

PL_V = PL1_v + PL2_v #calculates overall numerical value for player
DL_V = DL1_v + DL2_v #calculates overall numerical value for dealer

print check_matrice(PL1, DL1, DL2)
