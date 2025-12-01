file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

position = 50
times_at_zero = 0
times_passed_zero = 0
full_loops = 0

for line in data.split("\n"):
    turn_amount = int(line[1:])
    turn_direction = line[0]

    full_loops += turn_amount // 100
    turn_amount %= 100

    before = position

    if turn_direction == "R":
        position = (position + turn_amount) % 100
        if before != 0 and position != 0 and before > position:
            times_passed_zero += 1
    else:
        position = (position - turn_amount) % 100
        if before != 0 and position != 0 and before < position:
            times_passed_zero += 1

    if position == 0:
        times_at_zero += 1

print(times_at_zero + times_passed_zero + full_loops)
