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

prices = []
for line in lines:
    secret = line
    digits = [int(str(secret)[-1])]
    for i in range(secret_iteraitons):
        secret = calc_next_secret(secret)
        digits.append(int(str(secret)[-1]))
    prices.append(digits)

n = len(prices[0])
seqsseqs = {}
for i in range(len(prices)):
  prev = prices[i][0]
  seqs = {}
  seq = []
  for j in range(1, n):
    if len(seq) == 4:
      seq.pop(0)
      seq.append(prices[i][j] - prev)
      if str(seq) not in seqs:
        seqs[str(seq)] = prices[i][j]
    else:
      seq.append(prices[i][j] - prev)
    prev = prices[i][j]
  for seq in seqs.keys():
    if seq not in seqsseqs:
      seqsseqs[seq] = seqs[seq]
    else:
      seqsseqs[seq] += seqs[seq]

ans = max(seqsseqs.values())
print(ans)

