
import heapq

n = int(input("Enter number of characters: "))

heap = []
for i in range(n):
    ch = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    heap.append((freq, ch))

heapq.heapify(heap)

while len(heap) > 1:
    f1, c1 = heapq.heappop(heap)
    f2, c2 = heapq.heappop(heap)

    heapq.heappush(heap, (f1 + f2, (c1, c2)))

def display(node, code=""):
    if isinstance(node, str):
        print(node, ":", code)
    else:
        display(node[0], code + "0")
        display(node[1], code + "1")

print("Huffman Codes:")
display(heap[0][1])


Enter number of characters: 3
Enter character: A
Enter frequency: 5
Enter character: B
Enter frequency: 2
Enter character: C
Enter frequency: 1
