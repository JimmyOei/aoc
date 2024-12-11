input = open('./input_11.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]
nums = [int(x) for x in lines[0].split(' ')]
cnts = [1] * len(nums)

times = 75
for i in range(times):
    j = 0
    while j < len(nums):
        num = nums[j]
        cnt = cnts[j]
        strnum = str(num)
        if num == 0:
            nums[j] = 1
        elif len(strnum) % 2 == 0:
            m = len(strnum)//2
            newnum1 = int(strnum[:m])
            newnum2 = int(strnum[m:])
            del cnts[j]
            del nums[j]
            jj = 0
            if newnum1 == newnum2:
              cnt += cnt
            if newnum1 in nums and nums.index(newnum1) < j:
                cnts[nums.index(newnum1)] += cnt
                jj -= 1
            else:
                nums.insert(j, newnum1)
                cnts.insert(j, cnt)
                jj += 1
            if newnum1 != newnum2:
              if newnum2 in nums and nums.index(newnum2) < j:
                  cnts[nums.index(newnum2)] += cnt
                  jj -= 1
              else:
                  nums.insert(j, newnum2)
                  cnts.insert(j, cnt)
                  jj += 1
            if jj == 2:
                j += 1
            if jj < 0:
                j -= 1
        else:
            nums[j] *= 2024
        j += 1

ans = 0
for i in range(len(cnts)):
    ans += cnts[i]

print(ans)