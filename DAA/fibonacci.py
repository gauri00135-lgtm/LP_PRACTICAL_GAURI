
n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    if i < n - 1:
        a, b = b, a + b
        count += 1

print("\nStep Count:", count)
