#23 Sn=a+aa+aaa+aaaa+aaa…..a(n个)，a,n输入的数a,n∈N*且a∈[0,9],n∈[2,9]
a = int(input("a:"))
n = int(input("n:"))
x,y,i = 0,0,0
while i!=n:
    s = a*10**i
    i+=1
    x+=s
    y+=x
    if i==n:
        print(y)