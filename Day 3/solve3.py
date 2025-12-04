

with open("input.txt", "r") as f:

    data = f.read().split('\n')[:-1]


# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".split("\n")
total = 0
for bank in data:

    max_val = -1
    idx_max_val = -1
    max_val_2 = -1

    for i in range(len(bank) - 1):
        val = int(bank[i])
        if  val > max_val:
            idx_max_val = i
            max_val = val
    
    for i in range(idx_max_val + 1, len(bank)):
        val = int(bank[i])
        if val > max_val_2:
            max_val_2 = val
    

    total += int(str(max_val) + str(max_val_2))

print(f'{total=}')
# Part two

total = 0
numbers = 12
for bank in data:

    max_vals = []
    idx_max_vals = []

    for i in range(numbers):
        starting_point = -1 if len(idx_max_vals) == 0 else idx_max_vals[-1]
        max_val = -1
        idx_max_val = -1
        for j in range(starting_point + 1, len(bank) - numbers + i + 1):
            val = int(bank[j])
            if val > max_val:
                max_val = val
                idx_max_val = j
        
        max_vals.append(max_val)
        idx_max_vals.append(idx_max_val)

    

    total += int("".join([str(val) for val in max_vals]))

print(f'{total=}')
