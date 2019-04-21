import time 

class Team(object):
    def __init__(self, name, record, arena): 
        self.name = name
        self.record = record
        self.arena = arena
        self.list = [name, record, arena] #new list item
    def __getitem__(self,index): #magic that I don't understand, but it works.
        return self.list[index]
    def __iter__(self):
        for elem in self, name, record, arena:
            yield elem


HomeTeam = Team('Australia', '0-0', 'The Sydney Cricket Ground')
AwayTeam = Team('England', '0-0', 'Lords')

class Player(object):
    def __init__(self, playerid, name, batrating, battype, batave, batsr, bowlrating, bowltype, bowlave, bowlsr):
        self.playerid = playerid
        self.name = name
        self.batrating = batrating
        self.battype = battype
        self.batave = batave
        self.batsr = batsr
        self.bowlrating = bowlrating
        self.bowltype= bowltype
        self.bowlave = bowlave
        self.bowlsr = bowlsr
        self.list = [playerid, name, batrating, battype, batave, batsr, bowlrating, bowltype, bowlave, bowlsr] #new list item
    def __getitem__(self,index): #magic that I don't understand, but it works.
        return self.list[index]
    def __iter__(self):
        for elem in self, playerid, name, batrating, battype, batave, batsr, bowlrating, bowltype, bowlave, bowlsr:
            yield elem
    

HomePlayer = [Player(1, 'D. Warner', 77, "Open", 26.74, 140.10, 20,  "LB", 99, 99),
              Player(2, "A. Finch", 84, "Open", 37.13, 155.87, 52,  "LAO", 99, 99),
              Player(3, "D. Short", 73, "Open", 32.88, 120.81, 50, "SLAC", 50.33, 38.00),
              Player(4, "G. MAxwell", 82, "Middle", 34.40, 158.20, 70,  "OB", 27.07, 21.60),
              Player(5, "P. Handscomb", 70, "Middle", 33.00, 100, 20, "None", 99, 99),
              Player(6, "M. Stoinis", 60, "Middle", 15.11, 116.23, 66, "Med", 35.44, 25.5),
              Player(7, "N. Coulter-Nile", 60, "Lower", 13.63, 125.00, 78, "RF", 23.58, 17.1),
              Player(8, "P. Cummins", 45, "Lower", 5.00, 94.59, 81, "RF", 21.24, 18.2),
              Player(9, "J. Richardson", 55, "Lower", 13.00, 216.66, 72, "RF", 31.88, 22.6),
              Player(10, "J. Behrendorff", 30,"Lower", 0, 0, "LFM", 83, 16.71, 13.7),
              Player(11, "A. Zampa", 30, "Lower", 11.50, 88.46, "LB", 79, 19.43, 19.3)]



AwayPlayer = [Player(101, 'J. Roy', 75, "Middle", 23.32, 145.11, 20, "None", 99, 99),
              Player(102, "J. Buttler", 80,  "Open", 26.80, 138.15, 20, "None", 99, 99),
              Player(103, "A. Hales", 79, "Open", 31.01, 136.65, 20, "Med", 99, 99),
              Player(104, "E. Morgan", 73,  "Middle", 27.82, 130.14, 20, "None", 99, 99),
              Player(105, "B. Stokes", 68, "Middle", 15.46, 130.33, 60,  "RFM", 49.60, 33.4),
              Player(106, "J. Bairstow", 77, "Middle", 27.00, 130.20, 20,  "None", 99, 99),
              Player(107, "D. Willey", 65,  "Middle", 13.83, 131.74, 81, "LFM", 21.64, 15.8),
              Player(108, "C. Jordan", 59, "Lower", 12.92, 116.66, 75, "RFM", 25.13, 17.5),
              Player(109, "L. Plunkett", 40, "Lower", 6.00, 123.52, 79, "RF", 25.08, 19.0),
              Player(110, "J. Ball", 30, "Lower", 0, 0, 68, "RFM", 41.50, 21.0),
              Player(111, "A. Rashid", 20, "Lower", 7.83, 85.45, 78, "LB", 23.97, 19.60)]

