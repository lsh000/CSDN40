#写一个求素数的函数。在主程序中调用这个函数，求出结果
def f(x)  :
    for i in range(2,x):
        if x%i == 0:
            return  False
            break
    return  True



x = int(input())
y = f(x)
if y == True:
    print("yes")
else :
    print("no")