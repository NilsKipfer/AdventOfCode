with open("2020\\DayEight\\textfile.txt") as f:
    document = f.read().splitlines()

counter = 0
idx_list = [False for _ in document]
idx = 0

while True:
    idx_list[idx] = True
    operation = document[idx]
    operat, value = operation.split()
    if operat == "nop":
        idx += 1
    elif operat == "acc":
        counter += int(value)
        idx += 1
    elif operat == "jmp":
        idx += int(value)

    if idx_list[idx] == True:
        break
    

print(counter)