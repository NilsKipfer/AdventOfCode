f = open("G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DayTree2020\\labirint.txt")
gebiet = [line.replace("\n", "") for line in f]
gebietslinie = ""
position_x = 0
position_y = 0

rechts = [1,3,5,7,1]
unten =  [1,1,1,1,2]

baeume = []
baum = 0
anzbaeume = 0

for i in range(len(rechts)):
    while position_y in range(len(gebiet)):
        gebietslinie = gebiet[position_y][position_x]
        if gebietslinie == '#':
            baum += 1
        position_x = (position_x + rechts[i]) % len(gebiet[0])
        position_y = position_y + unten[i]
        
    baeume.append(baum)
    if anzbaeume != 0:
        anzbaeume *= baum
    else:
        anzbaeume = baum
    baum = 0
    position_x = 0
    position_y = 0


print(baeume)
print(anzbaeume)