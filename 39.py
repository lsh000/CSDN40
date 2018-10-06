#39 插入排序
n = int(input("n:"))
xlist = []
for i in range(n):
    x = int(input())
    xlist.append(x)
for i in range(n):
    a = xlist[i]
    j = i - 1
    while j >= 0 and a < xlist[j]:
        xlist[j + 1] = xlist[j]
        j -= 1
        xlist[j + 1] = a
print(xlist)

        

        