class Batsman(object):
    def __init__(self, batID, batruns, batballs, batSR, isstriker, isnonstriker, isout, hasbatted):
        self.batID = batID
        self.batruns = batruns
        self.batballs = batballs
        self.batSR = batSR
        self.isstriker = isstriker
        self.isnonstriker = isnonstriker
        self.isout = isout
        self.hasbatted = hasbatted
        self.list = [batID, batruns, batballs, batSR, isstriker, isnonstriker, isout, hasbatted] #new list item
    def __getitem__(self,index): #magic that I don't understand, but it works.
        return self.list[index]
    def __iter__(self):
        for elem in self, batID, batruns, batballs, batSR, isstriker, isnonstriker, isout, hasbatted:
            yield elem
            

BatterList = [Batsman(1, 0, 0, 0, False, False, False, False), Batsman(2, 0, 0, 0, False, False, False, False), Batsman(3, 0, 0, 0, False, False, False, False),
              Batsman(4, 0, 0, 0, False, False, False, False), Batsman(5, 0, 0, 0, False, False, False, False), Batsman(6, 0, 0, 0, False, False, False, False),
              Batsman(7, 0, 0, 0, False, False, False, False), Batsman(8, 0, 0, 0, False, False, False, False), Batsman(9, 0, 0, 0, False, False, False, False),
              Batsman(10, 0, 0, 0, False, False, False, False), Batsman(11, 0, 0, 0, False, False, False, False)]

class Bowler(object):
    def __init__(self, bowlID, bowlballs, bowlruns, bowlwickets, isbowler, lastbowler, maxed):
        self.bowlID = bowlID
        self.bowlballs = bowlballs
        self.bowlruns = bowlruns
        self.bowlwickets = bowlwickets
        self.isbowler = isbowler
        self.lastbowler = lastbowler
        self.maxed = maxed
        self.list = [bowlID, bowlballs, bowlruns, bowlwickets, isbowler, lastbowler, maxed] #new list item
    def __getitem__(self,index): #magic that I don't understand, but it works.
        return self.list[index]
    def __iter__(self):
        for elem in self, bowlID, bowlballs, bowlruns, bowlwickets, isbowler, lastbowler, maxed:
            yield elem
            

BowlerList = [Bowler(1, 0, 0, 0, False, False, False), Bowler(2, 0, 0, 0, False, False, False), Bowler(3, 0, 0, 0, False, False, False),
              Bowler(4, 0, 0, 0, False, False, False), Bowler(5, 0, 0, 0, False, False, False), Bowler(6, 0, 0, 0, False, False, False),
              Bowler(7, 0, 0, 0, False, False, False), Bowler(8, 0, 0, 0, False, False, False), Bowler(9, 0, 0, 0, False, False, False),
              Bowler(10, 0, 0, 0, False, False, False), Bowler(11, 0, 0, 0, False, False, False)]

import random 
toss = random.randint(0,1)
if toss == 0:
    winner = HomePlayer
    teamwinner = HomeTeam
    loser = AwayPlayer
    teamloser = AwayTeam

else:
    loser = HomePlayer
    teamloser = HomeTeam
    winner = AwayPlayer
    teamwinner = AwayTeam

#print(winner[0].name) format for winner
#print(teamwinner.name)

import time
time.sleep(10)

print ("Welcome to {} where tonight {} are set to face off against {} in what promises to be a thrilling clash.".format((HomeTeam.arena), (HomeTeam.name), (AwayTeam.name)))
print ('')

print ("{} and {} are in the middle for the toss.".format(HomePlayer[0].name, AwayPlayer[0].name))
time.sleep(1)
print ('The coin is tossed...')
print ('The call from {} is Tails.'.format(AwayPlayer[0].name))
time.sleep(1)
if toss == 0:
    print ('And its Heads! {} have won the toss.'.format(teamwinner.name))
else:
    print ('And its Tails! {} have called correctly and won the toss.'.format(teamwinner.name))
