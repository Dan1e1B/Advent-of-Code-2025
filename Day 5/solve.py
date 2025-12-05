

with open("input.txt", "r") as f:
    data = f.read().split('\n\n')


# data = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32""".split("\n\n")

id_ranges = data[0].split('\n')
available_ids = data[1].split('\n')[:-1]

# available_id_ranges = []
# for l in id_ranges:

#     l = l.split('-')
#     start = int(l[0])
#     end=int(l[1]) + 1

#     for id_range in available_id_ranges:
#         if start < id_range[0] and end:

    
#     available_id_ranges.append([start, end])
    
count = 0

for ingredient_id in available_ids:
    ingredient_id = int(ingredient_id)
    for available_range in id_ranges:
        available_range = available_range.split('-')

        if ingredient_id >= int(available_range[0]) and ingredient_id <= int(available_range[1]):
            count += 1
            break
        

print(f"{count=}")
# Part two
available_id_ranges = []
for l in id_ranges:

    l = l.split('-')
    start = int(l[0])
    end=int(l[1])

    contained = False
    overwrriten = False
    delete = []
    print([start, end])
    for i in range(len(available_id_ranges)):
        if start < available_id_ranges[i][0] and end > available_id_ranges[i][1]:
            if overwrriten == False:
                available_id_ranges[i] = [start, end]
                overwrriten = True
            else:
                delete.append(i)
        
        elif start >= available_id_ranges[i][0] and end <= available_id_ranges[i][1]:
            contained = True
            break
            
        elif start < available_id_ranges[i][0] and available_id_ranges[i][0] <= end <= available_id_ranges[i][1] :
            if overwrriten:
                available_id_ranges[i][0] = end + 1
            else:
                available_id_ranges[i][0] = start
                overwrriten = True

        elif end > available_id_ranges[i][1] and available_id_ranges[i][1] >= start >= available_id_ranges[i][0]:
            if overwrriten:
                available_id_ranges[i][1] = start - 1
            else:
                available_id_ranges[i][1] = end
                overwrriten = True

        # print([start, end], available_id_ranges, overwrriten, contained)
    
    delete = sorted(delete)
    for k in range(len(delete)):
        available_id_ranges.pop(delete[k] - k)
    
    if overwrriten == False and contained == False:
        available_id_ranges.append([start, end])



print(available_id_ranges)
count = 0
for range in available_id_ranges:
    count += range[1] - range[0] + 1

print(f'{count=}')
