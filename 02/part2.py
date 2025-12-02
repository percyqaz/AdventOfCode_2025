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

        hit = False
        for n in range(2, digits + 1):

            if digits % n != 0:
                continue

            factor_check = 0
            for i in range(n):
                factor_check *= 10 ** (digits//n)
                factor_check += 1

            if number % factor_check == 0:
                hit = True

        if hit:
            total += number

print(total)