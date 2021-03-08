with open("G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DayFour2020\\Passports.txt") as f:
    documents = f.read()

passports = documents.split("\n\n")
checkfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
countpassports = 0
countcorrectpassports = 0

while countpassports in range(len(passports)):
    counterforwrongissues = 0
    countfields = 0
    while countfields in range(len(checkfields) - 1):
        checkedfield = checkfields[countfields]
        if passports[countpassports].count(checkedfield) == 1:
            counterforwrongissues += 1
        if counterforwrongissues >= len(checkfields) -1:
            countcorrectpassports += 1
        countfields += 1
    countpassports += 1

print(countcorrectpassports)
