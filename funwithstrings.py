#GLOSSARY OF THIS FILE
# Declare a string as a variable a
# Print the string and make use of a single quote somewhere in the string to learn to deal with such cases
# Print the length of the string
# Perform various slicing operations on the string and print the result of the various operations




a = 'himalayas'
print(a)

a = 'himalaya\'s'
print(a)

print(len(a))

mystring = "Hello World"

#grab one char
print(mystring[0])

#grab a slice
print(mystring[0:7])

#grab a slice with alternate step size
print(mystring[0::2])

#use negative indexes to approach the string backwards
print(mystring[-1])

#reverse the string using negative step size
print(mystring[::-1])
print(mystring[:len(mystring)])

#multiplication with letters
let = 'y'
print(let*11)

#concatenate
print('Hello'+'\tUni')

#convert to upper and lowe using string functions
print(mystring.upper())
print(mystring.lower())

#string split
astr = "String Splitter :("
print(astr.split())


## PRINT FORMATTING OR STRING INTERPOLATION ##
# .format() method


print("Hello from {}".format("a String INSERTED"))
print('The {2} {0} {1}'.format('brown','fox','quick'))

#using indices
print('The {2} {0} {0}'.format('brown','fox','quick'))

#using variables
print('The {q} {b} {f}'.format(b='brown',f='fox',q='quick'))

## Float Formatting "{value:width.precision f}"
result = 20/7
print("The result is {r}".format(r=result))
print("The result is {r:1.6f}".format(r=result))


# f-strings method (formatted string literals)
name = "Jake Peralta"

print(f'{name} is married to Amy Santiago')
print(f"The result is {result:1.6f}")

## NOTES ##
# Remember, Strings are immutable, i.e you cannot change its characters
# We cannot concatenate strings with integers or floats