#35 输入一个n*m的矩阵，求出各斜行的和。
n = int(input("n:"))
m = int(input("m:"))
xlist = []
for i in range(n):
    t = []
    xlist.append(t)
    for k in range(m):
        x = int(input())
        xlist[i].append(x)
for i in range(0,n):
    for d in range(i):
        xlist[i].append(0)
    for t in range(i+1,n):
        xlist[i].insert(0,0)

for i in range(m+n-1):
    s = 0
    for j in range(n):
        s += xlist[j][i]

    print(s)