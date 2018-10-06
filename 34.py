#34 陶陶摘苹果
nlist = []
k = 0
for i in range(10):
    n = int(input("苹果到地面距离:"))
    nlist.append(n)
m = int(input("陶陶最大高度:"))
for j in range(10):
    if nlist[j] <= m + 30 :
        k += 1
print("可摘",k,"个")

