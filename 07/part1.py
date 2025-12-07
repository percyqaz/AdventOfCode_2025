file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

grid = [[c for c in line] for line in data.split("\n")]

start = (0, 0)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start = (x, y)

tachyon_beams = [start]
splitters_hit = set()

while tachyon_beams:
    x, y = tachyon_beams.pop(0)
    if y + 1 >= len(grid):
        continue
    
    next = grid[y + 1][x]
    if next == "^":
        splitters_hit.add((x, y + 1))
        if x > 0 and (x - 1, y + 1) not in tachyon_beams:
            tachyon_beams.append((x - 1, y + 1))
        if x + 1 < len(grid[0]) and (x + 1, y + 1) not in tachyon_beams:
            tachyon_beams.append((x + 1, y + 1))
    else:
        tachyon_beams.append((x, y + 1))

print(len(splitters_hit))