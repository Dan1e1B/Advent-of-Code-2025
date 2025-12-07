


with open("input.txt", "r") as f:
    data = f.read().split('\n')[:-1]

# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............""".split('\n')


tachyon_indexes = [data[0].find('S')]
counter = 0

for line in data[1:]:
    splitters_indexes = []
    new_tachyon_indexes = []

    for i in range(len(line)):
        if line[i] == '^':
            splitters_indexes.append(i)
    
    for splitter in splitters_indexes:
        split = False
        if splitter - 1 >= 0 and not (splitter - 1 in new_tachyon_indexes) and (splitter in tachyon_indexes):
            new_tachyon_indexes.append(splitter - 1)
            split = True
        
        if splitter + 1 < len(line) and not (splitter + 1 in new_tachyon_indexes) and (splitter in tachyon_indexes):
            new_tachyon_indexes.append(splitter + 1)
            split = True
        
        if split:
            counter += 1

    # print(f'{new_tachyon_indexes=}')
    for tachyon in tachyon_indexes:
        if not (tachyon in splitters_indexes) and not (tachyon in new_tachyon_indexes):
            new_tachyon_indexes.append(tachyon)

    tachyon_indexes = new_tachyon_indexes.copy() 
        
      
    
    # if len(tachyon_indexes) > 3: break
    
    
    
    # print(tachyon_indexes)

# print(len(tachyon_indexes))
print(counter)

# Part Two



tachyon_indexes = {data[0].find('S'): 1}
index = 0

for line in data[1:]:
    splitters_indexes = set()
    new_tachyon_indexes = {}

    for i in range(len(line)):
        if line[i] == '^':
            splitters_indexes.add(i)


    
    for tachyon_index, timelines in tachyon_indexes.items():
        if (tachyon_index in splitters_indexes):
            if tachyon_index - 1 >= 0:
                new_tachyon_indexes[tachyon_index - 1] = new_tachyon_indexes.get(tachyon_index - 1, 0) + timelines
            
            if tachyon + 1 < len(line):
                new_tachyon_indexes[tachyon_index + 1] = new_tachyon_indexes.get(tachyon_index + 1, 0) + timelines
        


    # print(f'{new_tachyon_indexes=}')
    for tachyon_index, timelines in tachyon_indexes.items():
        if not (tachyon_index in splitters_indexes):
            new_tachyon_indexes[tachyon_index] = new_tachyon_indexes.get(tachyon_index, 0) + timelines

    tachyon_indexes = new_tachyon_indexes.copy()
    # print(index, len(tachyon_indexes), tachyon_indexes)
    index += 1

        
      
    
    # if len(tachyon_indexes) > 3: break
    
    
    
    # print(counter, len(tachyon_indexes), tachyon_indexes)
res = 0

for timelines in tachyon_indexes.values():
    res += timelines
print(len(tachyon_indexes))
print(res)



