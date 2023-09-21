def main():
    print_sq(2)


def print_sq(size):
    for  _ in range(size):
        print_rw(size)    

def print_rw(w):
    for _ in  range(w):
        print("#"*w)     


main()        
           
        