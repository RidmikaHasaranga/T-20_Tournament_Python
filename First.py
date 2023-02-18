import codecs
import reprlib
import random
class FormulaError(Exception): pass

def insert():
    try:
        #Error handeling
        file = open("Team.txt", "r")
        lineCount = 0
        for line in file:
            if line != "\n":
                lineCount += 1
        if lineCount == 8:
            print("8 Teams already Insert")
            start()
        file.close()

        file = open("Team.txt", "a")
        list = []
        print("Do not use spaces for name")
        print("Please use \"_\" for it")
        TName = input("Enter Team Name : ")
        if " " in TName: #error handeling
            raise FormulaError("Spaces are not valid for name please use '_' \nRe-Enter Team")
        list.append(TName)  # Team Name insert in to list
        x = 1
        while x < 12:
            y = str(x)
            player = input(f"Enter player {y} : ")
            if " " in player: #error handeling
                raise FormulaError("Spaces are not valid for name please use '_' \nRe-Enter Team and Players")
            list.append(player)  # Players add to list one by one
            x += 1
        file.write(str(list) + "\n")  # '\n' for line break
        file.close()
        start()
    except FormulaError as e:
        print(e)
        insert()


def read():
    try:
        import os
        file = open("Team.txt", "r")
        filesize = os.path.getsize("Team.txt")
        a = file.readline()
        if filesize == 0:
            raise FormulaError("No data yet as data has not been entered")
        while a:
            b = a.replace("[", "")  # remove [ ]  one by one
            c = b.replace("]", "")
            d = list(c.split(","))
            print("Team : ", d[0])
            x = 1
            while x < 12:
                print("Player", str(x), ":", d[x])
                x += 1
            a = file.readline()
        file.close()
        start()

    except FormulaError as e:
        print(e)
        print()
        start()


def select():
    try:
        import os
        file = open("Team.txt", "r")
        filesize = os.path.getsize("Team.txt")
        a = file.readline()
        if filesize == 0:
            raise FormulaError("No data yet as data has not been entered")
        x = 1
        while a:
            b = a.replace("[", "")
            c = b.replace("]", "")
            d = c.replace("'", "")
            e = list(d.split(","))
            print(x, ") Team : ", e[0])
            x += 1
            a = file.readline()
        file.close()

    except FormulaError as e:
        print(e)
        print()
        start()


def update():
    try:
        import linecache  # to get specific line from text file
        file = open("Team.txt", "a")
        num = int(input("Select Team Number : "))
        if num > 8 or num < 1: #error handeling
            raise FormulaError ("Input not in range")
        a = linecache.getline("Team.txt", num)  # get relevant line from text file
        b = a.replace("[", "")
        c = b.replace("]", "")
        d = c.replace("'", "")
        f = d.replace(" ", "")
        e = list(f.split(","))
        print("Team", e[0])
        x = 1
        while x < 12:
            y = "player " + str(x) + " :"
            print(y, e[x])
            x += 1
        pnum = int(input("Select  the Player Number you want to update : "))
        if pnum >11 or pnum < 1: #error handeling
            raise FormulaError ("Input not in range")
        print("Do not use spaces for name")
        print("Please use \"_\" for it")
        newName = input("Enter New Player " + str(pnum) + " Name : ")
        if " " in newName:  # error handeling
            raise FormulaError("Spaces are not valid for name please use '_' \nRe-Update Player")
        e[pnum] = newName  # update new name

        file2 = open("Team.txt", "r")
        lines = file2.readlines()  # take all lines from file
        file2.close()
        lines.append(str(e))  # add updated line for lines variable

        del lines[num - 1]  # delete specific(old) line from lines variable

        newFile = open("Team.txt", "w+")
        lines2 = list(lines)

        for line in lines2:
            newFile.write(line)
        newFile.close()

        file.close()
        start()

    except FormulaError as e:
        print(e)
        print()
        select()
        update()



def delete():
    try:
        file = open("Team.txt", "r")
        num = int(input("Select Team Number : "))
        if num >8 or num < 1: #error handeling
            raise FormulaError("Input not in range")
        lines = file.readlines()  # take all lines in file
        file.close()
        del lines[num - 1]  # delete specific line from lines
        newFile = open("Team.txt", "w+")

        for line in lines:
            newFile.write(line)

        newFile.close()
        print()
        print("Successfully Deleted")
        start()

    except FormulaError as e:
        print(e)
        print()
        start()


def start():
    try:
        print()
        print("Welcome to T20-Teams System")
        print()
        print("Please select the number of the action you want to execute")
        print()
        print("1)INSERT Team and Team Members")
        print("2)Details about Team and Team Members")
        print("3)UPDATE Team Members")
        print("4)DELETE Teams")
        print("5)Exit")
        print("6)If all updates, deletes, and inserts are done, select 6 for going to Tournament System")
        print()
        x = int(input("Enter the number of the action you want to execute : "))
        if x > 6 or x < 1:
            raise FormulaError ("Input not in range")
        print()
        if x == 1:
            insert()
        elif x == 2:
            read()
        elif x == 3:
            select()
            update()
        elif x == 4:
            select()
            delete()
        elif x == 5:
            exit()
        elif x == 6:
            twoGroups()
            import time
            time.sleep(3)     #to watch A team and B Team
            import os
            os.startfile("Second.py")
            exit()

    except ValueError:
        print("Value Error")
        print()
        start()
    except FormulaError as e:
        print(e)
        print()
        start()


def twoGroups():
    file = open("Team.txt", "r")
    a = file.readline()
    li = []
    while a:
        b = a.replace("[", "")
        c = b.replace("]", "")
        d = c.replace("'", "")
        e = list(d.split(","))
        li.append(e[0])
        a = file.readline()
    file.close()
    print("A Team: ", li[0:4])
    print("B Team: ", li[4:])

    file = open("Team.txt", "r")
    lines = file.readlines()
    fileA = open("A.txt", "w")
    fileB = open("B.txt", "w")
    lines1 = list(lines[0:4])
    lines2 = list(lines[4:])
    for line in lines1:
        fileA.write(line)
    for line in lines2:
        fileB.write(line)

    file.close()
    fileA.close()
    fileB.close()
    newfile = open("A&B.txt", "w")
    newfile.write("A1")
    newfile.close()

    #for tournamnet standing
    li = []
    file = open("Team.txt", "r")
    a = file.readline()
    tFile = open("Tournament standings.txt", "w")
    while a:
        b = a.replace("[", "")
        c = b.replace("]", "")
        d = c.replace("'", "")
        e = list(d.split(","))
        s = (e[0], 0)
        li.append(s)
        a = file.readline()
    tFile.write(str(li))
    file.close()
    tFile.close()


start()