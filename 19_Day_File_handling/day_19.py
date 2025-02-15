# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f = open('./files/reading_file_example.txt')

# f = open('./files/reading_file_example.txt')
# txt = f.read()
# print(txt)
# txt = f.read(10)
# print(type(txt))
# line = f.readline()
# print(line)
# lines = f.readlines() or f.read().splitlines()
# readline includes special characters such as \n and splitlines doesn't
# print(lines)
# f.close()

