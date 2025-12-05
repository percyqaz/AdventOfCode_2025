file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

ranges, numbers = data.split("\n\n")
ranges = [(int(left), int(right)) for left, right in [range.split("-") for range in ranges.strip().split("\n")]]
numbers = [int(n) for n in numbers.strip().split("\n")]

fresh = 0

for number in numbers:
    for range in ranges:
        if range[0] <= number <= range[1]:
            fresh += 1
            break

print(fresh)