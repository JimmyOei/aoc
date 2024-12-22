input = open('./input_22.txt', 'r')
lines = input.readlines()
lines = [int(line.strip()) for line in lines]

prune_value = 16777216
secret_iteraitons = 2000

def calc_next_secret(value):
    y1 = ((value * 64) ^ value) % prune_value
    y2 = ((y1 // 32) ^ y1) % prune_value
    y3 = ((y2 * 2048) ^ y2) % prune_value
    return y3

ans = 0
for line in lines:
    secret = line
    for i in range(secret_iteraitons):
        secret = calc_next_secret(secret)
    ans += secret
print(ans)

