def add_all_nums(*nums):
  sum = 0
  for num in nums: 
    sum += num
  return sum
print(add_all_nums(1))
print(add_all_nums(1, 2))
print(add_all_nums(1, 2, 3))