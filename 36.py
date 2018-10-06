#36 输入n，输入n个数，输出其中最大的数以及最大数的序号
n = int(input("n:"))
i,z = 1,0
xlist = []
for i in range(n):
    x = input()
    xlist.append(x)
y = max(xlist)
a = xlist.index(y)
print(y," ",a+1)