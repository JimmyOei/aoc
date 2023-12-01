import re

input = open('./input_01.txt', 'r')
lines = input.readlines()

val = 0
for line in lines:
    digits = re.sub("[^0-9]", "", line)
    val += int(digits[0] + digits[-1])

print("res:", val)