# A function is a block of code that runs when it is called
# We use indentation with tabs or spaces over curly brackets

# create a function

def sayHello(name="Sam"):
  print(f"Hello {name}")

sayHello('John Doe')

# Return values
def getSum(num1,num2):
  total = num1 + num2
  return total

# Two options
num = getSum(3,4)
print(num)

print(getSum(3,4))

# A lambda function is a small anonymous function
# A lambda function can take any number of args,
# But can only have one expression
getSum = lambda num1, num2 : num1 + num2

print(getSum)