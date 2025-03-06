from functools import reduce
#
## Python allows a nested function to access the outer scope of the enclosing function. 
## This is is known as a Closure. 
## Closure is created by nesting a function inside another encapsulating function and then returning the inner function.
## See the example below.
#
#def add_ten():
#    ten = 10
#    def add(num):
#        return num + ten
#    return add
#
#closure_result = add_ten()
#print(closure_result(5))  # 15
#print(closure_result(10))  # 20
#
## Decorators
## Design pattern in Python that allows user to add new functionality to existing object without modifying structure
## Decorators usually called before definition of function you want to decorate
#
#def uppercase_decorator(function):
#    def wrapper():
#        func = function()
#        make_uppercase = func.upper()
#        return make_uppercase
#    return wrapper
#
#@uppercase_decorator
#def greeting():
#    return 'Welcome to Python'
#print(greeting())
#
## First Decorator
#def uppercase_decorator(function):
#    def wrapper():
#        func = function()
#        make_uppercase = func.upper()
#        return make_uppercase
#    return wrapper
#
## Second decorator
#def split_string_decorator(function):
#    def wrapper():
#        func = function()
#        splitted_string = func.split()
#        return splitted_string
#
#    return wrapper
#
#@split_string_decorator
#@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
#def greeting():
#    return 'Welcome to Python'
#print(greeting())   # WELCOME TO PYTHON
#
## Parameters in Decorator functions
#def decorator_with_parameters(function):
#    def wrapper_accepting_parameters(para1, para2, para3):
#        function(para1, para2, para3)
#        print("I live in {}".format(para3))
#    return wrapper_accepting_parameters
#
#@decorator_with_parameters
#def print_full_name(first_name, last_name, country):
#    print("I am {} {}. I love to teach.".format(
#        first_name, last_name, country))
#
#print_full_name("Asabeneh", "Yetayeh",'Finland')
#
## Built-in functions
## Map
#numbers = [1, 2, 3, 4, 5] # iterable
#def square(x):
#    return x ** 2
#numbers_squared = map(square, numbers)
#print(list(numbers_squared))    # [1, 4, 9, 16, 25]
## Lets apply it with a lambda function
#numbers_squared = map(lambda x : x ** 2, numbers)
#print(list(numbers_squared))    # [1, 4, 9, 16, 25]
#
#numbers_str = ['1', '2', '3', '4', '5']  # iterable
#numbers_int = map(int, numbers_str)
#print(list(numbers_int))    # [1, 2, 3, 4, 5]
#
#names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
#
#def change_to_upper(name):
#    return name.upper()
#
#names_upper_cased = map(change_to_upper, names)
#print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
#
## Let us apply it with a lambda function
#names_upper_cased = map(lambda name: name.upper(), names)
#print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
#
## Filter
## Lets filter only even nubers
#numbers = [1, 2, 3, 4, 5]  # iterable
#
#def is_even(num):
#    if num % 2 == 0:
#        return True
#    return False
#
#even_numbers = filter(is_even, numbers)
#print(list(even_numbers))       # [2, 4]
#
#even_numbers = filter(lambda x: x % 2 == 0, numbers)
#print(list(even_numbers))
#
## Filter long name
#names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
#def is_name_long(name):
#    if len(name) > 7:
#        return True
#    return False
#
#long_names = filter(is_name_long, names)
#print(list(long_names))         # ['Asabeneh']
#
#long_names = filter(lambda name: len(name) > 7, names)
#print(list(long_names))         # ['Asabeneh']
#
## Reduce
## Import from functools module
## Returns single value
#numbers_str = ['1', '2', '3', '4', '5']  # iterable
#def add_two_nums(x, y):
#    return int(x) + int(y)
#
#total = reduce(add_two_nums, numbers_str)
#print(total)    # 15
#
#countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#countries_uppercase = map(lambda country: country.upper(), countries)
#print(list(countries_uppercase))
#
#numbers_squared2 = map(lambda num: num ** 2, numbers)
#print(list(numbers_squared2))
#
#countries_without_land = filter(lambda x: 'land' not in x, countries)
#print(list(countries_without_land))
#
#countries_six_characters = filter(lambda x: len(x) != 6, countries)
#print(list(countries_six_characters))
#
#countries_start_with_E = filter(lambda x: x[0] != 'E', countries)
#print(list(countries_start_with_E))
#
#def get_string_lists(a_list):
#    return filter(lambda item: type(item) == str, a_list)
#
#print(list(get_string_lists(countries)))
#print(list(get_string_lists(numbers)))
#
#numbers_reduced = reduce(lambda x, y: x + y, numbers)
#print(numbers_reduced)
#
#countries_reduced = reduce(lambda x, y: x + ', ' + y, countries)
#print(countries_reduced + ' are north European countries')
#
#countries_first_letters = dict()
#for country in countries:
#    if country[0] not in countries_first_letters:
#        countries_first_letters[country[0]] = 1
#    else:
#        countries_first_letters[country[0]] += 1
#print(countries_first_letters)

countries = ['a', 'b', 'ccland', 'd', 'elanddafsaf', 'f']
names = ['gg', 'hh', 'ii', 'jj']
numbers = [1, 2, 3, 4]

# map applies function to each item in a list and can return multiple items
# filter applies function to each item and returns those that return True
# reduce applies function to each item and returns a single item

# higher level function is using functions within functions nesting them essentially
# closure is when a nested inner function can access variables outside of its local scope within the outer function
# decorator a way to modify existing functionality of a function without modifying its structure

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

def uppercase(phrase):
    return phrase.upper()

countries_uppercase = map(uppercase, countries)
print(list(countries_uppercase))
countries_uppercase2 = map(lambda x: x.upper(), countries)
print(list(countries_uppercase2))

numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))

names_uppercase = map(lambda x: x.upper(), names)
print(list(names_uppercase))

countries_no_land = filter(lambda x: x.find('land') == -1, countries)
print(list(countries_no_land))

countries_six_chars = filter(lambda x: len(x) != 6, countries)
print(list(countries_six_chars))

countries_six_chars_or_longer = filter(lambda x: len(x) < 6, countries)
print(list(countries_six_chars_or_longer))

countries_start_e = filter(lambda x: x[0].lower() != 'e', countries)
print(list(countries_start_e))

numbers_to_string_capitalized = reduce(lambda x, y: x + y, map(lambda x: str(x), numbers))
print(numbers_to_string_capitalized)

trash = [1, 2, '3', 4, '5']
def get_string_lists(lst):
    return list(filter(lambda x: type(x) == str, trash))
trash_filtered = get_string_lists(trash)
print(trash_filtered)

sum_reduced = reduce(lambda x, y: x + y, numbers)
print(sum_reduced)

countries_sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are all north European countries'
print(countries_sentence)

def categorize_countries(lst, pattern):
    return filter(lambda x: x.find(pattern) != -1, lst)

def countries_starting_letter(lst):
    dic = {}
    for country in lst:
        if country[0].lower() in dic:
            dic[country[0].lower()] += 1
        else:
            dic[country[0].lower()] = 1
    return dic
print(countries_starting_letter(countries))