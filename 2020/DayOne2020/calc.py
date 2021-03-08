numbers = []
f = open("G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DayOne2020\\numbers.txt")
numbers = list(map(int, f.readlines()))
calc1 = 0
calc2 = 0

######################################################
# Aufgaber 1 #
######################################################
for a in numbers:
    for b in numbers:
        if (a + b == 2020):
            calc1 = a*b
            print("Aufgabe 1:" ,calc1)
            break
    if calc1 != 0:
        break
######################################################

######################################################
# Aufgaber 2 #
######################################################
for x in numbers:
    for y in numbers:
        for z in numbers:
            if (x + y +z == 2020):
                calc2 = x*y*z
                print("Aufgabe 2:" ,calc2)
                break
        if calc2 != 0:
            break
    if calc2 != 0:
        break
######################################################            