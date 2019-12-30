"""
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1

for i in range(6, 1, -1):
    for k in range(1, 6):
        print(" ", end="")
    for j in range(1, i):  # , 0, -1):
        print(i, end=" ")
    print()
"""
n = 10
for i in range(1, n):
    for j in range(1, i):
        print(j, end=" ")
    print()
    for k in range(n-1, i, -1):
        print("", end=" ")


