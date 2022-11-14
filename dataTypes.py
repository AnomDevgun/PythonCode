#The following are the basic datatypes and data structures you will frequently encounter

# 1) integer (int): whole numbers like 3,40,30001, etc.
# 2) floating point (float): decimal point numbers like 3.1, 45.67, 4500.6754, etc.
# 3) strings (str): ordered sequence of characters like "samantha", "lukas", "d@arth5779", etc.
# 4) lists (list): an ordered sequence of objects (think a collection) like [10,"beautiful",898.04]
# 5) dictionaries (dict): unordered key:value pairs (in that specific format) like {"key1":34,"key2":"brother"}
# 6) tuples (tup): ordered immutable sequence of objects (similar to a list but elemts unchangeable once added) like (190,'dufresne',10.113)
# 7) sets (set): unordered collection of unique objects {'a','b'}
# 8) booleans (bool): logical value capable of 2 states, True or False.

a = 4
b = 56.4
c = "the mountain"
d = [10,"beautiful",898.04]
e = {"key1":34,"key2":"brother"}
f = (190,'dufresne',10.113)
g = {'a','b'}
h = True

print("The data type of \'"+str(a)+"\'"+" is "+type(a).__name__)
print("The data type of \'"+str(b)+"\'"+" is "+type(b).__name__)
print("The data type of \'"+str(c)+"\'"+" is "+type(c).__name__)
print("The data type of \'"+str(d)+"\'"+" is "+type(d).__name__)
print("The data type of \'"+str(e)+"\'"+" is "+type(e).__name__)
print("The data type of \'"+str(f)+"\'"+" is "+type(f).__name__)
print("The data type of \'"+str(g)+"\'"+" is "+type(g).__name__)
print("The data type of \'"+str(h)+"\'"+" is "+type(h).__name__)