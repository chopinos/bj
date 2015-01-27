#!/usr/bin/python

import random
import numpy as np
import matr
import os
import situations as sit

PL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
global PLv 
PLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
global DLv
DLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
global DLV
DLV = 0
global PLV
PLV = 0
global BET
global CASH
BET = 10
CASH = 1000
no_games = 0
global pro_dec
pro_dec = 0
wro_dec = 0
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
#    print os.system("clear")
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

#gramy
def lets_play():

    print os.system("clear")
    print_val()

    if ((PL[0] == 'A' or PL[1] == 'A') and PLV == 11 and ((DL[0] == 'A' or DL[1] == 'A') and PLV == 11)):
        print "PUSH. NOONE WINS"
        global pro_dec
        pro_dec = pro_dec + 1
    elif (PL[0] == 'A' or PL[1] == 'A') and PLV == 11:
        print "BLACKJACK!"
        global pro_dec 
        pro_dec = pro_dec + 1
#        BET = BET * 1.5
#        CASH = CASH + BET
    else: 
        global my_decision
        my_decision = raw_input("\nWhat is your decision? \nHit (1), Stand (2), Double (3), sPlit (4), End (5): \n")
        if   my_decision == '1':
            my_decision = 'H'
        elif my_decision == '2':
            my_decision = 'S'
        elif my_decision == '3':
            my_decision = 'D'
        elif my_decision == '4':
            my_decision = 'P'
        elif my_decision == '5':
            my_decision = 'E'

        if (prop_play(PL[:], DL[:]) == my_decision):
            print "[+] GOOD JOB!"
#            CASH = CASH + BET
            global pro_dec
            pro_dec =  pro_dec + 1
        elif my_decision == 'E':
            print "GOODBYE"
        else:
            print "[-] WRONG" 
            print "Proper decision: %s" % prop_play(PL[:], DL[:])
#	    CASH = CASH - BET
            global wro_dec 
            wro_dec = wro_dec + 1
    raw_input()

my_decision = 'Y'
while(my_decision != 'E'):
    PL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    DL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sit.hit(PL)
    sit.hit(PL)
    sit.hit(DL)
    sit.hit(DL)
    for x in xrange(9):
        PLv[x] = numerical_value(PL[x])
        DLv[x] = numerical_value(DL[x])

    PLV = sum(PLv[0:8])
    DLV = sum(DLv[0:8])
    lets_play()
    no_games = no_games + 1

print "Overall games: %d" % (no_games - 1)
print "Proper decisions: %d (%d%%)" % (pro_dec, 100 * float(pro_dec) / (no_games - 1))
print "Wrong decisions: %d (%d%%)" % (wro_dec, 100 * float(wro_dec) / (no_games - 1))
