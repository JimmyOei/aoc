input = open('./input_03.txt', 'r')
lines = input.readlines()
lines = [list(line.strip('\n')) for line in lines]

m = len(lines)
n = len(lines[0])

def parsenumber(i , j):
    while j > 0 and lines[i][j-1].isdigit():
        j -= 1
    number = ''
    while j < n and lines[i][j].isdigit():
        number += lines[i][j]
        lines[i][j] = '.'
        j += 1
    return int(number)


res = 0
for i, line in enumerate(lines):
    for j, v in enumerate(line):
        if v == '*':
            nums = []
            if i > 0 and lines[i-1][j].isdigit():
                nums.append(parsenumber(i-1, j))
            if i < m-1 and lines[i+1][j].isdigit():
                nums.append(parsenumber(i+1, j))
            if j > 0 and lines[i][j-1].isdigit():
                nums.append(parsenumber(i, j-1)) 
            if j < n-1 and lines[i][j+1].isdigit():
                nums.append(parsenumber(i, j+1))
            if i > 0 and j > 0 and lines[i-1][j-1].isdigit():
                nums.append(parsenumber(i-1, j-1))
            if i > 0 and j < n-1 and lines[i-1][j+1].isdigit():
                nums.append(parsenumber(i-1, j+1))
            if i < m-1 and j > 0 and lines[i+1][j-1].isdigit():
                nums.append(parsenumber(i+1, j-1))
            if i < m-1 and j < n-1 and lines[i+1][j+1].isdigit():
                nums.append(parsenumber(i+1, j+1))
            if len(nums) == 2:
                res += (nums[0]*nums[1])
print(res)