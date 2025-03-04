import random, string

def random_user_id():
    possible_choices = list(string.ascii_letters + string.digits)
    return ''.join(random.choices(possible_choices, k = 6))
print(random_user_id())

def user_id_gen_by_user():
    possible_choices = list(string.ascii_letters + string.digits)
    num_chars = int(input('Input length of id: '))
    num_ids = int(input('Input number of ids: '))
    for i in range(num_ids):
        print(''.join(random.choices(possible_choices, k = num_chars)))
user_id_gen_by_user()

def rgb_color_gen():
    return f'rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})'
print(rgb_color_gen())

def list_of_hexa_colors():
    num_colors = int(input('How many colors: '))
    for i in range(num_colors):
        print('#' + ''.join(random.choices('0123456789abcdef', k=6)))
list_of_hexa_colors()

def list_of_rgb_colors():
    num_colors = int(input('How many colors: '))
    for i in range(num_colors):
        print(rgb_color_gen())
list_of_rgb_colors()

def generate_colors(color_code, num):
    ans = []
    if color_code == 'hexa':
        for i in range(num):
            ans.append('#' + ''.join(random.choices('0123456789abcdef', k=6)))
    elif color_code == 'rgb':
        for i in range(num):
            ans.append(f'rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})')
    else:
        print('Improper format')
        return None
    return ans
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

def shuffle_list(a_list):
    random.shuffle(a_list)
    return a_list
a_list = [1, 2, 3, 4, 5]
print(shuffle_list(a_list))

def seven_unique_digits():
    ans = []
    while len(ans) != 7:
        digit = random.randint(0, 9)
        if digit not in ans:
            ans.append(digit)
    return ans

print(seven_unique_digits())