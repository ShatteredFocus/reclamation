import random
Loot=0
while Loot<3:
    LootCrate=random.randint(1,3)
    print('---------------------')
    if LootCrate==1:
        WS = random.randint(2, 4)
        BS = random.randint(2, 4)
        S = random.randint(2, 4)
        T = random.randint(2, 4)
        W = random.randint(2, 4)
        I = random.randint(2, 4)
        A = random.randint(1, 3)
        LD = random.randint(6, 8)

        Role = random.randint(1, 6)
        if Role < 3:
            A=A+1
            LD = LD + 1
            if WS > BS:
                WS = WS + 1
            if BS > WS:
                BS = BS + 1
            if BS == WS:
                T = T + 1
            print('Lone Wolf')
        if 2 < Role < 6:
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
        Loot=Loot+1
    if LootCrate==2:
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
            if AP==4:
                AP=random.randint(3, 4)
            if AP==3:
                AP=random.randint(2, 3)
            Range=random.randint(3, 5)
            Range=Range*6
            if RoF==1 and AP>4:
                RoF='flamer'
                Range='n/a'
            if AP==7:
                AP='n/a'
            S=str(S)
            AP=str(AP)
            Range=str(Range)
            RoF=str(RoF)
            print('Assault '+RoF)
            print ('S:'+S+' AP:'+AP+' Range:'+Range+'"')
        if Type==6:
            S=random.randint(4, 10)
            if S<7:
                RoF=random.randint(1, 6)
                AP=random.randint(4, 5)
                if AP==4:
                    AP=random.randint(3, 4)
                if AP==3:
                    AP=random.randint(2, 3)
                if RoF==2:
                    RoF='Small Blast'
                if RoF==1:
                    RoF='Large Blast'
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
        Loot=Loot+1
    if LootCrate==3:
        ArmourType=random.randint(1, 6)
        if ArmourType<4:
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
        if 3<ArmourType<6:
            AS=random.randint(4, 6)
            print('Exo-Suit')
            AS=str(AS)
            print('AS:'+AS+'+')
            JetPack=random.randint(1, 6)
            if JetPack==6:
                print('Rocket Boots')
            Mount=random.randint(1, 6)
            if Mount==6:
                print('Heavy Weapon Mount')
        if ArmourType==6:
            print('Powered Armour')
            AS=random.randint(2, 3)
            if AS==2:
                print('Bulky')
            AS=str(AS)
            print('AS:'+AS+'+')
            Mount=random.randint(1, 6)
            if Mount==6:
                print('Heavy Weapon Mount')
        Target=random.randint(1, 6)
        if Target==6:
            print('Targeting Systems')
        Loot=Loot+1

