with open('input.txt') as f:
    content = f.read()

parts = content.split('\n\n')

ranges = []

for line in parts[0].split("\n"):
    start, end = line.split("-")
    ranges.append((int(start), int(end)))

numbers = [int(x) for x in parts[1].split("\n")]
count = set()
for num in numbers:
    for r_start, r_end in ranges:
        if r_start <= num <= r_end:
            count.add(num)
            print("Valid number:", num)
        else:
            print("Invalid number:", num)

print("Total valid numbers:", len(count))