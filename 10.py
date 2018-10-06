a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if (b**2-a*c*4) < 0:
    print("No solution")
else:
    x1 = -b + (b**2-a*c*4)**0.5
    x2 = -b - (b**2-a*c*4)**0.5
    print(x1,x2)