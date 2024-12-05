input = open('./input_05_rules.txt', 'r')
rules = input.readlines()
rules = [rule.strip() for rule in rules]
rules = [rule.split('|') for rule in rules]
rules = [[int(x) for x in rule] for rule in rules]

input2 = open('./input_05_updates.txt', 'r')
updates = input2.readlines()
updates = [update.strip() for update in updates]

ans = 0
for update in updates:
  nums = update.split(',')
  nums = [int(num) for num in nums]
  valid = False
  incorrect = False
  while not valid:
    valid = True
    for rule in rules:
      if rule[0] in nums and rule[1] in nums and nums.index(rule[0]) > nums.index(rule[1]):
        valid = False
        incorrect = True
        nums[nums.index(rule[0])] = rule[1]
        nums[nums.index(rule[1])] = rule[0]
  if incorrect:
    ans += nums[len(nums) // 2]
print(ans)
      
      