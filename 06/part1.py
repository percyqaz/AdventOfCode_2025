file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

sheet = [ line.strip().split() for line in data.split("\n") ]
lengths = [ len(row) for row in sheet ]
if max(lengths) != min(lengths):
    raise Exception("Sheet parsed wrong")

total = 0

for i in range(lengths[-1]):
    op = sheet[-1][i]
    if op == "*":
        result = 1
        for row in sheet[:-1]:
            result *= int(row[i])
    else:
        result = 0
        for row in sheet[:-1]:
            result += int(row[i])
    total += result

print(total)