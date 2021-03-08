numbers = []  #string trennen bei - und bei " "die beiden Zahlen werden im numbers Array gespeichert.
letter = ""  #das zeichen vor dem : wird in Letters gespeichert.
password = "" #password erhält die Zeichen nach dem zweiten " " und wird dann auf die Existens von Letter an der Stelle von numbers geprüft
text = []
countPasswords = 0
countLetters = 0
count = 0

with open("G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DayTwo2020\\password.txt") as f:
    text = list(f.readlines())



######################################################################################
# Aufgabe 1
######################################################################################
#for t in text:
#    countLetters = 0
#    number, letters, password = t.split(" ",2)
#    firstnumber, secondnumber = number.split("-",1)
#    letter, signal = letters.split(":",1)
#    countLetters = password.count(letter)
#    if countLetters >= int(firstnumber) and countLetters <= int(secondnumber):
#        countPasswords = countPasswords + 1
######################################################################################

######################################################################################
# Aufgabe 2
######################################################################################
for t in text:
    countLetters = 0
    count = 0
    number, letters, password = t.split(" ",2)
    firstnumber, secondnumber = number.split("-",1)
    letter, signal = letters.split(":",1)
    for char in password:
        countLetters = countLetters + 1
        if char == letter:
            if countLetters == int(firstnumber) or countLetters == int(secondnumber):
                count = count + 1
                if count == 1:
                    countPasswords = countPasswords + 1
                else:
                    countPasswords = countPasswords - 1
                
######################################################################################
        

print(countPasswords)