time.sleep(1)
import random
decision = random.randint(0,1)
if decision == 0:
    Batter = winner
    Batteam = teamwinner
    BowlPlayer = loser
    Bowlteam = teamloser
    
else:
    Batter = loser
    Batteam = teamloser
    BowlPlayer = winner
    Bowlteam = teamwinner
    
if decision == 0:
    print ('{} have elected to Bat first.'.format(Batteam.name))
else:
    print ('{} have decided to have a bowl.'.format(Bowlteam.name))
print ('')
time.sleep(1)
print ('The {} openers are making their way out to the middle. Its going to be {} to face the first ball.'.format(Batteam.name, Batter[0].name))
print("")
time.sleep(1)
#Links Batsman to Players
(BatterList[0].batID) = (Batter[0].name)
(BatterList[1].batID) = (Batter[1].name)
(BatterList[2].batID) = (Batter[2].name)
(BatterList[3].batID) = (Batter[3].name)
(BatterList[4].batID) = (Batter[4].name)
(BatterList[5].batID) = (Batter[5].name)
(BatterList[6].batID) = (Batter[6].name)
(BatterList[7].batID) = (Batter[7].name)
(BatterList[8].batID) = (Batter[8].name)
(BatterList[9].batID) = (Batter[9].name)
(BatterList[10].batID) = (Batter[10].name)

#Links Bowlers to Players
(BowlerList[0].bowlID) = (BowlPlayer[0].name)
(BowlerList[1].bowlID) = (BowlPlayer[1].name)
(BowlerList[2].bowlID) = (BowlPlayer[2].name)
(BowlerList[3].bowlID) = (BowlPlayer[3].name)
(BowlerList[4].bowlID) = (BowlPlayer[4].name)
(BowlerList[5].bowlID) = (BowlPlayer[5].name)
(BowlerList[6].bowlID) = (BowlPlayer[6].name)
(BowlerList[7].bowlID) = (BowlPlayer[7].name)
(BowlerList[8].bowlID) = (BowlPlayer[8].name)
(BowlerList[9].bowlID) = (BowlPlayer[9].name)
(BowlerList[10].bowlID) = (BowlPlayer[10].name)



#Start Of Innings Setup

import decimal
from decimal import *
value = Decimal("0.1")+Decimal("0.1")+Decimal("0.1")

over = Decimal(0)
gameover = Decimal(0)
NonStriker = 0
CurrentBowler = 0
LastBowler = 0
Striker = 0
wickets = 0
runs = 0
score =+ runs
n = 0
isout = bool(1)
isstriker = bool(2)
isbowler = bool(3)
lastbowler = bool(4)

#Determining Bowler
n = 0
while (n < 11):
    if (BowlerList[n].lastbowler) == False: 
        (BowlerList[n].isbowler) = True
        break
    if (BowlerList[n].lastbowler) == True: 
        n = n + 1
n = 0
while (n < 11):
    if (BowlerList[n].isbowler) == True:
        CurrentBowler = (BowlerList[n]) 
        break
    if (BowlerList[n].isbowler) == False:
        n = n + 1
    
        
#Determines who the Striker is
n = 0
while (n < 11):
    if (BatterList[n].hasbatted) == False:
        (BatterList[n].isstriker) = True
        break 
    if (BatterList[n].hasbatted) == True:
        n = n + 1

n = 0
while (n <11):
    if (BatterList[n].isstriker) == True:
        Striker = (BatterList[n])
        break
    if (BatterList[n].isstriker) == False:
        n = n + 1



#Determines who the NonStriker is
n = 0
while (n < 11):
    if (BatterList[n].isstriker) == False:
        (BatterList[n].isnonstriker) = True
        break 
    if (BatterList[n].isstriker) == True:
        n = n + 1

n = 0
while (n <11):
    if (BatterList[n].isnonstriker) == True:
        NonStriker = (BatterList[n]) 
        break
    if (BatterList[n].isnonstriker) == False:
        n = n + 1
