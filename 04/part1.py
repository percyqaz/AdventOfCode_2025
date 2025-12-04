file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

lines = data.split("\n")
width = len(lines)
grid = []

grid.append([0] * (width + 2))
for line in lines:
    grid.append([0] + [1 if c == '@' else 0 for c in line.strip()] + [0])
grid.append([0] * (width + 2))

hits = 0

for x in range(1, width + 1):
    for y in range(1, width + 1):
        if grid[y][x] == 1:
            neighbors = grid[y-1][x] + grid[y-1][x-1] + grid[y-1][x+1] + grid[y][x-1] + grid[y][x+1] + grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1]
            if neighbors < 4:
                hits += 1

print(hits)