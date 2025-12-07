file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

grid = [[c for c in line] for line in data.split("\n")]

start = (0, 0)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start = (x, y)

tachyon_beams = {start: 1}

while tachyon_beams:
    tachyon_beams_2 = {}
    for x, y in tachyon_beams:
        n = tachyon_beams[(x, y)]
        if y + 1 >= len(grid):
            continue
        
        if grid[y + 1][x] == "^":
            if (x - 1, y + 1) not in tachyon_beams_2:
                tachyon_beams_2[(x - 1, y + 1)] = 0
            tachyon_beams_2[(x - 1, y + 1)] += n
            if (x + 1, y + 1) not in tachyon_beams_2:
                tachyon_beams_2[(x + 1, y + 1)] = 0
            tachyon_beams_2[(x + 1, y + 1)] += n
        else:
            if (x, y + 1) not in tachyon_beams_2:
                tachyon_beams_2[(x, y + 1)] = 0
            tachyon_beams_2[(x, y + 1)] += n
    if not tachyon_beams_2:
        break
    tachyon_beams = tachyon_beams_2

timelines = 0
for k in tachyon_beams:
    timelines += tachyon_beams[k]
print(timelines)