import re 

input = open('./input_02.txt', 'r')
lines = input.readlines()

def parser(line):
    n = len(line)
    i = 5
    gameId = line[i]
    i += 1
    while line[i].isdigit():
        gameId += line[i]
        i += 1
    
    i += 1
    turns = []
    while i < n:
        dic = {'g': 0, 'b': 0, 'r': 0}
        while i < n and line[i] != ';':
            i += 1
            number = line[i]
            i += 1
            while line[i].isdigit():
                number += line[i]
                i += 1
            i += 1
            dic[line[i]] = int(number)
            while i < n and line[i] != ',' and line[i] != ';':
                i += 1
        turns.append(dic)
        i += 1
    return int(gameId), turns

res = 0
for line in lines:
    id, turns = parser(line)
    found = False
    for dic in turns:
        for key, value in dic.items():
            if key == 'r' and value > 12 or key == 'g' and value > 13 or key == 'b' and value > 14:
                found = True
                break
        if found:
            break
    if not found:
        res += id
print(res)