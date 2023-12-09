input = open('./input_09.txt', 'r')
lines = input.readlines()

def rec(nums):
    dif = []
    for i in range(len(nums)-1):
        dif.append(nums[i+1] - nums[i])
    if all(j == 0 for j in dif):
        return dif[0]
    return dif[0] - rec(dif)

res = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    res += nums[0] - rec(nums)
print(res)
