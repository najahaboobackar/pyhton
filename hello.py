#ask user for thier name
name=input("what is your name")
#remove white space from string
name=name.strip()
#capitalize the string
name=name.capitalize()
#capitalize the first letter of the word
name=name.title()
#we can also remove white space as weell as capitalize
name1=name.strip().title()
#in single line both stripping whitespcae and capitalizing
string=input("any string").strip().title()
#split usersname 
first,last=name.split(" ")
print(f"hello,{first}")
#say hello to users
print(name1, string)
print("hello, World" +name)
print("hello ,",end="")
print(name)
print("hello ,",name,sep="@@")
print("hello,\"friend\"")
print(f"name:{name}")
