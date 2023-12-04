input = open('./input_04.txt', 'r')
lines = input.readlines()

res = 0
for line in lines:
    nums = [int(num) for num in line.split() if num.isdigit()]
    wins = nums[:10]
    pts = 0.5
    for i in nums[10:]:
        if i in wins:
            pts += pts
    if pts > 0.5:
        res += int(pts)
print(res)