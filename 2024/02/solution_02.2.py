input = open('./input_02.txt', 'r')
lines = input.readlines()

def isSafe(i, j, increasing):
  if abs(i - j) > 3 or abs(i - j) < 1:
    return False
  if i < j and increasing:
    return False
  if i > j and not increasing:
    return False
  return True

def isLevelSafe(digits, increasing):
  prev = digits[0]
  for digit in digits[1:]:
    if not isSafe(digit, prev, increasing):
      return False
    prev = digit
  return True

ans = 0
for line in lines:
  digits = line.split()
  digits = [int(d) for d in digits]

  prev = digits[1]
  sep = 0
  for digit in digits[2:]:
    sep += prev-digit
    prev = digit
  increasing = sep < 0

  if isLevelSafe(digits, increasing):
    ans += 1
    continue
  for i in range(len(digits)):
    digitsWithoutI = digits[:i] + digits[i+1:]
    if isLevelSafe(digitsWithoutI, increasing):
      ans += 1
      break
print(ans)