numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
even_numbers_only = [num for num in numbers if num > 0]
print(even_numbers_only)
numbers = [i for i in range(11)]
squares = [i * i for i in range(11)]
numbers_and_squares = [(i, i * i) for i in range(11)]
even_numbers = [i for i in range(21) if i % 2 == 0]
odd_numbers = [i for i in range(21) if i % 2 != 0]
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in list_of_lists for num in sublist]
print(flattened_list)

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

def power(x):
  return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers_positive = [num for num in numbers if num > 0]
print(numbers_positive)

list_of_lists2 =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_of_lists2_flattened = [num for row in list_of_lists2 for num in row]
list_of_lists2_flattened = [num for row in list_of_lists2_flattened for num in row]
print(list_of_lists2_flattened)

list_of_tuples = [(i, 1, i, i ** 2, i ** 3, i ** 4, i **5) for i in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_flattened = [[term, term[0: 3], term2] for terms in countries for term, term2 in terms]
print(countries_flattened)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dictionary = [{'country': term1, 'city': term2} for terms in countries for term1, term2 in terms]
print(countries_dictionary)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concatentated = [a + ' ' + b for firstlast in names for a, b in firstlast]
print(names_concatentated)