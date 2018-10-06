#42 输入n，输入n个数，存入数组后，将数组内的数交换为倒序存储
n = int(input("n:"))
nlist = []
for i in range(n):
    n = int(input())
    nlist.append(n)
nlist.reverse()
print(nlist)

