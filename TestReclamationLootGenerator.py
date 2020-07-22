import random
Loot=0
while Loot<3:
    LootCrate=random.randint(1,4)
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
        Type = random.randint(1, 7)
        if Type < 3:
            print ('Close Combat Weapon')
            STR = random.randint(0, 3)
            AP = random.randint(0, 5)
            AGI= random.randint(0, 2)
            MAC = random.randint(-1, +1)
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
            STR=random.randint(3, 5)
            AP=random.randint(1, 3)
            if AP==3:
                AP=random.randint(3, 4)
            if AP==4:
                AP=random.randint(4, 5)
            Range=random.randint(3, 6)
            Range=Range*6
            STR=str(STR)
            AP=str(AP)
            Range=str(Range)
            print ('STR:'+STR+' AP:'+AP+' Range:'+Range+'"')
        if Type==4:
            print ('Pistol')
            STR=random.randint(2, 5)
            AP=random.randint(0, 3)
            if AP==3:
                AP=random.randint(3, 4)
            if AP==4:
                AP=random.randint(4, 5)
            Range=random.randint(1, 3)
            Range=Range*6
            STR=str(STR)
            AP=str(AP)
            Range=str(Range)
            print ('STR:'+STR+' AP:'+AP+' Range:'+Range+'"')
        if Type==5:
            RoF=random.randint(1, 3)
            STR=random.randint(2, 5)
            AP=random.randint(0, 3)
            if AP==3:
                AP=random.randint(3, 4)
            if AP==4:
                AP=random.randint(4, 5)
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
                RoF=random.randint(1, 6)
                AP=random.randint(2, 3)
                if AP==3:
                    AP=random.randint(3, 4)
                if AP==4:
                    AP=random.randint(4, 5)
                if RoF==2:
                    RoF='Small Blast'
                if RoF==1:
                    RoF='Large Blast'
            if STR>6:
                RoF=random.randint(1, 2)
                AP=random.randint(3, 4)
                if AP==4:
                    AP=random.randint(4, 5)
            Range=random.randint(4, 8)
            Range=Range*6
            STR=str(STR)
            AP=str(AP)
            Range=str(Range)
            RoF=str(RoF)
            print('Heavy '+RoF)
            print ('STR:'+STR+' AP:'+AP+' Range:'+Range+'"')
        if Type==7:
            STR=random.randint(1, 5)
            AP=random.randint(0, 1)
            if AP==1:
                AP=random,randint(1, 2)
            if AP==2:
                AP=random,randint(2, 3)
            if AP==3:
                AP=random,randint(3, 4)
            if AP==4:
                AP=random,randint(4, 5)
            RoF=random.randint(1, 6)
            if RoF<5:
                RoF='Small Blast'
            if RoF>4:
                RoF='Large Blast'
            STR=str(STR)
            AP=str(AP)
            RoF=str(RoF)
            if STR<3:
                Special=random.randint(1,3)
                if Special==1:
                    print('Flash Grenade '+RoF)
                if Special==2:
                    print('Smoke Grenade '+RoF)
                if Special==3:
                    print('Concussion Grenade '+RoF)
            if STR>2:
                print('Grenade '+RoF)
                print('STR:'+STR+' AP:'+AP)
        Loot=Loot+1
    if LootCrate==3:
        ArmourType=random.randint(1,7)
        if ArmourType<4:
            print('Combat Plate')
            ARM=random.randint(1, 3)
            if ARM==3:
                ARM=random.randint(3, 4)
            if ARM==4:
                ARM=random.randint(4, 5)
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
            JetPack=random.randint(1, 6)
            if Jetpack==6:
                MVE=MVE*2
            ARM=str(ARM)
            MVE=str(MVE)
            AGI=str(AGI)
            print('ARM:'+ARM+' MVE:'+MVE+'" AGI:'+AGI)
            if Jetpack==6:
                print('Jetpack')
        if 3<ArmourType<6:
            ARM=random.randint(1, 3)
            print('Exo-Suit')
            MVE=random.randint(7, 12)-ARM
            if MVE > 8:
                MVE = 8
            if MVE < 6:
                MVE = 6
            AGI=random.randint(1, 6)-ARM
            if AGI < 0:
                AGI=0
            if AGI > 2:
                AGI=2
            STR=random.randint(0, 2)
            JetPack=random.randint(1, 6)
            if Jetpack==6:
                MVE=MVE*2
            STR=str(STR)
            ARM=str(ARM)
            MVE=str(MVE)
            AGI=str(AGI)
            print('ARM:'+ARM+' MVE:'+MVE+'" AGI:+'+AGI+' STR=+'+STR)
            if Jetpack==6:
                print('Jetpack')
            Hvy=random.randint(1, 6)
            if Hvy==6:
                print('Heavy Weapon Mount')
        if ArmourType>5:
            print('Powered Armour')
            ARM=random.randint(4, 5)
            MVE=random.randint(7, 12)-ARM
            if MVE > 6:
                MVE = 6
            if MVE < 4:
                MVE = 4
            AGI=random.randint(1, 6)-ARM
            if AGI > 0:
                AGI=0
            if AGI < -1:
                AGI=-1
            STR=random.randint(0, 2)
            TUF=random.randint(0, 2)
            STR=str(STR)
            ARM=str(ARM)
            MVE=str(MVE)
            AGI=str(AGI)
            TUF=str(TUF)
            print('ARM:'+ARM+' MVE:'+MVE+'" AGI:'+AGI+' STR=+'+STR+' TUF:+'+TUF)
            Hvy=random.randint(1, 6)
            if Hvy==6:
                print('Heavy Weapon Mount')
        Aim=random.randint(1, 6)
        if Aim==6:
            print('Targeting Systems')
        Loot=Loot+1
    if LootCrate==4:
        VehicleType=random.randint(1, 3)
        if VehicleType==1:
            print('Cavalry')
            MVE=random.randint(10, 14)
            TUF=random.randint(0, 2)
            Special=random.randint(1, 3)
            if Special==1:
                Specia
            
            
            

