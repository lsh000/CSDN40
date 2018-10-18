#输入一个日期，计算从2000.01.01到这一天要多少天
print("输入日期,例如：2000.01.02 :")
a = input()
year = int(a[:4])
month = int(a[5:7])
day = int(a[8:])
x = year - 2000
y = month - 1
z = day - 1
dic = {0:0,1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334}
if x != 0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        
        if y >= 1:
            r = x*(365)+(int(x/4))+dic[y]+z+1    
    else:
        r = x*(365)+(int(x/4))+dic[y]+z
else:
    if y >= 1:
        r=dic[y]+z+1
    else:
        r=dic[y]+z
print(r)
