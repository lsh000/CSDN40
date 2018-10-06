#37 选择排序
ylist = []
xlist = []
n = int(input("n:"))
for i in range(n):
    x = int(input())
    xlist.append(x)
for i in range(n):
    ylist.append(min(xlist))
    xlist.pop(xlist.index(min(xlist)))
print(ylist)

