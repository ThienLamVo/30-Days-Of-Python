import re
print(dir(re))

# re.match() searches beginning of first line of string and return matched objects if found otherwise None
# re.search() returns match object if there is one anywhere including multiline strings
# re.findall returns list containing all matches
# re.split take string, splits it at match points, and returns list
# re.sub replaces one or many matches within a string

# Match
# Syntax re.match(substring, string, re.I)
txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
# re.I is case ignore
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None



# Search
# re.search(substring, string, re.I)
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first



# Findall
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']




# Replacing substring
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol


# Writing RegEx Patterns
import re

# RegEx variable
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!




paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

word_set = []
paragraph_split = paragraph.split(' ')
for word in paragraph_split:
    for letter in word:
        if letter == '.':
            word = word.replace(letter, '')
    flag = False
    for existing_word in word_set:
        if word in existing_word:
            flag = True
            break
    if not flag:
        length = 0
        for current_word in paragraph_split:
            if word in current_word:
                length += 1
        word_set.append((length, word))
word_set.sort(reverse=True) 
print(word_set)

number_string = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
numbers_extracted = re.findall(r'[-]?[\d]+', number_string)
print(numbers_extracted)
lowest = 0
biggest = 0
numbers_extracted = list(map(int, numbers_extracted))
for num in numbers_extracted:
    if lowest > num:
        lowest = num
    if biggest < num:
        biggest = num
print(lowest, biggest)
print('Biggest difference is: ' + str(biggest - lowest))

def is_valid_variable(string_name):
    if len(string_name) < 1:
        return False
    start_index = re.search(r'[a-z_]', string_name, re.I)
    if (start_index == None) or (start_index.span()[0] != 0):
        return False
    invalid_character = re.search(r'[^A-Za-z0-9_]', string_name, re.I)
    if invalid_character != None:
        return False
    return True

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(string_to_clean):
    string_to_clean = re.sub(r'[%|@|&|#|$|;]', '', string_to_clean)
    return string_to_clean
def most_frequent_words(string_to_check):
    ans_set = []
    cleanup = ['.', '!', '?', ',']
    string_to_check = string_to_check.split(' ')
    for word in string_to_check:
        for letter in word:
            if letter in cleanup:
                word = word.replace(letter, '')
        flag = False
        for existing_word in ans_set:
            if word in existing_word:
                flag = True
                break
        if not flag:
            length = 0
            for current_word in string_to_check:
                if word == current_word:
                    length += 1
            ans_set.append((length, word))
    ans_set.sort(reverse=True) 
    ans_set = ans_set[0: 3]
    return ans_set

cleaned_text = clean_text(sentence)
print(cleaned_text)
print() 
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]