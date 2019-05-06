# 3.1.1. Numbers
2+2 # int
17/3 # classic division returns a float
17//3 # floor division that discards the fractional part
17%3 # the % operator returns the remainder of the division
5**2 # 5 squared

# 3.1.2. Strings
'spam eggs' # single quotes
'doesn\'t' # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.' # another example
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
print(s)  # with print(), \n produces a new line

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote
print("""\
Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
""")
3 * 'un' + 'ium' # 3 times 'un', followed by 'ium'
'Py' 'thon'

word = 'Python'
word[0] # character in position 0
word[-1]  # last character
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[:2] + word[2:]

# 3.1.3. Lists
squares = [1, 4, 9, 16, 25]
squares[0]
squares+[36, 49, 64, 81, 100]
squares[3] = 111 # Lists are mutable type unlike strings
cubes = [1, 8, 27, 65, 125]
cubes.append(216)  # add the cube of 6
cubes.append(7**3)
cubes
letters = ['a', 'b', 'c', 'd']
len(letters) #
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x

x[0]

x[0][1]