#Functions allow us to create blocks of code that are easy to execute, debug and modify

#def keyword is used to define and create functions in python

#example: def name_of_function():

""" This is an example of a multiline comment typically used
to give information about the function"""

#ctrl+ k followed by ctrl+c will comment the selected lines

import random as rand

def hello_world(name):
    print(f"Hello {name} how are you today?")

def king(name):
    return (f'You are doing great, {name}, keep it up!')

def add_num(num1,num2):
    return num1+num2

def mostHours(workHours):
    currentMax=0
    best_employee=''
    for emp,hours in workHours:
        if(hours>currentMax):
            currentMax=hours
            best_employee=emp
        else:
            pass

    return(best_employee,currentMax)

def shuffleList(myList):
    rand.shuffle(myList)
    return myList

# name = input('Please enter your name: ')
# num1 = int(input('Please input number 1: '))
# num2 = int(input('Please input number 2: '))
# sum = add_num(num1,num2)
# op = king(name)

# hello_world(name)
# print(f"The sum of the two numbers entered is: {sum}")
# print(op)

# workHours = [('Abby',100),('Billy',400),('Cassie',800),('Alex',20),('Sinbad',4000)]
# print((f'Employee that worked the most hours: {mostHours(workHours)}'))

orglist = [1,2,3,4,5,6,7,8,9]
print(f"The original list is {orglist}, the shuffled list is {shuffleList(orglist)}")