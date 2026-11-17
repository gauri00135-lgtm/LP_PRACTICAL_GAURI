
n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    profit.append(int(input("Enter profit: ")))
    weight.append(int(input("Enter weight: ")))

capacity = int(input("Enter knapsack capacity: "))

ratio = [profit[i] / weight[i] for i in range(n)]
items = sorted(range(n), key=lambda i: ratio[i], reverse=True)

total = 0

for i in items:
    if weight[i] <= capacity:
        total += profit[i]
        capacity -= weight[i]
    else:
        total += ratio[i] * capacity
        break

print("Maximum Profit:", total)


Enter number of items: 3
Enter profit: 60
Enter weight: 10
Enter profit: 100
Enter weight: 20
Enter profit: 120
Enter weight: 30
Enter knapsack capacity: 50
