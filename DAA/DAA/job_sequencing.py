
n = int(input("Enter number of jobs: "))

jobs = []
for i in range(n):
    p = int(input("Enter profit: "))
    d = int(input("Enter deadline: "))
    jobs.append((p, d, i + 1))

jobs.sort(reverse=True)

slots = [0] * n
total = 0

for p, d, job in jobs:
    for j in range(min(d, n) - 1, -1, -1):
        if slots[j] == 0:
            slots[j] = job
            total += p
            break

print("Selected Jobs:", [x for x in slots if x != 0])
print("Maximum Profit:", total)


Enter number of jobs: 4
Enter profit: 20
Enter deadline: 2
Enter profit: 15
Enter deadline: 2
Enter profit: 10
Enter deadline: 1
Enter profit: 5
Enter deadline: 3
