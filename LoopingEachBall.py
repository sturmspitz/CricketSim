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
              Player(4, "G. Maxwell", 82, "Middle", 34.40, 158.20, 70,  "OB", 27.07, 21.60),
              Player(5, "P. Handscomb", 70, "Middle", 33.00, 100, 20, "None", 99, 99),
              Player(6, "M. Stoinis", 60, "Middle", 15.11, 116.23, 66, "Med", 35.44, 25.5),
              Player(7, "N. Coulter-Nile", 60, "Lower", 13.63, 125.00, 78, "RF", 23.58, 17.1),
              Player(8, "P. Cummins", 45, "Lower", 5.00, 94.59, 81, "RF", 21.24, 18.2),
              Player(9, "J. Richardson", 55, "Lower", 13.00, 216.66, 72, "RF", 31.88, 22.6),
              Player(10, "J. Behrendorff", 30,"Lower", 0, 0, 83, "LFM", 16.71, 13.7),
              Player(11, "A. Zampa", 30, "Lower", 11.50, 88.46, 79, "LB", 19.43, 19.3)]



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
    def __init__(self, batID, batrating, batruns, batballs, batSR, howout, isstriker, isnonstriker, isout, hasbatted):
        self.batID = batID
        self.batrating = batrating
        self.batruns = batruns
        self.batballs = batballs
        self.batSR = batSR
        self.howout = howout
        self.isstriker = isstriker
        self.isnonstriker = isnonstriker
        self.isout = isout
        self.hasbatted = hasbatted
        self.list = [batID, batrating, batruns, batballs, batSR, howout, isstriker, isnonstriker, isout, hasbatted] #new list item
    def __getitem__(self,index): #magic that I don't understand, but it works.
        return self.list[index]
    def __iter__(self):
        for elem in self, batID, batrating, batruns, batballs, batSR, howout, isstriker, isnonstriker, isout, hasbatted:
            yield elem
            

BatterList = [Batsman(1, 0, 0, 0, 0, 0, False, False, False, False), Batsman(2, 0, 0, 0, 0, 0, False, False, False, False), Batsman(3, 0, 0, 0, 0, 0, False, False, False, False),
              Batsman(4, 0, 0, 0, 0, 0, False, False, False, False), Batsman(5, 0, 0, 0, 0, 0, False, False, False, False), Batsman(6, 0, 0, 0, 0, 0, False, False, False, False),
              Batsman(7, 0, 0, 0, 0, 0, False, False, False, False), Batsman(8, 0, 0, 0, 0, 0, False, False, False, False), Batsman(9, 0, 0, 0, 0, 0, False, False, False, False),
              Batsman(10, 0, 0, 0, 0, 0, False, False, False, False), Batsman(11, 0, 0, 0, 0, 0, False, False, False, False)]

class Bowler(object):
    def __init__(self, bowlID, bowlrating, bowlballs, bowlmaiden, bowlruns, bowlwickets, isbowler, lastbowler, maxed):
        self.bowlID = bowlID
        self.bowlrating = bowlrating
        self.bowlballs = bowlballs
        self.bowlmaiden = bowlmaiden
        self.bowlruns = bowlruns
        self.bowlwickets = bowlwickets
        self.isbowler = isbowler
        self.lastbowler = lastbowler
        self.maxed = maxed
        self.list = [bowlID, bowlrating, bowlballs, bowlmaiden, bowlruns, bowlwickets, isbowler, lastbowler, maxed] #new list item
    def __getitem__(self,index): #magic that I don't understand, but it works.
        return self.list[index]
    def __iter__(self):
        for elem in self, bowlID, bowlrating, bowlballs, bowlmaiden, bowlruns, bowlwickets, isbowler, lastbowler, maxed:
            yield elem
            

BowlerList = [Bowler(1, 0, 0, 0, 0, 0, False, False, False), Bowler(2, 0, 0, 0, 0, 0, False, False, False), Bowler(3, 0, 0, 0, 0, 0, False, False, False),
              Bowler(4, 0, 0, 0, 0, 0, False, False, False), Bowler(5, 0, 0, 0, 0, 0, False, False, False), Bowler(6, 0, 0, 0, 0, 0, False, False, False),
              Bowler(7, 0, 0, 0, 0, 0, False, False, False), Bowler(8, 0, 0, 0, 0, 0, False, False, False), Bowler(9, 0, 0, 0, 0, 0, False, False, False),
              Bowler(10, 0, 0, 0, 0, 0, False, False, False), Bowler(11, 0, 0, 0, 0, 0, False, False, False)]

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



print ("Welcome to {} where tonight {} are set to face off against {} in what promises to be a thrilling clash.".format((HomeTeam.arena), (HomeTeam.name), (AwayTeam.name)))
print ('')

print ("{} and {} are in the middle for the toss.".format(HomePlayer[0].name, AwayPlayer[0].name))

print ('The coin is tossed...')
print ('The call from {} is Tails.'.format(AwayPlayer[0].name))

if toss == 0:
    print ('And its Heads! {} have won the toss.'.format(teamwinner.name))
