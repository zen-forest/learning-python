# Dictionaries is a collection which is unorderd, changeable, and indexed. 
# No duplicate members 

# Create dict
person = {
  "first_name": "John",
  "last_name": "Doe",
  "age": 31
}

# use constructor 
# person2 = dict(first_name="sara", last_name="Doe")

# Get value
print(person['first_name'])
print(person.get('first_name'))

# Add key/value
person['phone'] = "555-123-1234"
print(person)

# Get dict keys
print(person.keys())

# Get  dict items 
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = "Boston"

# Remove item 
person.pop("age")

# clear
person.clear()

# Get length
print(len(person2))

print(person)

# Like JSON you can have a list of dictionaries
people = [
  {'name':'Martha','age':30},
  {'name':'Steve','age':30}
]

print(people)
