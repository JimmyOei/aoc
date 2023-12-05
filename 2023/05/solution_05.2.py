input = open('./input_05.txt', 'r')
lines = input.readlines()

nums = [int(num) for num in lines[0].split() if num.isdigit()]
ranges = [(nums[i], nums[i]+nums[i+1]) for i in range(0, len(nums), 2)]

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

for cat in data:
    newranges = []
    while len(ranges) > 0:
        s, f = ranges.pop()
        for a, b, c in cat:
            os = max(s, b)
            of = min(f, b + c)
            if os < of:
                newranges.append((os - b + a, of - b + a))
                if os > s:
                    ranges.append((s, os))
                if of < f:
                    ranges.append((of, f))
                break
        else:
            newranges.append((s, f))
    ranges = newranges

print(min(ranges)[0])