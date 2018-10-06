#31 输出斐波拉契数列前n项
n = int(input("n:"))
i,a,b = 1,0,1
while i <= n :
    print(a)
    a,b = b,a+b
    i += 1