#Repeating Overs 1-20
while (gameover < Decimal("19.1")):
    while (over < Decimal("0.7")):
        over += Decimal("0.1")
        gameover += Decimal("0.1")
        
        #Ball 
        import random
        my_list = [0] *301 + [1] *411 + [2] *78 + [3] *6 + [4] *103 + [5] *2 + [6] *42 + [8] *57

        result = random.choice(my_list)

        (Striker.hasbatted) = True
        (Striker.isstriker) = True
        (NonStriker.hasbatted) = True
        (NonStriker.isnonstriker) = True
        #Result of Ball consequences
        if result != 8:
            runs += result
            (Striker.batruns) += int(result)
            (Striker.batballs) += 1
        elif result ==8:
            wickets += 1
            (Striker.batballs) += 1
            (Striker.isout) = True
            

            
        if (result == 0):
            Comm = ("{} - (0) -  {} to {}, no run.")
        elif (result == 1):
            Comm = ("{} - (1) -  {} to {}, 1 run.")
        elif (result == 2):
            Comm = ("{} - (2) -  {} to {}, 2 runs.")
        elif (result == 3):
            Comm = ("{} - (3) -  {} to {}, 3 runs.")
        elif (result == 4):
            Comm = ("{} - (4) -  {} to {}, FOUR runs.")
        elif (result == 5):
            Comm = ("{} - (5) -  {} to {}, 5 runs.")
        elif (result == 6):
            Comm = ("{} - (6) -  {} to {}, SIX runs.")
        else:
            Comm = ("{} - (W) -  {} to {}, OUT.")

        
     
        print(Comm.format(gameover, CurrentBowler.bowlID, Striker.batID))
        


        #Determines who the batsmen are

        if (Striker.isout) == True:
            Striker = 0
            n = 0
            while (n < 11):
                if (BatterList[n].hasbatted) == False and (BatterList[n].isnonstriker) == False:
                    (BatterList[n].isstriker) = True
                    break 
                if (BatterList[n].hasbatted) == True:
                    n = n + 1

        if Striker == 0:
            n = 0
            while (n <11):
                if (BatterList[n].isstriker) == True and (BatterList[n].hasbatted) == False:
                    Striker = (BatterList[n]) 
                    break
                else:
                    n = n + 1
        if result % 2 == 1:
            Striker, NonStriker = NonStriker, Striker # Rotates Strike

        if over == Decimal("0.6"):
            Striker, NonStriker = NonStriker, Striker # Rotates Strike
            over -= Decimal("0.6")
            gameover += Decimal("0.4")
            (CurrentBowler.lastbowler) = True
            (CurrentBowler.isbowler) = False
            #Determines who the NonStriker is
            n = 0
            while (n < 11):
                if (BowlerList[n].lastbowler) == True:
                    LastBowler = (BowlerList[n])
                    break 
                if (BowlerList[n].lastbowler) == False:
                    n = n + 1
            if  gameover >= Decimal("5.0"):
                (LastBowler.lastbowler) = False
            
                
            
            #Determining Bowler
            n = 0
            while (n < 11):
                if (BowlerList[n].lastbowler) == False: 
                    (BowlerList[n].isbowler) = True
                    break
                if (BowlerList[n].lastbowler) == True: 
                    n = n + 1
            n = 0
            while (n < 11):
                if (BowlerList[n].isbowler) == True:
                    CurrentBowler = (BowlerList[n]) 
                    break
                if (BowlerList[n].isbowler) == False:
                    n = n + 1
            break
    
    print("")
    print("END OF OVER: {} | {} Runs {} Wkt | {}: {}/{}".format(gameover, runs, wickets, Batteam.name, runs, wickets))
    print("{}                          {}({})".format(Striker.batID, Striker.batruns, Striker.batballs))
    print("{}                          {}({})".format(NonStriker.batID, NonStriker.batruns, NonStriker.batballs))
    print("")
    time.sleep(1)
    if over >= Decimal("20.0"):
        break
 


    
 
