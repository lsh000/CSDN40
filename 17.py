#17 输入年份以及月份，输出这个月有几天
a=int(input("year:"))
b=int(input("month:"))
if b in(1,3,5,7,8,10,12):
    print(31)
if b in(4,6,9,11):
    print(30)
if b==2:
    if a%100==0 and a%400==0:
        print(29)
    elif a%100!=0 and a%4==0:
        print(29)
    else:
        print(28)
 

