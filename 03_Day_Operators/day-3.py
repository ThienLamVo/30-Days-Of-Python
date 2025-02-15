from math import pi, sqrt
'''
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

age = 24
height = 5.8
complex_number = 1 + 1j
print(type(age))
print(type(height))
print(type(complex_number))

base_triangle = float(input('Enter base: '))
height_triangle = float(input('Enter height: '))
print('The area of the triangle is ' + str(0.5 * base_triangle * height_triangle))

side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
print('The perimeter of the triangle is ' + str(side_a + side_b + side_c))

length_rectangle = float(input('Enter length: '))
width_rectangle = float(input('Enter width: '))
print('The area of the rectangle is ' + str(length_rectangle * length_rectangle))


print('The perimeter of the rectangle is ' + str(2 * (length_rectangle + length_rectangle)))

radius_circle = float(input('Enter radius: '))
print('The area of the circle is ' + str(pi * radius_circle ** 2))
print('The circumference of the circle is ' + str(2 * pi * radius_circle))

x1 = 0
x2 = 1

y1 = 2 * x1 - 2
y2 = 2 * x2 - 2

slope_one = (y2 - y1) / (x2 - x1)

print('Slope 1: ' + str(slope_one))

y_intercept = 2 * 0 - 2
x_intercept = (0 + 2) / 2
print('y-intercept is at y = ' + str(y_intercept))
print('x-intercept is at x = ' + str(x_intercept))

slope_two = (10 - 2) / (6 - 2)

print('Slope 2: ' + str(slope_two))

distance_between_points = sqrt((10-2)**2 + (6-2)**2)
print('Distance between points is: ' + str(distance_between_points))

if slope_one == slope_two:
    print('Slopes are the same')
else:
    print('Slopes are different')

x_value = -4
y_value = (x_value) ** 2 + 6 * (x_value) + 9
print('Y-value at ' + str(x_value) + ' is ' + str(y_value))
x_value = -3
y_value = (x_value) ** 2 + 6 * (x_value) + 9
print('Y-value at ' + str(x_value) + ' is ' + str(y_value))
x_value = -2
y_value = (x_value) ** 2 + 6 * (x_value) + 9
print('Y-value at ' + str(x_value) + ' is ' + str(y_value))

length_of_python = len('python')
length_of_dragon = len('dragon')
print('Length of python and dragon are the same?: ' + str(length_of_python == length_of_dragon))

on_is_in_both_words = 'on' in 'python' and 'on' in 'dragon'
print('Is "on" in both "python" and "dragon"?: ' + str(on_is_in_both_words))

jargon_check = 'jargon' in 'I hope this course is not full of jargon'
print('Is "jargon" in "I hope this course is not full of jargon"?: ' + str(jargon_check))

str_to_float_to_string = str(float(length_of_python))
print('Converted length to float to string: ' + str_to_float_to_string)

num_one = 1
num_two = 2

even_number_check = num_one % 2 == 0
print('Is ' + str(num_one) + ' an even number?: ' + str(even_number_check))
even_number_check = num_two % 2 == 0
print('Is ' + str(num_two) + ' an even number?: ' + str(even_number_check))

floor_division_of_7 = 7 // 3
int_converted_value = int(2.7)

print('Is floor division of 7 by 3 equal to int converted value of 2.7: ' + str(floor_division_of_7 == int_converted_value))

string_ten = '10'
value_ten = 10
print('Is "10" equal to 10: ' + str(string_ten == value_ten))

nine_point_eight = '9.8'
nine_point_eight = int(float(nine_point_eight))
print(int(float(nine_point_eight)))
print('Is "int(9.8)" equal to 10: ' + str(nine_point_eight == 10))

hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
print('Your weekly earning is ' + str(hours * rate_per_hour))

years_lived = int(input('Enter number of years you have lived: '))
print('You have lived for ' + str(years_lived * 365 * 24 * 60 * 60) + ' seconds.')

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
'''
for i in range(5):
    for j in range(5):
        if (i == 0):
            print(i + 1, end=' ')
        else:
            if j == 0 or j == 2:
                print(i + 1, end=' ')
            elif j == 1:
                print(1, end=' ')
            elif j == 3:
                print((i + 1) ** 2, end=' ')
            elif j == 4:
                print((i + 1) ** 3, end=' ')
    print()