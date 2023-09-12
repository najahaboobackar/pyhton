def main():
    number =get_number()
    mew(number)

def get_number():
    while True:
        n=int(input("enter the number"))
        if n>0:
                break 
    return n   

def mew(n):
    
    for _ in range(n):
        print("neow")

main()        