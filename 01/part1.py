file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

position = 50
tally = 0

for line in data.split("\n"):
    turn_amount = int(line[1:])
    turn_direction = line[0]

    if turn_direction == "R":
        position = (position + turn_amount) % 100
    else:
        position = (position - turn_amount) % 100
    
    if position == 0:
        tally = tally + 1

print(tally)