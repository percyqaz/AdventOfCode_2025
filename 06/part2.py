file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

sheet = data.split("\n")
split_markers = []
last_op = sheet[-1][0]
for i in range(1, len(sheet[-1])):
    if sheet[-1][i] in ["*", "+"]:
        split_markers.append((i, last_op))
        last_op = sheet[-1][i]
split_markers.append((len(sheet[-1]) + 1, last_op))

calculations = []
last_marker = 0
for m, op in split_markers:
    numbers = [ line[last_marker:m - 1] for line in sheet[:-1] ]
    c_numbers = [ int("".join(x).strip()) for x in [[numbers[j][i] for j in range(len(numbers))] for i in range(len(numbers[0]))]]
    calculations.append((c_numbers, op))
    last_marker = m

total = 0

for numbers, op in calculations:
    if op == "*":
        result = 1
        for number in numbers:
            result *= number
    else:
        result = 0
        for number in numbers:
            result += number
    total += result

print(total)