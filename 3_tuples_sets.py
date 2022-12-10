# A tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members. 
fruits = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))

fruits2 = ('Apples',)
# A comma is what makes a tuple a tuple

# Get value
print(fruits[1])

# print(fruits2,type(fruits2))

# A set is a collection which is unordered and unindexed. No duplicate members. 

# Create set
fruits_set = {'apples', 'oranges', 'mangos'}
print('apples' in fruits_set)

fruits_set.add('Grape')
print(fruits_set)