


with open("input.txt", "r") as f:
    data = f.read().split('\n')[:-1]

# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +""".split('\n')

def ignore_spaces(input_text):
    res = []
    text = ""
    for i in range(len(input_text)):
        if input_text[i] != ' ':
            text += input_text[i]
        
        elif text != "":
            res.append(text)
            text = ""
    
    if text != "": res.append(text)
    return res


res = ignore_spaces(data[0])
operations = ignore_spaces(data[-1])

for i in range(len(res)):
    res[i] = int(res[i])

# print(f'{res=}')
# print(f'{operations=}')

for i in range(1, len(data) - 1):
    line = ignore_spaces(data[i])
    for j in range(len(line)):
        if operations[j] == '+':
            res[j] += int(line[j])
        elif operations[j] == '*':
            res[j] *= int(line[j])
        else:
            print(f'Operation Error: {operations[j]}')

s = sum(res)
print(f'Result: {s}')
# Part Two

op = data[-1]

s = 0
indexes = [0] * len(data)
op_index = 0
math = []
result = 0
for i in range(len(data[0])):
    all_spaces = True
    math.append([])
    for j in range(len(data) - 1):
        if data[j][i] != ' ':
            all_spaces = False
            math[-1].append(data[j][i])
            pass
    
    if all_spaces:
        if operations[op_index] == '+':
            operation = lambda x,y : x + y
            result = 0
        elif operations[op_index] == '*':
            operation = lambda x,y : x * y
            result = 1
        
        # print(f'{op_index=} Operation: {operations[op_index]}')
        for num in math:
            if num == []: continue
            num = int("".join(num))
            result = operation(result, num)
        s += result
        math = []
        op_index += 1


if operations[op_index] == '+':
    operation = lambda x,y : x + y
    result = 0
elif operations[op_index] == '*':
    operation = lambda x,y : x * y
    result = 1


for num in math:
    if num == []: continue
    num = int("".join(num))
    result = operation(result, num)
s += result

print(f'Result: {s}')