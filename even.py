def main():
    x=int(input("enter the number"))
    if is_even(x):
     print("even")
    else:
        print("odd")
    
def is_even(n):
    return True if n%2==0 else False  

main()
