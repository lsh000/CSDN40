#33 输出三级斐波拉契数列前n项：
n = int(input("n:"))
a,b,c,i = 0,1,1,1
while i <= n :
    print(a)
    a,b,c = b,c,a+b+c
    i += 1