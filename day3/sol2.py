res = []
total = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

    for line in lines:
        # Need to pick exactly 12 digits, maintaining order
        # Greedy approach: at each step, pick the largest digit
        # that still leaves enough digits remaining
        
        n = len(line)
        k = 12  # number of digits to pick
        result = []
        start = 0  # starting position to search from
        
        for i in range(k):
            # We need to pick (k - i) more digits including this one
            # So we can search from 'start' up to position n - (k - i - 1) - 1
            # This ensures enough digits remain after our pick
            remaining_needed = k - i
            end = n - remaining_needed + 1
            
            # Find the largest digit in range [start, end)
            best_digit = '0'
            best_pos = start
            for pos in range(start, end):
                if line[pos] > best_digit:
                    best_digit = line[pos]
                    best_pos = pos
            
            result.append(best_digit)
            start = best_pos + 1  # next search starts after this position
        
        num = int(''.join(result))
        res.append(num)
    
    total = sum(res)
    print("total", total)