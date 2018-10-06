#26 2/1,3/2,5/3,8/5,13/8,21/13,……求此数列的前n项和
n = int(input("n:"))
a,b,i,x= 2,1,1,0
while i <= n :
    s = a/b
    a,b = a+b,a
    i += 1
    x += s
print(x)