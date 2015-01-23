#describes play when Hit/Stand/sPlit/Double

import matr
import random

PL = [3, 'A', 0, 0, 0, 0, 0, 0, 0, 1, 0]
DL = [8, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0]
PLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DLv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PL_V = 0
PL_V_b = 0
deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

def numerical_value(card):
    if card not in ["J","Q","K","A"]:
        card = int(card)
    elif (card == "A"):
        card = 1
    else:
        card = 10
    return card

def stand(PL, DL, PLv, DLv):
    PL[10] = 1 #END of story
    return PL 

def double(PL, DL, PLv, DLv):
    PL[2] = random.choice(deck) 
    PL[10] = 1 #END of story
    return PL

def hit(PL, DL, PLv, DLv):
    PL[PL[9]] = random.choice(deck)
    PL[9] = PL[9] + 1
    return PL
     
def split(val_p, val_d):
    True

print hit(PL, DL, PLv, DLv)

for x in xrange(9):
    PLv[x] = numerical_value(PL[x])
    DLv[x] = numerical_value(DL[x])

PL_V = sum(PLv)

print PL_V

for x in xrange(9):
    if PL[x] == 'A':
        PL_V_b = PL_V + 10
print PL_V_b

if PL_V_b > 21:
    PL_V_b = 0

print max(PL_V, PL_V_b)

print hit(PL, DL, PLv, DLv) 
print hit(PL, DL, PLv, DLv)

