# If/else conditions are used to decide to do something
# Based on whether they are true or false 

x = 10
y = 10

# Comparison operators (==, !=, >,<,<=) used to compare values

# Simple if
if x > y:
  print(f'{x} is greater than {y}')

# If/else
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')
else:
  print(f'{y} is greater than {x}')


# You can also do nested if
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or not) - Used to combine conditional statements

# Both have to be true
if x > 2 and x <= 10:
  print(f"{x} is gerater than 2 and less than or equal to 10")

# Only one of these has to be true
if x > 2 or x <= 10:
  print(f"{x} is gerater than 2 and less than or equal to 10")

# not
if not(x == y):
  print("f{x} is not equal to {y}")

# Membership operators
# not, not in 
# used to test if a sequqnce is presented in an object
numbers = [1,2,3,4,5]

# in
if x in numbers:
  print(x in numbers)

# not in
if x not in numbers:
  print(x not in numbers)

# is 
if x is y: 
  print(x is y)

# is not 
if x is not y: 
  print(x is not y)