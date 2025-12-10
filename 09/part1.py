file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

tiles = [(int(a), int(b)) for a,b in [line.split(",") for line in data.split("\n")]]

sizes = []

for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        x1,y1 = tiles[i]
        x2,y2 = tiles[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        sizes.append((area, (i, j)))

print(sorted(sizes)[-1][0])