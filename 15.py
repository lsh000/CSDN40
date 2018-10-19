r = int(input("r:"))
h = int(input("h:"))
x = int(input("x:"))
y = int(input("y:"))
if (x**2 + y**2)**0.5 >= r:
    print("h:",0)
else:
    H = (h*((x**2 + y**2)**0.5))/r
    print("h:%.5f"%H)