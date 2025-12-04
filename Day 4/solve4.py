

with open("input.txt", "r") as f:
    data = f.read().split('\n')[:-1]


def count(matrix, k):

    res = 0

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if matrix[i][j] == k: res += 1

    return res

# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.""".split('\n')

aux_data = []
for line in data:
    aux_data.append(list(line))

data = aux_data.copy()

res = 0
for i in range(len(data)):

    for j in range(len(data[i])):
        matrix = []
        for k in range(max(0, i - 1), min(len(data), i + 2)):
            line = []
            for z in range(max(0, j - 1), min(len(data[i]), j + 2)):
                line.append(data[k][z])

            matrix.append(line)
        
        if count(matrix, '@') <= 4 and data[i][j] == '@':
            res += 1

print(f'{res=}')

# part two

s = 0
aux_data = data.copy()
while (res > 0):
    res = 0
    for i in range(len(data)):

        for j in range(len(data[i])):
            matrix = []
            for k in range(max(0, i - 1), min(len(data), i + 2)):
                line = []

                for z in range(max(0, j - 1), min(len(data[i]), j + 2)):
                    line.append(data[k][z])

                matrix.append(line)
            

            if count(matrix, '@') <= 4 and data[i][j] == '@':
                aux_data[i][j] = 'x'
                res += 1

    data = aux_data.copy()
    s += res
print(f'Sum: {s}')



