with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

# Pad all lines to the same length
max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) for line in lines]

operators_row = lines[-1]
digit_rows = lines[:-1]

# Process columns right-to-left, grouping into problems
problems = []  # list of (operator, [numbers])
current_numbers = []
current_operator = None

for col in range(max_len - 1, -1, -1):  # right to left
    char_at_bottom = operators_row[col]
    
    # Check if this column is part of a problem or a separator
    column_digits = ''.join(row[col] for row in digit_rows if row[col] != ' ')
    
    if char_at_bottom in '+*':
        current_operator = char_at_bottom
    
    if column_digits:  # This column has a number
        number = int(column_digits)
        current_numbers.append(number)
    elif current_numbers:  # Space column = end of current problem
        if current_operator:
            problems.append((current_operator, current_numbers))
        current_numbers = []
        current_operator = None

# Don't forget the last problem
if current_numbers and current_operator:
    problems.append((current_operator, current_numbers))

# Calculate results
res = []
for op, nums in problems:
    if op == '+':
        res.append(sum(nums))
    elif op == '*':
        total = 1
        for n in nums:
            total *= n
        res.append(total)

print(sum(res))