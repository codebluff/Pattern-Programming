n = ['A', 'B', 'C', 'D', 'E']

for i in range(len(n)+1, 0, -1):
    for j in range(0, i-1):
        print(n[j], end=" ")
    print()