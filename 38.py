#38 输入n，输入n个排好序的数，在输入一个带插入的数，将这个数插入此序列中，并保持从小到大的顺序输出
n = int(input("n:"))
xlist = []
for i in range(n):
    x = int(input())
    xlist.append(x)
y = [int(input("插入的数："))]
xlist.extend(y)
xlist.sort()
print(xlist)
