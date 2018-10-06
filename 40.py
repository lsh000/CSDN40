#40 输入n,m，分别输入n个，m个排好序的数，将这2个数列合并，并保持从小到大的顺序输出
n = int(input("n:"))
m = int(input("m:"))
nlist = []
mlist = []
for i in range(n):
    n = int(input())
    nlist.append(n)
for j in range(m):
    m = int(input())
    mlist.append(m)
nlist.extend(mlist)
nlist.sort()
print(nlist)