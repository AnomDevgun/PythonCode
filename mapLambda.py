def squared(num):
    return num**2


mynums= [1,2,3,4,5]

print(list(map(squared,mynums)))

# Map returns a list.

def checkeven(num):
    return num%2==0

print(list(filter(checkeven,mynums)))

#Filter function returns only the arguments that eval to True.

#LAMBDA FUNCTION

square = lambda num: num**2

print(square(3))

#example
print(list(map(lambda nums:nums%2==0,mynums)))
print(list(filter(lambda nums:nums%2==0,mynums)))

#reverse strings using lambda functions
names = ['Sally','Annie','Johnboy','Darth']
print(list(map(lambda name:name[::-1],names)))