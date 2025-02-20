for num in range(11):
  print(num)

count = 0
while count != 11:
  print(count)
  count += 1

for num in range(10, -1, -1):
  print(num)

count = 10
while count != -1:
  print(count)
  count -= 1

hashtag = '#'
for i in range(7):
  print(hashtag)
  hashtag += '#'

for i in range(8):
  for j in range(8):
    print('# # # # # # # #')

for i in range(11):
  print(f'{i} x {i} = {i * i}')

techs = ['Python', 'Numpy','Pandas','Django', 'Flask']
for tech in techs:
  print(tech)

for i in range(101):
  if i % 2 != 1:
    print(i)

for i in range(101):
  if i % 2 == 1:
    print(i)

sum_all = 0
for i in range(101):
  sum_all += i
else:
  print(f'The sum of all numbers is {sum_all}')

sum_even = 0
sum_odd = 0
for i in range(101):
  if i % 2 == 0:
    sum_even += i
  else:
    sum_odd += i
else:
  print(f'The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reversed = []
for fruit in fruits:
  fruits_reversed.insert(0, fruit)
print(fruits)
print(fruits_reversed)