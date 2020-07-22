#This is a random character generator.

import random

WS = random.randint(2, 4)
BS = random.randint(2, 4)
S = random.randint(2, 4)
T = random.randint(2, 4)
W = random.randint(2, 4)
I = random.randint(2, 4)
A = random.randint(1, 3)
LD = random.randint(6, 8)

Role = random.randint(1, 6)
if Role == 1:
    LD = LD + 1
    A=A+1
    if WS > BS:
        WS = WS + 1
    if BS > WS:
        BS = BS + 1
    if BS == WS:
        T = T + 1
    print('Lone Wolf')
if 1 < Role < 6:
    print('Thug')
if Role == 6:
    A=A+1
    LD = LD + 2
    print('Sergeant')

WS = str(WS)
BS = str(BS)
S = str(S)
T = str(T)
W = str(W)
I = str(I)
A = str(A)
LD = str(LD)
print('WS:' + WS + ' BS:' + BS + ' S:' + S + ' T:' + T + ' W:' + W + ' I:' + I + ' A:' + A + ' LD:' + LD)
