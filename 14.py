#14 收电费，电费的单价，小于等于50kwh的部分0.5元，50-100 0.7，100以上1元每kwh,，输出电费总价
x = input("用电度数：")
a = int(x)
if a<=50:
    y = a*0.5
    print("电费：",y)
elif 50<a<=100:
        b = 50*0.5+(a-50)*0.7
        print("电费：",b)
else:
        d = 50*0.5+50*0.7+(a-100)*1
        print("电费：",d)
      