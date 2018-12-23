myfile = open("fruits.txt")
content = myfile.read()
myfile.close()
content = content.splitlines()
for i in content:
    print(len(i)) 

mylist = [1,2,3]
newfile = open("feladat.txt", "w")
for key in mylist:
    newfile.write(str(key) + "\n")

newfile.close()


