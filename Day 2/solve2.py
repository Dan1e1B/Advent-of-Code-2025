

with open("input.txt", "r") as f:
    data = f.read().split(',')

# data = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
# data = data.split(',')
# data = ['99-115']
invalid_ids = []
for rng in data:

    start, end = rng.split('-')

    for i in range(int(start), int(end) + 1):
        s = str(i)

        if len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]:
            invalid_ids.append(i)


print(sum(invalid_ids))
invalid_ids = []

print(invalid_ids)
for rng in data:

    start, end = rng.split('-')

    for i in range(int(start), int(end) + 1):
        s = str(i)

        for j in range(1, (len(s) // 2) + 1):

            if len(s) % j: continue
            valid = False
            initial_sequence = s[:j]

            for k in range(j, (len(s) - j) + 1, j):
                if s[k-j:k] != s[k:k+j]:
                    valid = True
                    break
            
            if valid == False: 
                # print(f'Invalid {i} sequence: {j} len: {len(invalid_ids)} invalid_ids: {invalid_ids}')
                invalid_ids.append(i)
                # print(f'Invalid {i} sequence: {j} len: {len(invalid_ids)} invalid_ids: {invalid_ids}')
                break



print(sum(invalid_ids))
print(len(invalid_ids))
print(invalid_ids)