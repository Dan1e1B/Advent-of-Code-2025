

with open('input.txt', "r") as f:
    data = f.read().split('\n')[:-1]

# data ="""162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689""".split('\n')

aux_data = []
for line in data:
    aux_data.append([int(coordinate) for coordinate in line.split(',')])

data = aux_data.copy()
# print(data)

connected = []
distances = []

def distance(pointA, pointB):
    return (((pointB[0] - pointA[0]) ** 2) + ((pointB[1] - pointA[1]) ** 2) + ((pointB[2] - pointA[2]) ** 2))** (1/2)

def are_connected(connected, pointA, pointB):
    for connection in connected:
        if (pointA in connection) or (pointB in connection):
            return (pointA in connection) and (pointB in connection)
    
    return False

def exist(connected, point):
    for connection in connected:
        if point in connection:
            return True
    return False

def find(connected, point):
    for i in range(len(connected)):
        if point in connected[i]:
            return i
    return -1

# print(distance(data[0], data[1]))
for i in range(len(data)):
    for j in range(i):        
        distances.append([distance(data[j], data[i]), j, i])


sorted_distances = sorted(distances, key=lambda k: k[0])

connected_counter = 0
connection_counter = 0

for i in range(len(sorted_distances)):

    pointB = sorted_distances[i][1]
    pointA = sorted_distances[i][2]

    # if connection_counter >= 10: break 
    if connection_counter >= 1000: break 

    
    if are_connected(connected, pointA, pointB):
        connection_counter += 1
        continue

    elif exist(connected, pointA) and exist(connected, pointB):
        index_pointA = find(connected, pointA)
        index_pointB = find(connected, pointB)

        for point in connected[index_pointB]:
            connected[index_pointA].add(point)
        
        connected.pop(index_pointB)
        connection_counter += 1
    
    elif exist(connected, pointA):
        index_pointA = find(connected, pointA)
        connected[index_pointA].add(pointB)
        connected_counter += 1
        connection_counter += 1

    elif exist(connected, pointB):
        index_pointB = find(connected, pointB)
        connected[index_pointB].add(pointA)
        connected_counter += 1
        connection_counter += 1
    
    else:
        connected.append({pointA, pointB})
        connected_counter += 2
        connection_counter += 1
    
    # print(connected, connection_counter)
    




print(len(connected), len(connected[0]))
connected.sort(key=lambda k: len(k))
# print(connected)
res = len(connected[-1]) * len(connected[-2]) * len(connected[-3])
# print(sorted_distances[:5])
print(f'{connected_counter=}')
print(f'{res=}')
print(f'{len(data)}')


# print(distances)

# Part two

connected_counter = 0
connection_counter = 0
last_distance = -1
for i in range(len(sorted_distances)):

    pointB = sorted_distances[i][1]
    pointA = sorted_distances[i][2]

    # if connected_counter >= 99: break
    # if connection_counter >= 1000: break 

    if len(connected[0]) == len(data):
        break

    last_distance = sorted_distances[i]
    if are_connected(connected, pointA, pointB):
        connection_counter += 1
        continue

    elif exist(connected, pointA) and exist(connected, pointB):
        index_pointA = find(connected, pointA)
        index_pointB = find(connected, pointB)

        for point in connected[index_pointB]:
            connected[index_pointA].add(point)
        
        connected.pop(index_pointB)
        connection_counter += 1
    
    elif exist(connected, pointA):
        index_pointA = find(connected, pointA)
        connected[index_pointA].add(pointB)
        connected_counter += 1
        connection_counter += 1

    elif exist(connected, pointB):
        index_pointB = find(connected, pointB)
        connected[index_pointB].add(pointA)
        connected_counter += 1
        connection_counter += 1
    
    else:
        connected.append({pointA, pointB})
        connected_counter += 2
        connection_counter += 1

pointA = last_distance[1]
pointB = last_distance[2]


print(f'Result: {data[pointA][0] * data[pointB][0]}')