# A list is a collection which is ordered and changeable. Allows duplicate members. 

# Create a list 
numbers = [1,2,3,4,5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# use a constructor, not necessary
numbers2 = list((1,2,3,4,5))
# print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get a length
print(len(fruits))

# Append to list 
fruits.append("mangos")

# Remove from a list
fruits.remove("Grapes")

# Inert into position
fruits.insert(2, "Strawberries")

# Remove with pop
fruits.pop(2)

# Reverse
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

# Change value
fruits[0] = "Blueberries"

print(fruits)