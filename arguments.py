# An argument is a value that you pass into a function or method when you call it. 
# Arguments are inputs, just like in Origami 
# Then return something based on that input 

# Types of arguments 
# 1. Positional arguments 
# 2. Keyword arguments 
# 3. Default arguments 
# 4. Variable-length arguments: 
# 5. Namedtuple: 

def example_function(pos1, pos2, kwags1=None, *args, **kwargs):
    print(pos1, pos2)
    print(pos1, pos2)
    print(pos1, pos2)
    print(pos1, pos2)

example_function(1,2, kwargs1="three", extra1=4, extra2=5)
