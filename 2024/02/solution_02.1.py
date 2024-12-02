input = open('./input_02.txt', 'r')
lines = input.readlines()

ans = 0
for line in lines:
  digits = line.split()
  digits = [int(d) for d in digits]
  prev = digits[0]
  increasing = digits[0] < digits[-1]
  safe = True
  for digit in digits[1:]:
    if abs(digit - prev) > 3 or abs(digit - prev) < 1:
      safe = False
      break
    if digit < prev and increasing:
      safe = False
      break
    if digit > prev and not increasing:
      safe = False
      break
    prev = digit
  if safe:
    ans += 1
print(ans)