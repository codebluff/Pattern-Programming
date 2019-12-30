list1 = ['A', 'B', 'C', 'D', 'E']

for i in range(len(list1)-1, -1, -1):
    for j in range(len(list1)-1, -1, -1):
        print(list1[j], end=" ")
    print()