# A module is basically a file containing 
# a set of functions to include in your application
# there are core python modules, modules you can install using the pip package manager
# (including Django) as well as custom modules

# core modules
import datetime
from datetime import date
from time import time 

# pip module
from camelcase import CamelCase

# local module 
import validator 
from validator import validate_email

today = datetime.date.today()
timestamp = time()

# Alternatively you can pull in the object directly 
today2 = date.today()

print(timestamp)

c = CamelCase()
print(c.hump('hello there world'))

email = "tim@test.com"

if validate_email(email):
  print("email is valid")
else:
  print("email is bad")

# Using PIP
# 1. when running PIP you install it globally
# 2. 'pip freeze' will show you everything installed globally
# 3. you can create a virtual environment to install it just there
# 4. pip env for instance 
# 