# Strings in python are surrounded by either single or double quotation marks
name = "Tim"
age = 31

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F strings is very handy! 
print(f"Hello my name is {name} and I am {age}")

# String methods 
s = "hello world"

# Capitalize
print(s.capitalize())

# Uppercase
print(s.upper())

# Lowecase
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
# print(s.replace('world, 'everyone'))

# starts with 
print(s.startswith('hello'))

# split into a list
print(s.split())