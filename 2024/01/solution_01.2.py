input = open('./input_01.txt', 'r')
lines = input.readlines()

list1 = []
list2 = []

for line in lines:
    nums = line.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

ans = 0
for i in range(len(list1)):
    cnt = list2.count(list1[i])
    ans += (cnt*list1[i])
print(ans)