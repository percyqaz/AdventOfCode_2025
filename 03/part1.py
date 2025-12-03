file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

total = 0

for bank in data.split("\n"):
    
    position_of_highest_digit = -1
    highest_digit = "0"
    for i in range(0, len(bank) - 1):
        digit = bank[i]
        if digit > highest_digit:
            highest_digit = digit
            position_of_highest_digit = i
            if highest_digit == "9":
                break # 9 cannot be beaten

    next_highest_digit = "0"
    for i in range(position_of_highest_digit + 1, len(bank)):
        digit = bank[i]
        if digit > next_highest_digit:
            next_highest_digit = digit
            if next_highest_digit == "9":
                break # 9 cannot be beaten

    total += int(highest_digit + next_highest_digit)

print(total)