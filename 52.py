#写一个判断一个年份是不是闰年的函数
def f(x):
    if x%100 == 0:
        if x%400 == 0:
            return "yes"
        else:
            return "no"
    else:
        if x%4 == 0:
            return "yes"
        else:
            return "no"

x = int(input())
print(f(x))