#This is a random armour generator
import random

ArmourType=random.randint(1, 6)
if ArmourType<5:
    print('Combat Plate')
    AS=random.randint(4, 6)
    if AS==4:
        AS=random.randint(3, 4)
    if AS==3:
        AS=random.randint(2, 3)
    if AS==4:
        print('Cumbersome')
    if AS<4:
        print('Cumbersome Bulky')
    AS=str(AS)
    print('AS:'+AS+'+')
if ArmourType==5:
    AS=random.randint(4, 6)
    print('Exo-Suit')
    AS=str(AS)
    print('AS:'+AS+'+')
if ArmourType==6:
    print('Powered Armour')
    AS=random.randint(2, 3)
    if AS==2:
        print('Bulky')
    AS=str(AS)
    print('AS:'+AS+'+')
    
