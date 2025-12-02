file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

total = 0

pairs = data.split(",")

for pair in pairs:
    start, end = [int(x) for x in pair.split("-")]
    
    for number in range(start, end + 1):
        number_as_text = str(number)
        digits = len(number_as_text)
        if digits % 2 != 0:
            continue # odd length numbers cannot be repeating like we're looking for

        factor_check = 10 ** (digits//2) + 1
        if number % factor_check == 0:
            total += number

print(total)