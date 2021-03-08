f = open("G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DayFive2020\\seats.txt")
document = [line for line in f]

columns = 8
row = 128
seatid = []
highestseatid = 0

for bordingpasses in range(len(document)):
    seatmaxrow = row
    seatminrow = 0
    seatrow = 0
    seatmaxcolumn = columns
    seatmincolumn = 0
    seatcolumn = 0
    countseat = 0
    myseat = 0
    while countseat in range(len(document[bordingpasses])):
        if document[bordingpasses][countseat] == "F":
            seatmaxrow = round(seatmaxrow - ((seatmaxrow-seatminrow)/2)) 
        elif document[bordingpasses][countseat] == "B":
            seatminrow = round(seatminrow + ((seatmaxrow - seatminrow)/2))
        elif document[bordingpasses][countseat] == "R":
            seatmincolumn = round(seatmincolumn + ((seatmaxcolumn- seatmincolumn)/2))
        elif document[bordingpasses][countseat] == "L":
            seatmaxcolumn = round(seatmaxcolumn - ((seatmaxcolumn - seatmincolumn)/2))
        countseat += 1
        
        seatrow = seatminrow

        seatcolumn = seatmincolumn
    seatid.append(seatrow*columns+seatcolumn)
    
for i in range(len(seatid) - 1):
    allseats = sorted(seatid, reverse=False)
    firstcount = int(allseats[i])
    secondcount = int(allseats[i+1])
    if firstcount - secondcount == -2:
        print(int(allseats[i] + 1))
#print(myseat)     
#highestseatid = max(seatid)
#print(highestseatid)