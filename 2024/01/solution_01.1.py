input = open('./input_01.txt', 'r')
lines = input.readlines()

list1 = []
list2 = []

for line in lines:
    nums = line.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

list1.sort()
list2.sort()

ans = 0
for i in range(len(list1)):
    ans += abs(list1[i] - list2[i])
print(ans)