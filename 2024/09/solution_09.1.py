input = open('./input_09.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]
disk = [int(x) for x in list(lines[0])]

ans = 0
i = 0
k = 0
idi = 0
j = len(disk) - 1
idj = (j // 2)

while i < j:
    if i % 2 == 0:
        while disk[i] > 0:
            ans += idi*k
            disk[i] -= 1
            k += 1
        i += 1
        idi += 1
    else:
        while disk[j] > 0 and disk[i] > 0:
            ans += idj*k
            disk[i] -= 1
            disk[j] -= 1
            k += 1
        if disk[j] == 0:
            j -= 2
            idj -= 1
        if disk[i] == 0:
            i += 1

while i < len(disk):
    if i % 2 == 0:
        while disk[i] > 0:
            ans += idi*k
            disk[i] -= 1
            k += 1
        i += 1
        idi += 1
    else:
        while disk[i] > 0:
            k += 1
            disk[i] -= 1
        i += 1
print(ans)
        