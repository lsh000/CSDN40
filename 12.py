#12
#y=x(x<1)
#y=2x-1(1<=x<=10)
#y=3x-11(x>10)
a = int(input())
if a<1:
    print(a)
elif 1<=a<=10:
    print(a*2-1)
else:
    print(a*3-11)