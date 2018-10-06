#19 输入一个数n，n∈N*，判断n是素数还是合数
n = int(input("n:"))
if n == 1 or n == 0:
    print(n,"既不是素数也不是合数")
else:
    for i in range(2,n):
        if n % i == 0:
            a = False   
            break
        else:
            a = True
if a == True:
    print("yes")
else:
    print("no")
            