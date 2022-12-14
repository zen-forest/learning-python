# A class is like a blueprint for creating objects.
# An object has properties and methods 

# create class
class User: 
  # constructor 
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f"My name is {self.name} and I am {self.age}"

  def has_birthday(self):
    self.age += 1

# how to extend a class 
class Customer(User):
  # constructor 
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0
  
  def set_balance(self, balance):
    self.balance = balance 
  
  def greeting(self):
    return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"

# init user object 
tim = User("Tim Collins", "tim@test.com", 31)

# init customer object
ben = Customer("Ben Max", "bmr@test.com", 34)
ben.set_balance(500)

print(type(tim))
print(tim.name)
tim.has_birthday()
print(tim.greeting())

print(ben.greeting())