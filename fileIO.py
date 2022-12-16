myfile = open('text.txt')
print(myfile.read())
myfile.seek(0) #reset cursor to beginning of file.
fileLines = myfile.readlines()
print(fileLines)
myfile.close()


#Another way to read:
with open('text.txt',mode='r+') as newFile:
    print(newFile.readline())
    newFile.write('\nHello World')
newFile.close()