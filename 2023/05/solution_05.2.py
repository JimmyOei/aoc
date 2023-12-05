input = open('./input_05.txt', 'r')
lines = input.readlines()

seeds = [int(num) for num in lines[0].split() if num.isdigit()]
ranges = []
for i in range(1, len(seeds), 2):  
    ranges.append(seeds[i])
    seeds[i] = None
seeds = [x for x in seeds if x is not None]

data = []
l = 3
while l < len(lines):
    cat = []
    while l < len(lines) and not ':' in lines[l]:
        mp = [int(num) for num in lines[l].split() if num.isdigit()]
        if len(mp) > 0:
            cat.append(mp)
        l += 1
    # sort on second number
    cat.sort(key=lambda x: x[1])
    data.append(cat)
    l += 1

print(data)

for cat in data:
    reset = [True]*len(seeds)
    for mp in cat:
        start = mp[1]
        finish = mp[1]+mp[2]
        for j, x in enumerate(seeds):
            if reset[j]:
                if start <= x:
                    dif = finish - x
                    if dif < ranges[j]:
                        # add surplus as own interval
                        surplus = ranges[j] - dif
                        seeds.append(x + dif+1)
                        ranges.append(surplus-1)
                        reset.append(True)
                    ranges[j] = dif
                    startdif = x - start
                    seeds[j] = mp[0]+startdif
                    reset.append(False)
                else:
                    end = x+ranges[j]
                    if end >= start:
                        # add surplus as own interval
                        surplus = end - start
                        seeds.append(start)
                        ranges.append(surplus-1)
                        reset.append(True)
                        ranges[j] -= surplus
                    k = len(seeds)-1
                    y = r=seeds[k]
                    dif = finish - y
                    if dif < ranges[k]:
                        # add surplus as own interval
                        surplus = ranges[k] - dif
                        seeds.append(y + dif+1)
                        ranges.append(surplus-1)
                        reset.append(True)
                    ranges[k] = dif
                    startdif = y - start
                    seeds[k] = mp[0]+startdif
                    reset.append(False)

print(seeds)
print(min(seeds))