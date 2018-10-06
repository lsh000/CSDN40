#25
n = int(input("n:"))
for i in range(1,n+1):
    a = "*"*(2*i-1)
    b = a.center(2*n-1,' ')
    print(b)
for j in range(n-1,0,-1):
    a = "*"*(2*j-1)
    b = a.center(2*n-1,' ')
    print(b)