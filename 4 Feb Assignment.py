N = int(input("Enter a positive integer N: "))

for i in range(1, N): 
    print((10**i - 1) // 9 * i)