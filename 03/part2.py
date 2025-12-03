file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

total = 0

# changing to 2 solves part 1
NUMBER_OF_DIGITS = 12

for bank in data.split("\n"):
    
    joltage = 0
    search_range_start = 0
    for i in range(NUMBER_OF_DIGITS):
        best_digit = "0"
        for i in range(search_range_start, len(bank) - NUMBER_OF_DIGITS + 1 + i):
            digit = bank[i]
            if digit > best_digit:
                best_digit = digit
                search_range_start = i + 1
                # these 2 lines are optional for optimization
                # if we see a 9 it can't be beaten, so stop looking early
                if best_digit == "9":
                    break
        joltage = joltage * 10 + int(best_digit)

    total += joltage

print(total)