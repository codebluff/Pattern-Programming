li = 5
for i in range(1, li + 1):
    for j in range(li, i - 1, -1):
        print(chr(j+64), end=" ")
    print()
