file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

ranges, numbers = data.split("\n\n")
ranges = [(int(left), int(right)) for left, right in [range.split("-") for range in ranges.strip().split("\n")]]
numbers = [int(n) for n in numbers.strip().split("\n")]

ranges = sorted(ranges)

def make_merge(ranges):

    for i in range(len(ranges)):
        for j in range(len(ranges)):
            if i == j: continue
            range1 = ranges[i]
            range2 = ranges[j]
            if not (range1[1] < range2[0] or range2[1] < range1[0]):
                new_range = (min(range1[0], range2[0]), max(range1[1], range2[1]))
                ranges.remove(range1)
                ranges.remove(range2)
                ranges.append(new_range)
                return True
            
    return False

while make_merge(ranges):
    pass

print(ranges)

sum = 0
for left, right in ranges:
    sum += (right - left) + 1
print(sum)