#32 输入一个n*m的矩阵，求出各列的和
n = int(input("n:"))
m = int(input("m:"))
xlist = []
for i in range(n):
    for j in range(m):
        x = int(input())
        xlist.append(x)
for k in range(m):
    a = xlist[k::m]
    print(sum(a))



    
