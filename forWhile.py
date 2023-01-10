#For loops and while loops in python

from random import shuffle
from random import randint

a = 10
for i in range(a+1):
    if(i%2==0):print(i)
li = ['this','is','a','list']
for word in li:
    print(word)
for _ in 'Hello World':
    print('Cool cool cool!')

#Tuple unpacking
tu = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in tu:
    print(a+b)
for (a) in tu:
    print(a)

di = {'k1':100,'k2':101,'k3':102}
for key in di:
    print(key)
for val in di.values():
    print(val)
for key,value in di.items():
    print('key '+key+':'+str(value))


#WHILE loops
wA = 10
while wA>=0:
    print(f'Countdown!:{wA}')
    wA-=1
print(wA)
#break : breaks out of current enclosing loop
#continue : goes to the top of the nearest enclosing loop
#pass: does nothing at all

x = [1,2,3]
for i in x:
    pass
print('Loop iterated with pass')
string = 'Sammy'
for letter in string:
    if letter=='a':
        continue
    print(letter)

for letter in string:
    if letter=='a':
        break
    print(letter)

count = 0
for letter in 'abcde':
    print(f"The letter {letter} is at index {count}")
    count+=1
word = 'hello'
for let in enumerate(word):
    print(let)
for ind,letr in enumerate(word):
    print(f"The letter {letr} is at index {ind}")
myL1 = [1,2,3]
myL2 = ['a','b','c']

for item in zip(myL1,myL2):
    print(item)
#in keyword
print('a' in 'hello world')

#Shuffle from random library, returns none and is a inplace function
myL3 = [1,2,3,4,5,6,7,8,9]
shuffle(myL3)
print(myL3)

#Randint
print(randint(0,100))

#Inputting always accepts input as a string by default unless typecast
#a = int(input('Enter a number: '))
#print(f"You have entered {a}")


#LIST COMPREHENSION
stra = "hello world"
letList = [letter for letter in stra]
print(letList)

print([num**2 for num in range(0,11)])
print([num**2 for num in range(0,11) if num%2==0])

celcius = [0,32.4,670,1000]

print([((9/5)*temp+32) for temp in celcius])

#Using ifelse in list comprehension
print(["EVEN" if x%2==0 else "ODD" for x in range(0,11)])

#Nested for loop in list comprehension

print([x*y for x in [1,2,3] for y in [4,5,6]])