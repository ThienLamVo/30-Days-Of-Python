from math import pi
from array import array
def add_two_numbers(a, b):
  return a + b
print(f'{add_two_numbers(1, 2)}')

def area_of_circle(radius):
  return pi * radius ** 2
print(f'Area of circle radius 1: {area_of_circle(2)}')

def add_all_nums(*nums):
  check_correct = True
  sum = 0
  for num in nums: 
    num_type = type(num)
    if num_type == int or num_type == float or num_type == complex:
      sum += num
    else:
      print(f'{num} is not a number type')
      check_correct = False
      break
  if check_correct:
    return sum
print(add_all_nums(1))
print(add_all_nums(1, 2))
print(add_all_nums(1, 2, 3))
print(add_all_nums(1, 2, '3'))

def convert_celsius_to_fahrenheit(c_temp):
  return (c_temp * 9 / 5) + 32
print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(100))

def check_season(name_month):
  if name_month == 'December' or name_month == 'January' or name_month =='February':
    return 'Winter'
  elif name_month == 'March' or name_month == 'April' or name_month == 'May':
    return 'Spring'
  elif name_month == 'June' or name_month == 'July' or name_month == 'August':
    return 'Summer'
  elif name_month == 'September' or name_month == 'October' or name_month == 'November':
    return 'Autumn'
  else:
    return 'Incorrect spelling or not a month'
print(check_season('January'))
print(check_season('january'))
print(check_season('ball'))

def solve_quadratic_eqn(a, b, c):
  x1 = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
  x2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
  return x1, x2

print(solve_quadratic_eqn(1, 1, 1))
print(solve_quadratic_eqn(2, 4, 8))
print(solve_quadratic_eqn(3, 6, 9))

def print_list(a_list):
  for item in a_list:
    print(item)
print_list(['a', 'b', 'c'])
print_list(['a', 1, 'b', 2, 'c', 3])

first_array = [1, 2, 3]
second_array = ['1', '2', '3']
def reverse_list(an_array):
  reversed_list_to_return = []
  for item in an_array:
    reversed_list_to_return.insert(0, item)
  return reversed_list_to_return
print(reverse_list(first_array))
print(reverse_list(second_array))

def capitalize_list_items(a_list):
  list_to_return = []
  for item in a_list:
    if type(item) == str:
      list_to_return.append(item.upper())
    else:
      print(f'{item} is not a string')
  return list_to_return
print(capitalize_list_items(['a', 'ab', 'abc']))
print(capitalize_list_items([1, 2, 3]))

def add_item(a_list, new_item):
  return a_list.append(new_item)
a_list = [1]
add_item(a_list, 2)
print(a_list)

def remove_item(a_list, item):
  if item in a_list:
    a_list.remove(item)
  return a_list
a_list = [1, 2]
remove_item(a_list, 1)
print(a_list)
remove_item(a_list, 3)
print(a_list)

def sum_of_numbers(num):
  sum = 0
  for i in range(num + 1):
    sum += i
  return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


def sum_of_odds(num):
  sum = 0
  for i in range(num + 1):
    if i % 2 == 1:
      sum += i
  return sum
print(sum_of_odds(5))

def sum_of_even(num):
  sum = 0
  for i in range(num + 1):
    if i % 2 == 0:
      sum += i
  return sum
print(sum_of_even(5))

def evens_and_odd(num):
  odds = 0
  evens = 0
  for i in range(num + 1):
    if i % 2 == 0:
      evens += 1
    else:
      odds += 1
  return f'The number of odds are {odds}\nThe number of evens are {evens}'
print(evens_and_odd(100))

def factorial(num):
  product = 1
  for i in range(1, num + 1):
    product *= i
  return product
print(factorial(7))

def is_empty(anything):
  if not anything:
    return True
  else:
    return False
print(is_empty([]))
print(is_empty([1]))

a_list = [1, 3, 2, 4, 3]

def calculate_mean(a_list):
  sum = 0
  for item in a_list:
    sum += item
  sum /= len(a_list)
  return sum
print(calculate_mean(a_list))

def calculate_median(a_list):
  a_list.sort()
  return a_list[len(a_list) // 2]
print(calculate_median(a_list))

def calculate_mode(a_list):
  quantity = {}
  for item in a_list:
    if not item in quantity:
      quantity[item] = 1
    else:
      quantity[item] += 1
  return [x for x, highest_appearing in quantity.items() if highest_appearing == max(quantity.values())]
print(calculate_mode(a_list))

def calculate_range(a_list):
  a_list.sort()
  if len(a_list) > 1:
    return a_list[len(a_list) - 1] - a_list[0]
  else:
    return 'No Range'
print(calculate_range(a_list))

def calculate_variance(a_list):
  mean = calculate_mean(a_list)
  sum = 0
  for item in a_list:
    sum += (item - mean) ** 2
  return sum / (len(a_list) - 1)

def calculate_std(a_list):
  variance = calculate_variance(a_list)
  return variance ** 0.5

def is_prime(num):
  for i in range(1, num + 1):
    if num % i == 0 and (i > 1 and i < num):
      return False
  return True
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print()

def is_unique(a_list):
  for i in range(len(a_list) - 1, -1, -1):
    ind = a_list.index(a_list[i])
    if (ind != i):
      return False
  return True
print(is_unique([1, 2, 3]))
print(is_unique([3, 2, 1, 1]))
print(is_unique(['a', 1, '1']))
print(is_unique([1, 1, '1']))
print()

def same_type(a_list):
  if len(a_list) == 0:
    return False
  elif len(a_list) == 1:
    return True
  else:
    type_checked = type(a_list[0])
    for item in a_list:
      if type_checked != type(item):
        return False
  return True
print(same_type([1, 2, 3]))
print(same_type([3, 2, 1, 1]))
print(same_type(['a', 1, '1']))
print(same_type([1, 1, '1']))
print(same_type(['1', '1', '1']))
print()
print()
print()

def is_legal_variable(str_var):
  if len(str_var) < 1:
    return False
  if str_var.isalpha():
    return True
  elif str_var.isalnum():
    return str_var[0].isalpha()
  else:
    for i in str_var:
      if not i.isalnum() and i != '_':
        return False
  return True

print(is_legal_variable('myvar'))
print(is_legal_variable('my_var'))
print(is_legal_variable('_my_var'))
print(is_legal_variable('m2yvar'))
print(is_legal_variable('myvar2'))
print(is_legal_variable('2myvar2'))
print(is_legal_variable('my-var2'))
print(is_legal_variable('my var2'))
print()