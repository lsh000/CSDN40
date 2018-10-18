#P1059.Problem @数论（*筛法求素数）输出1…n的所有素数
n = int(input())
nlist = []
for i in range(1,n+1):
    nlist.append(i)
if n >= 2:
    for i in nlist[1:]:
        for j in nlist[1:]:
            x = i*j
            if x in nlist:
                del nlist[nlist.index(x)]
del nlist[0]
print(nlist)

