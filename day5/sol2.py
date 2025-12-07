with open('input.txt') as f:
    content = f.read()

parts = content.split('\n\n')

ranges = []

for line in parts[0].split("\n"):
    start, end = line.split("-")
    ranges.append((int(start), int(end)))

numbers = [int(x) for x in parts[1].split("\n")]
ranges.sort()
merged = []

for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

total = sum(end - start + 1 for start, end in merged)
print("Total numbers in ranges:", total)