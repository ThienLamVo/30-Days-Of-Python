empty_tuple = ()
brother = ('Brother 1', 'Brother 2')
sister = ('Sister 1', 'Sister 2')
siblings = brother + sister
print(siblings)
print('Number of siblings: ' + str(len(siblings)))
parents = ('Father', 'Mother')
family_members = siblings + parents
print(family_members)

siblings = family_members[0:4]
print(siblings)
parents = family_members[4:]
print(parents)
fruits = ('Orange', 'Strawberry')
vegetables = ('Lettuce', 'Cabbage')
animal_products = ('Butter', 'Milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
middle_items = food_stuff_lt[2:4]
print(middle_items)
first_three = food_stuff_lt[0:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Is Estonia a nordic country: ' + str('Estonia' in nordic_countries))
print('Is Iceland a nordic country: ' + str('Iceland' in nordic_countries))
