import random
Loot=0
while Loot<3:
    LootCrate=random.randint(1,3)
    print('---------------------')
    if LootCrate==1:
        MAC = random.randint(2, 4)
        RAC = random.randint(2, 4)
        STR = random.randint(2, 4)
        TUF = random.randint(5, 7)
        HP = random.randint(2, 4)
        AGI = random.randint(5, 7)
        ATT = random.randint(1, 3)
        BRV = random.randint(6, 8)

        Role = random.randint(1, 4)
        if Role == 1:
            ATT=ATT+1
            BRV = BRV + 1
            if MAC > RAC:
                MAC = MAC + 1
            if RAC > MAC:
                RAC = RAC + 1
            if RAC == MAC:
                TUF = TUF + 1
            print('Lone Wolf')
        if 1 < Role < 4:
            print('Thug')
        if Role == 4:
            ATT=ATT+1
            BRV = BRV + 2
            print('Sergeant')

        MAC = str(MAC)
        RAC = str(RAC)
        STR = str(STR)
        TUF = str(TUF)
        HP = str(HP)
        AGI = str(AGI)
        ATT = str(ATT)
        BRV = str(BRV)
        print('MAC:' + MAC + ' RAC:' + RAC + ' STR:' + STR + ' TUF:' + TUF + ' HP:' + HP + ' AGI:' + AGI + ' ATT:' + ATT + ' BRV:' + BRV)
        if Role==1:
            Special=random.randint(1, 6)
            if Special==1:
                print('Gunslinger')
            if Special==2:
                print('Sniper')
            if Special==3:
                print('Artificier')
            if Special==4:
                print('Infiltrate')
            if Special==5:
                print('Fearsome')
            if Special==6:
                print('Fury')
        if Role==4:
            Special=random.randint(1, 6)
            if Special==1:
                print('Medic')
            if Special==2:
                print('Rifle Drill')
            if Special==3:
                print('Inspiring Rage')
            if Special==4:
                print('Enormous Presence')
            if Special==5:
                print('Artillery Specialist')
            if Special==6:
                print('Hold The Line')
        Loot=Loot+1
    if LootCrate==2:
        Type = random.randint(1, 6)
        if Type < 3:
            print ('Close Combat Weapon')
            STR = random.randint(0, 1)
            AP = random.randint(0, 3)
            AGI= random.randint(0, 2)
            MAC = random.randint(-2, +1)
            STR=str(STR)
            AP=str(AP)
            AGI=str(AGI)
            MAC=str(MAC)
            print ('STR:+'+STR+' AP:'+AP+' AGI:-'+AGI+' MAC:'+MAC)
            Special=random.randint(1, 6)
            if Special==1:
                print ('Bleed')
            if Special==2:
                print ('Sweep')
            if Special==3:
                print ('Parry')
            if Special==4:
                print ('Stun')
            if Special==5:
                print ('Reach')
            if Special==6:
                print ('Rend')
        if Type==3:
            print ('Rifle')
            STR=random.randint(3, 4)
            AP=random.randint(1, 3)
            Range=random.randint(3, 6)
            Range=Range*6
            STR=str(STR)
            AP=str(AP)
            Range=str(Range)
            print ('STR:'+STR+' AP:'+AP+' Range:'+Range+'"')
        if Type==4:
            print ('Pistol')
            STR=random.randint(2, 4)
            AP=random.randint(0, 3)
            Range=random.randint(1, 3)
            Range=Range*6
            STR=str(STR)
            AP=str(AP)
            Range=str(Range)
            print ('STR:'+STR+' AP:'+AP+' Range:'+Range+'"')
        if Type==5:
            RoF=random.randint(1, 3)
            STR=random.randint(2, 4)
            AP=random.randint(0, 3)
            Range=random.randint(3, 5)
            Range=Range*6
            if RoF==1 and AP<3:
                RoF='flamer'
                Range='n/a'
            STR=str(STR)
            AP=str(AP)
            Range=str(Range)
            RoF=str(RoF)
            print('Assault '+RoF)
            print ('STR:'+STR+' AP:'+AP+' Range:'+Range+'"')
        if Type==6:
            STR=random.randint(4, 10)
            if STR<7:
                RoF=random.randint(1, 4)
                AP=random.randint(2, 3)
                if RoF==2:
                    RoF='Small Blast'
                if RoF==1:
                    RoF='Large Blast'
            if STR>6:
                RoF=random.randint(1, 2)
                AP=random.randint(3, 4)
            Range=random.randint(4, 8)
            Range=Range*6
            STR=str(STR)
            AP=str(AP)
            Range=str(Range)
            RoF=str(RoF)
            print('Heavy '+RoF)
            print ('STR:'+STR+' AP:'+AP+' Range:'+Range+'"')
        Loot=Loot+1
    if LootCrate==3:
        print('Combat Plate')
        ARM=random.randint(1, 3)
        if ARM==3:
            ARM=random.randint(3, 4)
        MVE=random.randint(1, 6)+random.randint(3, 6)-ARM
        if MVE > 6:
            MVE = 6
        if MVE < 4:
            MVE = 4
        AGI=random.randint(1, 6)-ARM
        if AGI > 0:
            AGI=0
        if AGI < -1:
            AGI=-1
        ARM=str(ARM)
        MVE=str(MVE)
        AGI=str(AGI)
        print('ARM:'+ARM+' MVE:'+MVE+'" AGI:'+AGI)
        Loot=Loot+1

