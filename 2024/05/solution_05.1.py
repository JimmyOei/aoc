rules = open('./input_05_rules.txt', 'r')
rules = input.readlines()
rules = [rule.strip() for rule in rules]
rules = [rule.split('|') for rule in rules]
rules = [[int(x) for x in rule] for rule in rules]

updates = open('./input_05_updates.txt', 'r')
updates = updates.readlines()
updates = [update.strip() for update in updates]

ans = 0
for update in updates:
  nums = update.split(',')
  nums = [int(num) for num in nums]
  valid = True
  for rule in rules:
    if rule[0] in nums and rule[1] in nums and nums.index(rule[0]) > nums.index(rule[1]):
      valid = False
      break
  if valid:
    ans += nums[len(nums) // 2]
    print(nums, ans)
print(ans)
      
      