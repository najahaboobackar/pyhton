import random
n=random.randint(1,10)
print(n)
guess=0
while guess!=n:
    guess=int(input("enter the number"))
if guess<n:
    print("number is short")  
elif guess>n:
    print("number is greater")
else:
    print("lucky")          