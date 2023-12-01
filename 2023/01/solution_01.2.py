import re

input = open('./input_01.txt', 'r')
lines = input.readlines()

val = 0
for line in lines:
    parsedline = line.replace("one", 'o1e').replace("two", 't2o').replace("three", 't3e').replace("four", 'f4r').replace("five", 'f5e').replace("six", '6').replace("seven", '7').replace("eight", 'e8t').replace("nine", 'n9e')
    digits = re.sub("[^0-9]", "", parsedline)
    val += int(digits[0] + digits[-1])

print("res:", val)