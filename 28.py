#28 输出所有的水仙花数。水仙花数是它本身恰好等于他各个位数上的立方和的三位数
for a in range(100,1000): 
    x = int((str(a)[0]))
    y = int((str(a)[1]))
    z = int((str(a)[2]))
    b =x**3 + y**3 + z**3
    if b == a :
        print(b)


