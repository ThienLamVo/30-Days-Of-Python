dog = {}
dog['name'] = 'roy'
dog['color'] = 'black'
dog['legs'] = 4
dog['age'] = 2
print(dog)
student = {}
student['first_name'] = 'a'
student['last_name'] = 'b'
student['gender'] = 'Male'
student['age'] = 23
student['marital status'] = 'Single'
student['skills'] = ['a', 'b']
student['country'] = 'USA'
student['city'] = 'c'
student['address'] = {'street': 'a', 'zipcode': '24060'}
print(student)
print(len(student))
print(student.get('skills'))
student.get('skills').append('c')
print(student.keys())
print(student.values())
print(student.items())
del student['address']
print(student)
del student
print(student)