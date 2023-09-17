def main():
    it = primeGenerator(10)
    for e in it:
        print(e, end=" ")    

def isPrime(num):
    if num < 2:  # 0 and 1 are not primes
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True 

def primeGenerator(n):
    num = 2
    while n:
        if isPrime(num):
            yield num
            n = n - 1
        num = num + 1
    return     

main()
