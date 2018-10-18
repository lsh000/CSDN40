a = float(input())
b = float(input())
c = float(input())
p = ((a+b+c)/2)
s = (p*(p-a)*(p-b)*(p-c))**0.5
c = 2*p
print("面积：%.5f"%s)
print("周长：%d"%c)