while True:
    try:
        x=int(input("enter the  x"))
    except ValueError:
        print("X IS NOT INTEGER")   
    else:
        break
print(f"x is {x}")     