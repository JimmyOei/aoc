input = open('./input_07.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]

def is_valid(target, val, nums, i):
  if i == len(nums):
    return val == target
  if val > target:
    return False
  return is_valid(target, val * nums[i], nums, i + 1) or is_valid(target, val + nums[i], nums, i + 1)

ans = 0
for line in lines:
  line = line.replace(':', '')
  nums = line.split(' ')
  nums = [int(num) for num in nums]
  target = nums[0]
  if is_valid(target, int(nums[1]), nums[2:], 0):
    ans += target

print(ans)