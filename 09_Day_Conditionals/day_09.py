age_input = int(input('Enter your age: '))
if age_input >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18 - age_input} more year(s) to learn to drive')

my_age = 25
your_age = int(input('Enter your age: '))
age_diff = your_age - my_age
if age_diff < 0:
    if age_diff == -1:
        print('I am 1 year older than you.')
    else:
        print(f'I am {my_age - your_age} years older than you.')
elif age_diff == 0:
    print('We are the same age.')
elif age_diff == 1:
    print('You are 1 year older than me.')
else:
    print(f'You are {age_diff} years older than me')

num_one = input('Enter number one: ')
num_two = input('Enter number two: ')
if num_one > num_two:
    print(f'{num_one} is greater than {num_two}')
elif num_one == num_two:
    print(f'{num_one} is equal to {num_two}')
else:
    print(f'{num_one} is smaller than {num_two}')

grade_score = int(input('What was your score: '))
if grade_score <= 49:
    print('F')
elif grade_score <= 59:
    print('D')
elif grade_score <= 69:
    print('C')
elif grade_score <= 89:
    print('B')
else:
    print('A')

month = input('What month is it: ')
if month == 'September' or month == 'October' or month == 'November':
    print('Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('Summer')
else:
    print('Incorrect spelling or not a month')

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter new fruit: ')
if new_fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(new_fruit)
    print(fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

skills = person.get('skills')
if skills != None:
    print(f'Middle skill: {skills[int(len(skills) / 2)]}')
    if 'Python' in skills:
        print('Python is in skills')
    else:
        print('Python is not in skills')
    if len(skills) == 2 and 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('Unknown title')
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person.get('first_name')} {person.get('last_name')} lives in {person.get('country')}. He is married.")
