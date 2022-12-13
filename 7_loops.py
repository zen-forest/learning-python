# A loop is used for repeating a chunk of code - typically iterating over a sequence 
# That is either a a list, a tuple, a dictionary, a set, or string

people = ['Colin', 'Andi', 'Tim', 'Phil', 'Robbie']

# Simple for loop
# for person in people:
#   print(f'current person: {person}')

# Break
# for person in people: 
#   if person == 'Phil':
#     break
#   print(f'current person: {person}')

# Continue
# for person in people: 
#   if person == 'Phil':
#     break
#   print(f'current person: {person}')

# # range 
# for i in range(len(people)):
#   print(people[i])

# for i in range(0,12):
#   print(f'Number: {i}')

count = 0
while count <= 10:
  print(f'Count: {count}')
  count += 1