#24 求1!+2!+3!+4!+……n!的值并输出
n = int(input("n:"))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))
s = 0
for i in range(1,n+1):
    s += factorial(i)
print(s)
