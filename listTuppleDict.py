# Working with lists

l_a = [1,2,3,4,'a',"aString",'a']
l_b = [51,6,799,80,1]
l_c = [1,2,[3,4,5]]
print('Original list A is: '+str(l_a))
print('Original list B is: '+str(l_b))
print('Original list C is: '+str(l_c))
print(len(l_a))
print(l_a[3:])
print('Index of the first occurance of the letter a in the list is: '+str(l_a.index('a')))
print('Concatenated lists are: '+str(l_a+l_b))
l_a[l_a.index('aString')] = 'bString'
print('After changing the list item list a is now:'+str(l_a))
l_a.append('appendedItem')
print('Appended item'+str(l_a))
l_a.pop()
print('After popping'+str(l_a))
l_b.reverse()
print('Reversed list is: '+str(l_b))
l_b.sort()
print('Sorted list is: '+str(l_b))
print('Grabbing inner list from nested list c and the first element of nest: '+str(l_c[2])+' ,element is: '+str(l_c[2][0]))



# Working with tuples is the same, except items cannot be changed once added to the tuple, they can not modified.
t_a = ("yourName",2,4.5,'f')
print('Original tuple A is: '+str(t_a))
print(type(t_a))
print(t_a.index(4.5))


#Dictionaries
#unordered and cannot be sorted, the keys can be of different types at once, like a mix of float and int

a_dict = {1:'my',2:'name',3:'is',4:'slim','lastkey':'shady',"listindict":['this','is','a','list','in','dict'],'key':{'inner':'innerDict'}}
keys = a_dict.keys()
print(keys)
print(a_dict['listindict'])
print(a_dict['key']['inner'])


#Set: unordered collection of unique elements
a_set = set((1,2,3,4,5,6))
print(a_set.pop())
print(a_set.pop())
