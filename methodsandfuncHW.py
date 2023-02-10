import string

def vol(radius):
    return (4/3)*(3.14)*(radius**3)

def inrange(num,low,high):
    if(num in range(low,high+1)):
        return True
    return False

def checkcase(stringA):
    upp=0
    low=0
    for character in stringA:
        if(character.isupper()):
            upp+=1
        elif(character.islower()):
            low+=1
        else:
            pass
    print(f'The original string is: {stringA}')
    print(f'The number of lowercase char is {low}')
    print(f'The number of uppercase char is {upp}')

def unique(a):
    b=[]
    for eleA in a:
        if eleA in b:
            pass
        else:
            b.append(eleA)
    print(f'The original list is: {a}')
    print(f'The unique list is: {b}')

def mulList(a):
    num=1
    for number in a:
        num*=number
    print(f'Multiplying all numbers in {a} gives us {num}')

def palindrome(strA):
    strb=strA.replace(" ", "")
    if(strb==strb[::-1]):
        print(f'The string: {strA}, is a palindrome')
    else:
        print(f'The string: {strA}, is not a palindrome')

def panagram(strA):
    pan=list(string.ascii_lowercase)
    strA=strA.lower()
    for charA in strA:
        if(charA in pan):
            pan.remove(charA)
        else:
            pass
    if(len(pan)==0):
        print(f'The string: {strA}, is a panagram')
    else:
        print(f'The string: {strA}, is not a panagram')

print(vol(2))
# print(list(range(1,5)))
print(inrange(5,2,7))
checkcase('This IS a StRing!!')
unique([1,1,1,1,2,3,3,4,4,4,5,6,6,7,7,7,8,9,9])
mulList([1,2,3,-4])
palindrome('mom')
palindrome('neighbour')
palindrome('nurses run')
panagram('The quick brown fox jumps over the lazy dog')
panagram('Hello I am ava')