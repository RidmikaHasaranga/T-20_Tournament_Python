#toss function
def toss(team1,team2):
    import random
    ntuple = team1, team2
    nlist = list(ntuple)
    global Summary1
    Summary1 = {}
    winToss = random.choice(nlist)
    Summary1["Toss"] = winToss
    print()
    print(f"{winToss} win toss")
    first = ["bat", "ball"]
    choice = random.choice(first)
    print()
    print(f"{winToss} choose to {choice} first")
    print()
    global batFirst
    if choice == "bat":  #Identify First bst team
        batFirst = winToss
        Summary1["Choice"] = "bat"
    else:
        nlist.remove(winToss)
        batFirst = nlist[0]
        Summary1["Choice"] = "ball"

#1st ining function
def FirstIning(batFirst,batFirstTeam,ballerTeam,tPlayers1,tPlayers2):
    import random
    global Summary1Ining
    Summary1Ining = {}
    playerScore = {}
    ballerWicet = {}
    print("First bat team ", batFirst)  #First bat team
    player1 = batFirstTeam[1]
    player2 = batFirstTeam[2]
    playerNum = 2
    print(f"Opening batsmen : {player1},{player2}")
    over = 1
    ballerCount = 0
    ceeper = tPlayers2[1]
    ballers = ballerTeam[10], ballerTeam[9], ballerTeam[8], ballerTeam[7], ballerTeam[6]
    print()
    print(f"ballers {ballers}")
    print(f"Wicet ceeper {ceeper}")
    wicketCount = 0
    expectation = [0, 1, 2, 3, 4, 5, 6, 'NB', 'WD', 'W']
    wType = ("Runout", "Wicket", "Stump", "Lbw", "Catch")
    player1Score = 0
    player2Score = 0
    totalScore = 0
    while over != 21:
        print()
        print(f"over: {over}  baller: {ballers[ballerCount]}")
        ball = 1
        while ball < 7:
            expect = random.choice(expectation)

            if expect == 'W':        #Wicet
                wicketCount += 1
                w = random.choice(wType)
                wicket = random.choice([player1, player2])
                print(f"{wicket} out ({w})")
                if ballers[ballerCount] in ballerWicet:
                    ballerWicet[ballers[ballerCount]] += 1
                else:
                    ballerWicet[ballers[ballerCount]] = 1
                if playerNum == 11:
                    print("All Out")
                    break
                playerNum += 1
                if wicket == player1:
                    print(f"    {player1} {player1Score} runs")
                    playerScore[player1] = player1Score
                    player1 = batFirstTeam[playerNum]
                    print(f"The new batsman {player1}")
                    player1Score = 0

                else:
                    print(f"    {player2} {player2Score} runs")
                    playerScore[player2] = player2Score
                    player2 = batFirstTeam[playerNum]
                    print(f"The new batsman {player2}")
                    player2Score = 0



            elif expect == 'NB':        #No Ball
                print("No Ball")
                ball -= 1
                totalScore += 1

            elif expect == 'WD':        #Wide Ball
                print("Wide Ball")
                ball -= 1
                totalScore += 1

            elif expect == 0:
                print("Dot Ball")

            elif expect == 1:
                print("1 run")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 1

            elif expect == 2:
                print("2 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 2

            elif expect == 3:
                print("3 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 3

            elif expect == 4:
                print("4 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 4

            elif expect == 5:
                print("5 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 5

            elif expect == 6:
                print("6 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 6

            ball += 1   #End over

        if wicketCount == 10:
            break
        ballerCount += 1
        if ballerCount == 5:
            ballerCount = 0
        over += 1

    print()
    print(f"Score {totalScore}  wicket {wicketCount}")
    print(playerScore)
    print(ballerWicet)
    Summary1Ining["bat"] = batFirst
    Summary1Ining["Tscore"] = totalScore
    Summary1Ining["wicket"] = wicketCount
    Summary1Ining["score"] = playerScore
    Summary1Ining["ball"] = ballerTeam[0]
    Summary1Ining["wicketby"] = ballerWicet
    global target
    target = totalScore + 1
    #End 1st ining function

#2nd ining function
def SecondIning(batFirst, batFirstTeam, ballerTeam, tPlayers1, tPlayers2):
    import random
    global Summary2Ining
    Summary2Ining = {}
    playerScore = {}
    ballerWicet = {}
    print(batFirst)  # First bat team
    player1 = batFirstTeam[1]
    player2 = batFirstTeam[2]
    playerNum = 2
    print(f"Opening batsmen : {player1},{player2}")
    over = 1
    ballerCount = 0
    ceeper = tPlayers2[1]
    ballers = ballerTeam[10], ballerTeam[9], ballerTeam[8], ballerTeam[7], ballerTeam[6]
    print()
    print(f"ballers {ballers}")
    print(f"Wicet ceeper {ceeper}")
    wicketCount = 0
    expectation = [0, 1, 2, 3, 4, 5, 6, 'NB', 'WD', 'W']
    wType = ("Runout", "Wicket", "Stump", "Lbw", "Catch")
    player1Score = 0
    player2Score = 0
    totalScore = 0
    while over != 21:
        print()
        print(f"over: {over}  baller: {ballers[ballerCount]}")
        ball = 1
        while ball < 7:
            if target == totalScore:
                break
            expect = random.choice(expectation)

            if expect == 'W':  # Wicet
                wicketCount += 1
                w = random.choice(wType)
                wicket = random.choice([player1, player2])
                print(f"{wicket} out ({w})")
                if ballers[ballerCount] in ballerWicet:
                    ballerWicet[ballers[ballerCount]] += 1
                else:
                    ballerWicet[ballers[ballerCount]] = 1
                if playerNum == 11:
                    print("All Out")
                    break
                playerNum += 1
                if wicket == player1:
                    print(f"    {player1} {player1Score} runs")
                    playerScore[player1] = player1Score
                    player1 = batFirstTeam[playerNum]
                    print(f"The new batsman {player1}")
                    player1Score = 0

                else:
                    print(f"    {player2} {player2Score} runs")
                    playerScore[player2] = player2Score
                    player2 = batFirstTeam[playerNum]
                    print(f"The new batsman {player2}")
                    player2Score = 0


            elif expect == 'NB':  # No Ball
                print("No Ball")
                ball -= 1
                totalScore += 1
                if target <= totalScore:
                    break

            elif expect == 'WD':  # Wide Ball
                print("Wide Ball")
                ball -= 1
                totalScore += 1
                if target <= totalScore:
                    break

            elif expect == 0:
                print("Dot Ball")

            elif expect == 1:
                print("1 run")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 1
                if target <= totalScore:
                    break

            elif expect == 2:
                print("2 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 2
                if target <= totalScore:
                    break

            elif expect == 3:
                print("3 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 3
                if target <= totalScore:
                    break

            elif expect == 4:
                print("4 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 4
                if target <= totalScore:
                    break

            elif expect == 5:
                print("5 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 5
                if target <= totalScore:
                    break

            elif expect == 6:
                print("6 runs")
                play = random.choice([player1, player2])
                if play == player1:
                    player1Score += int(expect)
                else:
                    player2Score += int(expect)
                totalScore += 6
                if target <= totalScore:
                    break

            ball += 1  # End over

        if wicketCount == 10:
            break
        ballerCount += 1
        if ballerCount == 5:
            ballerCount = 0
        if target <= totalScore:
            break
        over += 1

    print()
    print(f"Score {totalScore}  wicket {wicketCount}")
    print(playerScore)
    print(ballerWicet)
    Summary2Ining["bat"] = batFirst
    Summary2Ining["Tscore"] = totalScore
    Summary2Ining["wicket"] = wicketCount
    Summary2Ining["score"] = playerScore
    Summary2Ining["ball"] = ballerTeam[0]
    Summary2Ining["wicketby"] = ballerWicet
    global score
    score = totalScore
    #End 2nd ining function

#select match status
file = open("A&B.txt", "r")
status = file.readline()
file.close()
if status == "A1":
    print("Team A")
    y = "A.txt"
    z = "SemiA.txt"
    t1I = 0  #Team index
    t2I = 1

    file = open("A&B.txt", "w")
    file.write("B1")
    file.close()

elif status == "B1":
    print("Team B")
    y = "B.txt"
    z = "SemiB.txt"
    t1I = 0  # Team index
    t2I = 1

    file = open("A&B.txt", "w")
    file.write("A2")
    file.close()

elif status == "A2":
    print("Team A")
    y = "A.txt"
    z = "SemiA.txt"
    t1I = 2  # Team index
    t2I = 3

    file = open("A&B.txt", "w")
    file.write("B2")
    file.close()

elif status == "B2":
    print("Team B")
    y = "B.txt"
    z = "SemiB.txt"
    t1I = 2  # Team index
    t2I = 3

    file = open("A&B.txt", "w")
    file.write("SA")
    file.close()

elif status == "SA":
    print("Team A  Semi Final")
    y = "SemiA.txt"
    z = "Final.txt"
    t1I = 0  # Team index
    t2I = 1

    file = open("A&B.txt", "w")
    file.write("SB")
    file.close()

elif status == "SB":
    print("Team B  Semi Final")
    y = "SemiB.txt"
    z = "Final.txt"
    t1I = 0  # Team index
    t2I = 1

    file = open("A&B.txt", "w")
    file.write("F")
    file.close()

elif status == "F":
    print("Final")
    y = "Final.txt"
    z = "Final.txt"
    t1I = 0  # Team index
    t2I = 1

    file = open("A&B.txt", "w")
    file.write("Finish")
    file.close()

elif status == "Finish":
    print("The tournament is already finish")
    import Second
    Second()

#Find the team players of the two selected teams

file = open(y, "r")
lines = file.readlines()
t1 = lines[t1I]
t2 = lines[t2I]

b = t1.replace("[", "")
c = b.replace("]", "")
d = c.replace("'", "")
e = d.replace(" ", "")
f = list(e.split(","))
team1 = f[0]
tPlayers1 = f


b = t2.replace("[", "")
c = b.replace("]", "")
d = c.replace("'", "")
e = d.replace(" ", "")
f = list(e.split(","))
team2 = f[0]
tPlayers2 = f

file.close()

print("The teams in the match today,")
print(team1)    #Team name
print(team2)


print(tPlayers1)    #Player List
print(tPlayers2)


toss(team1, team2)  #Call toss function

#1st ining variable creating
if batFirst == team1:
    batFirst = team1    #for function
    S_batFirst = team1  #for summary
    batFirstTeam = tPlayers1    #for function
    ballerTeam = tPlayers2  #for function
else:
    batFirst = team2    #for function
    S_batFirst = team2  #for summary
    batFirstTeam = tPlayers2    #for function
    ballerTeam = tPlayers1  #for function


FirstIning(batFirst, batFirstTeam, ballerTeam, tPlayers1, tPlayers2)  #Call 1st ining function


#2nd ining variable creating
if batFirst == team1:
    batFirst = team2
    batFirstTeam = tPlayers2
    ballerTeam = tPlayers1
else:
    batFirst = team1
    batFirstTeam = tPlayers1
    ballerTeam = tPlayers2

print()
print("2nd Ining")
print()

SecondIning(batFirst, batFirstTeam, ballerTeam, tPlayers1, tPlayers2)  #Call 2nd ining function

#select winner
print()
if target <= score:
    print(f"{batFirstTeam[0]} win")
    winner = batFirstTeam[0]
    loser = ballerTeam[0]
    winteam = batFirstTeam #to identify winner team & players
    ining = Summary2Ining #to identify winner bat ining
    winscore = score
    losescore = target - 1
else:
    print(f"{ballerTeam[0]} win")
    winner = ballerTeam[0]
    loser = batFirstTeam[0]
    winteam = batFirstTeam
    ining = Summary1Ining
    winscore = target - 1
    losescore = score

#Print match summary
print()
print("-----Match Summary-----")
print(f"{winner} win the match")
print(Summary1)
print()
print("1st Inning")
print(Summary1Ining)
print()
print("2nd Inning")
print(Summary2Ining)

newfile = open(z, "a")
newfile.write(str(winteam) + "\n")  #store wining team for next match
newfile.close()

#Store summary
sFile = open("Summary.txt", "a")
sFile.write(f"match status {status}\n")
sFile.write(f"{winner} win the match\n")
sFile.write("1st Inning\n")
sFile.write(str(Summary1Ining)+"\n")
sFile.write("2nd Inning\n")
sFile.write(str(Summary2Ining)+"\n")
sFile.write("\n")
sFile.write("\n")
sFile.close()

#Best batsman & baller
#batsman
d1 = Summary1Ining["score"]
maxScore1 = 0
for x in d1:
    if d1[x] > maxScore1:
        maxScore1 = d1[x]
        maxplayer1 = x

d2 = Summary2Ining["score"]
maxScore2 = 0
for x in d2:
    if d2[x] > maxScore2:
        maxScore2 = d2[x]
        maxplayer2 = x
li = []
if maxScore1 > maxScore2:
    li.append(Summary1Ining["bat"]) #country
    li.append(maxplayer1)   #player name
    li.append(maxScore1)    #score
else:
    li.append(Summary2Ining["bat"]) #country
    li.append(maxplayer2)   #player name
    li.append(maxScore2)    #score
bFile = open("bestBatsmen.txt", "a")
bFile.write(str(li)+"\n")
bFile.close()

#baller
d1 = Summary1Ining["wicketby"]
maxWicket1 = 0
for x in d1:
    if d1[x] > maxWicket1:
        maxWicket1 = d1[x]
        maxplayer1 = x

d2 = Summary2Ining["wicketby"]
maxWicket2 = 0
for x in d2:
    if d2[x] > maxWicket2:
        maxWicket2 = d2[x]
        maxplayer2 = x
li = []
if maxWicket1 > maxWicket2:
    li.append(Summary1Ining["ball"]) #country
    li.append(maxplayer1)   #player name
    li.append(maxWicket1)    #wicket
else:
    li.append(Summary2Ining["ball"]) #country
    li.append(maxplayer2)   #player name
    li.append(maxWicket2)    #wicket
bFile = open("bestBallers.txt", "a")
bFile.write(str(li)+"\n")
bFile.close()

#Tournament Standing
tFile = open("Tournament standings.txt", "r")
a = tFile.readline()
b = a.replace("[", "")
c = b.replace("]", "")
d = c.replace("'", "")
e = d.replace(" ", "")
f = e.replace("(", "")
g = f.replace(")", "")
h = list(g.split(","))
index = (0, 2, 4, 6, 8, 10, 12, 14)
for x in index:
    if winner == h[x]:
        y = int(h[x + 1])
        y += winscore
        h[x + 1] = y
    elif loser == h[x]:
        y = int(h[x + 1])
        y += losescore
        h[x + 1] = y

li = []
for x in index:
    s = (h[x], h[x + 1])
    li.append(s)

tFile = open("Tournament standings.txt", "w")
tFile.write(str(li))
tFile.close()
tFile.close()


import Second
Second()