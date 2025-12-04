file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

lines = data.split("\n")
width = len(lines)
grid = []

# Add padding of 0s around the grid, it makes neighbor checking easier
# without it you need a bunch of logic to not go "out of bounds" - in python this = crash and in sheets this = #REF!
grid.append([0] * (width + 2))
for line in lines:
    grid.append([0] + [1 if c == '@' else 0 for c in line.strip()] + [0])
grid.append([0] * (width + 2))

total = 0
this_pass_found_new_rolls = True

while this_pass_found_new_rolls:
    hits = []

    # check every position for the criteria of the puzzle
    # record their coordinates as a (x, y) tuple in `hits`
    for x in range(1, width + 1):
        for y in range(1, width + 1):
            if grid[y][x] == 1:
                neighbors = grid[y-1][x] + grid[y-1][x-1] + grid[y-1][x+1] + grid[y][x-1] + grid[y][x+1] + grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1]
                if neighbors < 4:
                    hits.append((x, y))

    this_pass_found_new_rolls = len(hits) > 0

    # remove all the hits from the grid, ready for next pass
    for x, y in hits:
        grid[y][x] = 0

    total += len(hits)

print(total)