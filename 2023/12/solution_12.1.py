input = open('./input_12.txt', 'r')
lines = input.readlines()
lines = [line.split() for line in lines]
L = [(list(line[0]), [int(i) for i in line[1].split(',')]) for line in lines]

def rec(s, c, i, j, cnt):
    while i < len(s) and cnt <= c[j]:
        if s[i] == '#':
            cnt += 1
        elif s[i] == '.' and cnt > 0:
            if c[j] != cnt:
                return 0
            cnt = 0
            j += 1
            if j == len(c):
                if '#' in s[i:]:
                    return 0
                return 1
        elif s[i] == '?':
            news = s.copy()
            news[i] = '#'
            ret = rec(news, c, i, j, cnt)
            newnews = s.copy()
            newnews[i] = '.'
            return ret + rec(newnews, c, i, j, cnt)
        i += 1
    if j+1 < len(c) or j+1 == len(c) and cnt != c[j]:
        return 0
    return 1

res = 0
for s, c in L:
    res += rec(s, c, 0, 0, 0)
print(res)


