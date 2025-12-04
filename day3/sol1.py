res = []
total = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

    for line in lines:
        best = 0
       
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
               
                num = int(line[i] + line[j])
                if num > best:
                    best = num
        
        res.append(best)
    
    total = sum(res)
    print("total", total)


