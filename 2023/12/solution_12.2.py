input = open('./input_12.txt', 'r')
lines = input.readlines()
lines = [line.split() for line in lines]
L = [(list((line[0]+'?')*5)[:-1], [int(i) for i in ((line[1]+',')*5).split(',')[:-1]]) for line in lines]

def rec(s, c, i, j, cnt, dp):
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
            if dp[i][j][cnt] == None:
                news = s.copy()
                news[i] = '#'
                newnews = s.copy()
                newnews[i] = '.'
                dp[i][j][cnt] = rec(news, c, i, j, cnt, dp) + rec(newnews, c, i, j, cnt, dp)
            return dp[i][j][cnt]
        i += 1
    if j+1 < len(c) or j+1 == len(c) and cnt != c[j]:
        return 0
    return 1

res = 0
for s, c in L:
    dp = [[[None for _ in range(max(c)+1)] for _ in range(len(c))] for _ in range(len(s))]
    res += rec(s, c, 0, 0, 0, dp)
print(res)


