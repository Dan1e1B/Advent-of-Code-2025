


content = ""

with open("input.txt", "r") as f:

    content = f.read().split("\n")[:-1]


number = 50
# content = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
counter = 0
for line in  content:

    direction = line[0]
    line = line[1:]

    if direction == 'R':
        number = (number + int(line)) % 100
    
    else:
        number = (number - int(line)) % 100

    if number == 0: counter += 1

print(f'{counter=}')


# Part two


number = 50
counter = 0
for line in  content:

    direction = line[0]
    line = line[1:]

    

    if direction == 'R':
        counter += int((number + int(line) - 1) / 100)
        number = (number + int(line)) % 100
    
    else:
        counter += abs(int((number - int(line) - 99) / 100))
        if number == 0: counter -= 1
        number = (number - int(line)) % 100
        # print(counter, number, line, int((number - int(line) - 99) / 100))


    
    if number == 0: counter += 1
    # print(f'{direction}{line} {number=} {counter=}')



print(f'{counter=}')


