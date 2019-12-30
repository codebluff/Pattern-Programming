n = ['A', 'B', 'C', 'D', 'E']

for i in range(1, len(n)+1):
    for j in range(len(n), i-1, -1):
        print(n[i-1], end=" ")
    print()