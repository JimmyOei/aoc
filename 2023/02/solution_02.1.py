import re 

input = open('./input_02.txt', 'r')
lines = input.readlines()

pattern = re.compile(r'Game (\d+):((?: \d+ [a-z]+,?;)+)')
print(pattern)

# def parser(line):
#     n = len(line)
#     i = 6
#     gameId = line[i]
#     i += 1
#     while line[i].isDigit():
#         gameId += line[i]
#         i += 1
    
#     turns = []
#     while i < n:
#         while line[i] != ';':
#             i += 2
#             number = line[i]
#             while line[i].isDigit():
#                 number += line[i]
#                 i += 1
#             i += 1
#             color = line[i]
