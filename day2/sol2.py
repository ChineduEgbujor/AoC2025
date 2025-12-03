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
        n = len(temp)
        
        # Check all possible pattern lengths (1 to n//2)
        # Pattern must repeat at least twice, so max length is n//2
        for p in range(1, n // 2 + 1):
            # Pattern length must divide evenly into total length
            if n % p == 0:
                pattern = temp[:p]
                repetitions = n // p
                # Check if repeating the pattern gives the original number
                if pattern * repetitions == temp:
                    res.append(num)
                    break  # Don't count the same number twice

print(sum(res))