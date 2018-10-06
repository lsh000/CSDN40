#2 输入立方体的长宽高，求出它的体积表面积
a=int(input("长: "))
b=int(input("宽: "))
c=int(input("高: "))
x = a*b*c
y = a*b*2+a*c*2+b*c*2
print("体积",x)
print("表面积",y)
