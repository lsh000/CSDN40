#8 输入一个年份，判断是不是闰年
a  = int(input())
if a % 100 == 0 :
    if a % 400 == 0:
        print("yes")
    else:
        print("no")
else:
    if a % 4 == 0 :
        print("yes")
    else :
        print("no")