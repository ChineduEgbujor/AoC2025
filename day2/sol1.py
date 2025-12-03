with open("input.txt") as f:
    line = f.read().strip()

ranges = []

for item in line.split(','):
    start, end = map(int, item.split('-'))
    ranges.append((start, end))

res = []

for start, end in ranges:
    for num in range(start, end + 1):
        temp = str(num)
        if len(temp) % 2 == 0:
            mid = len(temp) // 2
            if temp[:mid] == temp[mid:]:
                res.append(num)

print(sum(res))