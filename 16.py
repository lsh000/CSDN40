#16
#y=x-1(x<1或者x>10)
#y=x+2(1<=x<=10)
a=float(input())
if a<1 or a>10:
    y=a-1
    print(y)
else:
    y=a+2
    print(y)