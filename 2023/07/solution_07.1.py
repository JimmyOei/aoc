input = open('./input_07.txt', 'r')
lines = input.readlines()

types = [[] for _ in range(7)]

def get_card_value(card):
    if card.isdigit():  
        return int(card)  
    elif card == 'T':  
        return 10  
    elif card == 'J':  
        return 11  
    elif card == 'Q':  
        return 12  
    elif card == 'K':  
        return 13  
    elif card == 'A':  
        return 14 

for line in lines:  
    hand, bid = line.strip().split(' ')
    bid = int(bid)
    cnts = {}
    for c in hand:
        if c in cnts:
            cnts[c] += 1
        else:
            cnts[c] = 1
    maxcnt = max(cnts.values())
    if maxcnt == 5:
        types[0].append((hand, bid))
    elif maxcnt == 4:
        types[1].append((hand, bid))
    elif maxcnt == 3:
        if 2 in cnts.values():
            types[2].append((hand, bid))
        else:
            types[3].append((hand, bid))
    elif maxcnt == 2:
        if len(cnts.values()) == 3:
            types[4].append((hand, bid))
        else:
            types[5].append((hand, bid))
    else:
        types[6].append((hand, bid))

i = len(lines)
res = 0
for t in types:
    t.sort(key=lambda x: (  
        get_card_value(x[0][0]), get_card_value(x[0][1]), get_card_value(x[0][2]), get_card_value(x[0][3]), get_card_value(x[0][4]), int(x[1])  
    ), reverse=True)
    for h, b in t:
        res += (b * i)
        i -= 1

print(res)