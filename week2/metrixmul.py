n = int(input("Enter the matrix size: "))

# Initialize matrices
a = [[0 for _ in range(n)] for _ in range(n)]
b = [[0 for _ in range(n)] for _ in range(n)]

# Input elements for matrix 'a'
for i in range(n):
    for j in range(n):
        a[i][j] = int(input(f"Enter element for matrix A at position {i+1},{j+1}: "))

# Input elements for matrix 'b'
for i in range(n):
    for j in range(n):
        b[i][j] = int(input(f"Enter element for matrix B at position {i+1},{j+1}: "))

# Matrix multiplication
mul = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            mul[i][j] += a[i][k] * b[k][j]

# Print resulting matrix
for i in range(n):
    for j in range(n):
        print(mul[i][j], end=" ")
    print()  # move to next line
