"""

E E E E E
  D D D D
    C C C
      B B
        A

"""

n = 5

for i in range(n-1, 0, -1):
    for j in range(n-1, 0, -1):
        print(chr(i+64), end=" ")
    for k in range(i):
        print(" ", end="")
