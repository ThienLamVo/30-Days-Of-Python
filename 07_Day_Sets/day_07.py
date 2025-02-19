it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f'Length of it_companies: {len(it_companies)}')
it_companies.add('Twitter')
other_companies = {'a', 'b', 'c'}
it_companies.update(other_companies)
it_companies.discard('c')
print("Difference between .remove() and .discard() is .discard() won't raise an error if an item does not exist in the set and .remove() will")

print(f'A joined with B: {A.union(B) }')
print(f'A insersection with B: {A.intersection(B)}')
print(f'Is A subset of B: {A.issubset(B)}')
print(f'Is A and B disjoint sets: {A.isdisjoint(B)}')
print(f'B joined with A: {B.union(A)}')
print(f'Symmetric difference between A and B: {A.symmetric_difference(B)}')
del A, B

age_set = set(age)
length_age_list = len(age)
length_age_set = len(age_set)
print(f'Length of age list: {length_age_list} and length of age set: {length_age_set}')
print(f'Strings are sequence of chars, lists are ordered collections of non-unique items that is changeable, tuples are ordered collections of non-unique items that are unchangeable, and set are unordered collections of unique items that are changeable')