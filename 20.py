#20 输入n（0<n<10），求使1/1+1/2+1/3.....+1/k>n成立的最小正整数k
n = int(input("n:"))
k = 1
s = 1
while s != n :
    k+=1
    s = s + 1/k
    if s > n :
        print(k)
        break