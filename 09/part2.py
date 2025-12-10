file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

tiles = [(int(a), int(b)) for a,b in [line.split(",") for line in data.split("\n")]]

sizes = []

# sort all the x and y coordinates, this makes a much smaller but geometrically representative grid to scale the coordinates down to
xs = sorted([x for x, y in tiles])
ys = sorted([y for x, y in tiles])
tiles_n = [(xs.index(x) // 2, ys.index(y) // 2) for x, y in tiles]
grid = [[" "] * (len(xs) // 2) for i in range(len(ys) // 2)]

# with the smaller coordinates draw a manageable and visualisable grid
lx, ly = tiles_n[0]
for nx, ny in tiles_n[1:] + [tiles_n[0]]:
    if ly == ny:
        for x in range(min(nx, lx), max(nx, lx) + 1):
            grid[ly][x] = "X"
    else:
        for y in range(min(ny, ly), max(ny, ly) + 1):
            grid[y][lx] = "X"
    lx, ly = nx, ny

# flood fill it
fill = [(len(grid[0]) // 2, (len(grid) * 2) // 3)]
grid[fill[0][1]][fill[0][0]] = "F"
height = len(grid)
width = len(grid[0])
while fill:
    x, y = fill.pop(0)
    if y > 0 and grid[y - 1][x] == " ":
        grid[y - 1][x] = "F"
        fill.append((x, y - 1))
    if y + 1 < height and grid[y + 1][x] == " ":
        grid[y + 1][x] = "F"
        fill.append((x, y + 1))
    if x > 0 and grid[y][x - 1] == " ":
        grid[y][x - 1] = "F"
        fill.append((x - 1, y))
    if x + 1 < width and grid[y][x + 1] == " ":
        grid[y][x + 1] = "F"
        fill.append((x + 1, y))

# debug render
for row in grid:
    print("".join(row))

def check_rect(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    for x in range(min(x1, x2), max(x1, x2) + 1):
        if grid[y1][x] == " ":
            return False
        if grid[y2][x] == " ":
            return False
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if grid[y][x1] == " ":
            return False
        if grid[y][x2] == " ":
            return False
    return True

# now when checking rectangles, ensure the hole perimeter is in the shaded area
sizes = []
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):

        if not check_rect(tiles_n[i], tiles_n[j]):
            continue

        x1,y1 = tiles[i]
        x2,y2 = tiles[j]

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        sizes.append((area, (i, j)))

print(sorted(sizes)[-1][0])