n = int(input())
list1 = input().split(" ")

list1 = [int(list1[i]) for i in range(len(list1))]

listsum = 0
for i in range(len(list1)):
    listsum += list1[i]

mean = listsum / len(list1)

print(mean)
#calculate median

list1.sort()

mid = len(list1)/2
