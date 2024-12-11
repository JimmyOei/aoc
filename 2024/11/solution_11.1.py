input = open('./input_11.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]
nums = [int(x) for x in lines[0].split(' ')]

times = 75
for i in range(times):
    j = 0
    while j < len(nums):
        num = nums[j]
        strnum = str(num)
        if num == 0:
            nums[j] = 1
        elif len(strnum) % 2 == 0:
            m = len(strnum)//2
            nums[j] = int(strnum[:m])
            nums.insert(j+1, int(strnum[m:]))
            j += 1
        else:
            nums[j] *= 2024
        j += 1

print(len(nums))