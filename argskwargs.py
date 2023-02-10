def funcsum(*args):
    print(args)
    return sum(args) *0.1



def myfunc(**kwargs):
    print(kwargs)
    if('fruit' in kwargs):
        print(f"my fruit of choice is : {kwargs['fruit']}")
    else:
        print('I did not find any fruit.')

def comb(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[1]} {kwargs['food']}")

fsum = funcsum(10,10,5)
print(fsum)
myfunc(fruite='apple',fruits='banana')
comb(6,12,18,food='eggs',fruit='apple')

#*Args returns a tuple
#**Kwargs returns dictionary