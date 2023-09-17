def main():
    print_square(3)
    print_s(5)


def print_square(size):
    for  i in range(size):
        for j in range(size):
            print("#", end="")
        print()    

def print_s(s):
    for  i in range(s):
        for j in range(s): 
            print("#"*s)     


main()            
        