else:
    print ('And its Tails! {} have called correctly and won the toss.'.format(teamwinner.name))

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

print ('The {} openers are making their way out to the middle. Its going to be {} to face the first ball.'.format(Batteam.name, Batter[0].name))
print("")

#Links Players to Players
n=0
while (n < 11):
   (BatterList[n].batID) = (Batter[n].name)
   n = n + 1
n=0
while (n < 11):
   (BowlerList[n].bowlID) = (BowlPlayer[n].name)
   n = n + 1
n=0
while (n < 11):
   (BatterList[n].batrating) = (Batter[n].batrating)
   n = n + 1
n=0
while (n < 11):
   (BowlerList[n].bowlrating) = (BowlPlayer[n].bowlrating)
   n = n + 1

#Start Of Innings Setup

import decimal
from decimal import *
value = Decimal("0.1")+Decimal("0.1")+Decimal("0.1")

over = Decimal(0)
gameover = Decimal(0)
NonStriker = 0
CurrentBowler = 0
LastBowler = 0
LastOut = 0
Striker = 0
wickets = 0
FOW = 0
runs = 0
overruns = 0
overwickets = 0
score =+ runs
Caught = 0
Bowled = 0
LBW = 0
Stumped = 0
Runout = 0
ObstructingtheField = 0
HitWicket = 0
n = 0
isout = bool(1)
isstriker = bool(2)
isbowler = bool(3)
lastbowler = bool(4)

#Determining Bowler
n = 10
while (n >= 0):
    if (BowlerList[n].lastbowler) == False and (BowlerList[n].bowlrating) >=50: 
        (BowlerList[n].isbowler) = True
        break
    if (BowlerList[n].lastbowler) == True or (BowlerList[n].bowlrating) <=50: 
        n = n - 1
n = 10
while (n >= 0):
    if (BowlerList[n].isbowler) == True:
        CurrentBowler = (BowlerList[n]) 
        break
    if (BowlerList[n].isbowler) == False:
        n = n - 1

#Determining LAstBowler
n = 10
while (n >= 0):
    if (BowlerList[n].isbowler) == False: 
        LastBowler = (BowlerList[n])
        break
    else:
        n = n - 1
        
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

