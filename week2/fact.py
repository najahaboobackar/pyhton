n = int(input("enter the number"))
for i in range(1, n+1):  # Start from 2
    if n % i == 0:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count = count + 1
        if count == 2:
            print(i)
