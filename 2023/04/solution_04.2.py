input = open('./input_04.txt', 'r')
lines = input.readlines()

n = len(lines)
cnts = [1]*n

for i, line in enumerate(lines):
    nums = [int(num) for num in line.split() if num.isdigit()]
    wins = nums[:10]
    j = i+1
    curr = cnts[i]
    for l in nums[10:]:
        if l in wins:
            cnts[j] += curr
            j += 1

res = 0
for i in cnts:
    res += i

print(res)