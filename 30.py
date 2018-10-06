#30 非递归辗转相除
a = int(input())
b = int(input())
c = max (a,b)
d = min (a,b)
while c%d != 0 :
    a = d
    d = c%d
    c = a
print (d)