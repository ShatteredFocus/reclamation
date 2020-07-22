#This is a random weapon generator

import random

Type = random.randint(1, 6)
if Type < 3:
    print ('Close Combat Weapon')
    S = random.randint(0, 2)
    AP = random.randint(2, 6)
    I= random.randint(0, 2)
    S=str(S)
    AP=str(AP)
    I=str(I)
    print ('S:+'+S+' AP:'+AP+' I:-'+I)
if Type==3:
    print ('Rifle')
    S=random.randint(3, 5)
    AP=random.randint(4, 6)
    if AP==4:
        AP=random.randint(3, 4)
    if AP==3:
        AP=random.randint(2, 3)
    Range=random.randint(3, 6)
    Range=Range*6
    S=str(S)
    AP=str(AP)
    Range=str(Range)
    print ('S:'+S+' AP:'+AP+' Range:'+Range+'"')
if Type==4:
    print ('Pistol')
    S=random.randint(2, 5)
    AP=random.randint(4, 7)
    if AP==7:
        AP=0
    if AP==4:
        AP=random.randint(3, 4)
    if AP==3:
        AP=random.randint(2, 3)
    Range=random.randint(1, 3)
    Range=Range*6
    S=str(S)
    AP=str(AP)
    Range=str(Range)
    print ('S:'+S+' AP:'+AP+' Range:'+Range+'"')
if Type==5:
    RoF=random.randint(1, 3)
    S=random.randint(2, 5)
    AP=random.randint(4, 7)
    if AP==7:
        AP=0
    if AP==4:
        AP=random.randint(3, 4)
    if AP==3:
        AP=random.randint(2, 3)
    Range=random.randint(3, 5)
    Range=Range*6
    S=str(S)
    AP=str(AP)
    Range=str(Range)
    RoF=str(RoF)
    print('Assault '+RoF)
    print ('S:'+S+' AP:'+AP+' Range:'+Range+'"')
if Type==6:
    S=random.randint(4, 10)
    if S<7:
        RoF=random.randint(3, 6)
        AP=random.randint(4, 5)
        if AP==4:
            AP=random.randint(3, 4)
        if AP==3:
            AP=random.randint(2, 3)
    if S>6:
        RoF=random.randint(1, 2)
        AP=random.randint(3, 4)
        if AP==3:
            AP=random.randint(2, 3)
    Range=random.randint(4, 8)
    Range=Range*6
    S=str(S)
    AP=str(AP)
    Range=str(Range)
    RoF=str(RoF)
    print('Heavy '+RoF)
    print ('S:'+S+' AP:'+AP+' Range:'+Range+'"')
