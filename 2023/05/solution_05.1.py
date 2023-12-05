input = open('./input_05.txt', 'r')
lines = input.readlines()

seeds = [int(num) for num in lines[0].split() if num.isdigit()]
reset = [True]*len(seeds)

for line in lines[1:]:
    mp = [int(num) for num in line.split() if num.isdigit()]
    if len(mp) > 0:
        start = mp[1]
        finish = mp[1]+mp[2]
        for j, x in enumerate(seeds):
            if reset[j] and x >= start and x <= finish:
                dif = x-start
                seeds[j] = mp[0]+dif
                reset[j] = False
    else:
        reset = [True]*len(seeds)

print(seeds)
print(min(seeds))