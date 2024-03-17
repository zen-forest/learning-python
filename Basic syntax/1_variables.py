"""
Variable Rules 
- Variable names are case sensitive
- must start with letter or underscore
- can have numbers but not start with one 
"""

# you don't need semicolons 
x = 1          # int
y = 2.5        # float 
name = "Tim"   # str
is_cool = True # bool

# Multiple assignments
x, y, name, is_cool = (1, 2.5, 'John', True)

#basic math
a = x + y

# casting 
x = str(x)
y = int(y)
z = float(y)

print('Hello')
print(x,y,name,is_cool, a)

# here's how to check a type
# print(type(z),z)
# returns <class 'float'> 2.0


