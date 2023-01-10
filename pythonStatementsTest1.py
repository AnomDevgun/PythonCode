#1
st = 'Print only the words that start with s in this sentence'
listst = st.split()
for word in listst:
    if 's' in word:
        print(word)

#2
print([x for x in range(0,10)])

#3
print([x for x in range(1,51) if x%3==0])

#4
st2 = 'Print every word in this sentence that has an even number of letters'
print([word for word in st2.split() if len(word)%2==0])

#5 : Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
    if(x%3==0 and x%5==0):
        print("FizzBuzz")
    elif(x%3==0):
        print("Fizz")
    elif(x%5==0):
        print("Buzz")
    else:
        print(x)

#6
st3 = 'Create a list of the first letters of every word in this string'
print([let[0] for let in st3.split()])

#instead of the long form
blist = []
for word in st3.split():
    blist.append(word[0])
print(blist)