#Game Conditions
endinnings = False

    
#Repeating Overs 1-20
while (gameover < Decimal("19.1")):
    while (over < Decimal("0.7")):
        if wickets >= 10:
            endinnings = True
            break
        over += Decimal("0.1")
        gameover += Decimal("0.1")
        if over == Decimal("0.1"):
            overruns = 0
            overwickets = 0
        #Ball 
        import random
        OutcomeList1 = [0] *301 + [1] *411 + [2] *78 + [3] *6 + [4] *103 + [5] *2 + [6] *42 + [8] *57
        OutcomeList = [0] *301 + [1] *411 + [2] *78 + [3] *6 + [4] *103 + [5] *2 + [6] *42 + [8] *57
        DismisalList = ['Caught'] *2996 + ['Bowled'] *990 + ['Runout'] *494 + ['LBW'] *364 + ['Stumped'] *161 + ['HitWicket'] *8 + ['ObstructingtheField'] *1
        result = random.choice(OutcomeList)
        if result ==8:
            dismisal = random.choice(DismisalList)
        (Striker.hasbatted) = True
        (Striker.isstriker) = True
        (NonStriker.hasbatted) = True
        (NonStriker.isnonstriker) = True
        #Result of Ball consequences
        if result != 8:
            runs += result
            overruns += result
            (Striker.batruns) += int(result)
            (Striker.batballs) += 1
            (CurrentBowler.bowlruns) += int(result)
            (CurrentBowler.bowlballs) += Decimal("0.1")
        elif result ==8:
            wickets += 1
            overwickets += 1
            (Striker.howout) = dismisal
            (Striker.batballs) += 1
            (Striker.isout) = True
            LastOut = Striker
            (CurrentBowler.bowlballs) += Decimal("0.1")
            (CurrentBowler.bowlwickets) += 1
            

            
        if (result == 0):
            Comm = ("{}  (0)   {} to {}, no run.")
        elif (result == 1):
            Comm = ("{}  (1)   {} to {}, 1 run.")
        elif (result == 2):
            Comm = ("{}  (2)   {} to {}, 2 runs.")
        elif (result == 3):
            Comm = ("{}  (3)   {} to {}, 3 runs.")
        elif (result == 4):
            Comm = ("{}  (4)   {} to {}, FOUR runs.")
        elif (result == 5):
            Comm = ("{}  (5)   {} to {}, 5 runs.")
        elif (result == 6):
            Comm = ("{}  (6)   {} to {}, SIX runs.")
        else:
            Comm = ("{}  (W)   {} to {}, OUT.")

        
     
        print(Comm.format(gameover, CurrentBowler.bowlID, Striker.batID))
           # if (Striker.batruns)>= 50: print("And that's his 50! Wonderful Innings!")
         #TRY TO WORK THIS OUT


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
        #End of Over Events
        if over == Decimal("0.6"):
            Striker, NonStriker = NonStriker, Striker # Rotates Strike
            over -= Decimal("0.6")
            gameover += Decimal("0.4")
            if overruns == 0:
                (CurrentBowler.bowlmaiden) += 1
            (CurrentBowler.bowlballs) += Decimal("0.4")
            (CurrentBowler.isbowler) = False
            (CurrentBowler.lastbowler) = True
            (LastBowler.lastbowler) = False
            if (CurrentBowler.bowlballs) >= Decimal("4.0"):
                (CurrentBowler.maxed) = True
        #Determines Next Bowlers
        if (CurrentBowler.isbowler) == False and (CurrentBowler.lastbowler) == True:
            CurrentBowler = 0
            LastBowler = 0
            n = 10
            while (n >=0):
                if (BowlerList[n].lastbowler) == False and (BowlerList[n].maxed) == False and (BowlerList[n].bowlrating) >=50: 
                    (BowlerList[n].isbowler) = True
                    break
                if (BowlerList[n].lastbowler) == True or (BowlerList[n].maxed) == True or (BowlerList[n].bowlrating) <=50:  
                    n = n - 1
        if CurrentBowler == 0:
            n = 10
            while (n >=0):
                if (BowlerList[n].isbowler) == True and (BowlerList[n].lastbowler) == False:
                    CurrentBowler = (BowlerList[n]) 
                    break
                else:
                    n = n - 1
        if LastBowler == 0:
            n = 10
            while (n >=0):
                if (BowlerList[n].isbowler) == False and (BowlerList[n].lastbowler) == True:
                    LastBowler = (BowlerList[n])
                    break
                else:
                    n = n - 1
            
            break
    if endinnings == True:
        print("")
        print("END OF INNINGS | {}: {}/{} from {} Overs".format(Batteam.name, runs, wickets, gameover))
        print("")
        break
    if gameover >= Decimal("1.0"):
        print("")
        print("END OF OVER: {:2.0f} | {} Runs {} Wkt | {}: {}/{}".format(gameover, overruns, overwickets, Batteam.name, runs, wickets))
        print("{:20s}{:2.0f}({:2.0f}) | {:20s}{:1.0f}-{:1.0f}-{:2.0f}-{:1.0f}".format(Striker.batID, Striker.batruns, Striker.batballs, CurrentBowler.bowlID, CurrentBowler.bowlballs, CurrentBowler.bowlmaiden, CurrentBowler.bowlruns, CurrentBowler.bowlwickets))
        print("{:20s}{:2.0f}({:2.0f}) | {:20s}{:1.0f}-{:1.0f}-{:2.0f}-{:1.0f}".format(NonStriker.batID, NonStriker.batruns, NonStriker.batballs, LastBowler.bowlID, LastBowler.bowlballs, LastBowler.bowlmaiden, LastBowler.bowlruns, LastBowler.bowlwickets))
        if overwickets >= 0 and wickets >= 1:
            print("Last Wicket: {}  {}({}) - {}".format(LastOut.batID, LastOut.batruns, LastOut.batballs, LastOut.howout))
        print("")
    if gameover == Decimal("20.0"):
        print("")
        print("END OF INNINGS | {}: {}/{} from {} Overs".format(Batteam.name, runs, wickets, gameover))
        print("")
        break
 
print("{} Innings (20 overs maximum)".format(Batteam.name))
print ("-" *60)
print("{:<30}{:>5}{:>5}{:>5}{:>5}{:>9} |".format("BATSMAN", "R", "B", "4s", "6s", "SR"))
n = 0
while (n<11):
    if (BatterList[n].hasbatted) == True:
        print("{:<30}{:5.0f}{:5.0f}{:5.0f}{:5.0f}{:9.2f} |".format(BatterList[n].batID,BatterList[n].batruns,BatterList[n].batballs, 0, 0, (BatterList[n].batruns/BatterList[n].batballs)*100))
        n = n + 1
        if n == 10:
            break
    if (BatterList[n].hasbatted) == False:
        print("{:<59} |".format(BatterList[n].batID))
        n = n + 1
        if n == 10:
            break
print("TOTAL            {}/{} ({} Overs, RR: {:2.2f})".format(runs, wickets, gameover, (runs/gameover)))

print("")

print("{:<30}{:>5}{:>5}{:>5}{:>5}{:>9} |".format("BOWLING", "O", "M", "R", "W", "ECO"))
n = 10
while (n>=0):
    if (BowlerList[n].bowlballs) >= Decimal("0.1"):
        print("{:<30}{:5.0f}{:5.0f}{:5.0f}{:5.0f}{:9.2f} |".format(BowlerList[n].bowlID,BowlerList[n].bowlballs ,BowlerList[n].bowlmaiden, BowlerList[n].bowlruns, BowlerList[n].bowlwickets, (BowlerList[n].bowlruns/BowlerList[n].bowlballs)))
        n = n - 1
        if n == 0:
            break
    if (BowlerList[n].bowlballs) <= Decimal("0.0"):
        break
print("-" *60)
print("-" *60)


 
