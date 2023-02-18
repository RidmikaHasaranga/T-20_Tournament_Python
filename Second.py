class FormulaError(Exception): pass

def TournamentStanding():
    try:
        file = open("A&B.txt", "r")
        status = file.readline()
        if status == 'A1':
            raise FormulaError("No data yet as the Tournament has not started!")
        print("Tournament Standings")
        tFile = open("Tournament standings.txt", "r")
        a = tFile.readline()
        tFile.close()
        b = a.replace("[", "")
        c = b.replace("]", "")
        d = c.replace("'", "")
        e = d.replace(" ", "")
        f = e.replace("(", "")
        g = f.replace(")", "")
        h = list(g.split(","))
        index = (0, 2, 4, 6, 8, 10, 12, 14)
        scoreli = []
        for x in index:
            y = int(h[x + 1])
            scoreli.append(y)

        scoreli.sort(reverse=True)  # Score Descendin order

        y = 1
        for z in scoreli:
            for x in index:
                if z == int(h[x + 1]):
                    print(y, ")", h[x])
                    y += 1
                    if y == 9:
                        start()

    except FormulaError as e:
        print(e)
        start()


def bestBatsman():
    try:
        file = open("A&B.txt", "r")
        status = file.readline()
        file.close()
        if status != 'Finish':
            raise FormulaError("No data yet as the Tournament is not over!")
        print()
        print("Bets Batsmen in the tournament")
        print()
        file = open("bestBatsmen.txt", "r")
        a = file.readline()
        while a:
            b = a.replace("[", "")
            c = b.replace("]", "")
            d = c.replace("'", "")
            f = d.replace(" ", "")
            e = list(f.split(","))
            print(e[1] + "   (" + e[0] + ")")
            a = file.readline()

    except FormulaError as e:
        print(e)
        print()
        start()

def bestBollers():
    print()
    print("Bets Ballers in the tournament")
    print()
    file = open("bestBallers.txt", "r")
    a = file.readline()
    while a:
        b = a.replace("[", "")
        c = b.replace("]", "")
        d = c.replace("'", "")
        f = d.replace(" ", "")
        e = list(f.split(","))
        print(e[1] + "   (" + e[0] + ")")
        a = file.readline()
    start()

def summary():
    try:
        import os
        file = open("Summary.txt", "r")
        filesize = os.path.getsize("Summary.txt")
        if filesize == 0:
            raise FormulaError("No data yet as the tournament has not started")
        a = file.readline()
        while a:
            print(a)
            a = file.readline()
        start()
    except FormulaError as e:
        print(e)
        print()
        start()

def start():
    try:
        print()
        print("Welcome to T20-Tournament System")
        print()
        print("Please select the number of the action you want to execute")
        print()
        print("1)Generate Random Match")
        print("2)Watch Tournament Standings")
        print("3)Tournament summary up to now")
        print("4)Best batsmen & ballers in the tournament")
        print("5)Exit")
        print("6)Delete tournament details")
        print()
        x = int(input("Enter the number of the action you want to execute : "))
        if x > 6 or x < 1:
            raise FormulaError ("Input not in range")
        print()
        if x == 1:
            import os
            os.system("Match.py")
        elif x == 2:
            TournamentStanding()
        elif x == 3:
            summary()
        elif x == 4:
            bestBatsman()
            bestBollers()
        elif x == 5:
            exit()
        elif x == 6:
            open("bestBallers.txt", "w").close()
            open("bestBatsmen.txt", "w").close()
            open("Final.txt", "w").close()
            open("SemiA.txt", "w").close()
            open("SemiB.txt", "w").close()
            open("Summary.txt", "w").close()
            open("Tournament standings.txt", "w").close()
            open("A&B.txt", "w").close()
            open("A.txt", "w").close()
            open("B.txt", "w").close()
            import os
            os.startfile("First.py")
            exit()
    except FormulaError as e:
        print(e)
        print()
        start()

    except ValueError:
        print("Value Error")
        print()
        start()

start()