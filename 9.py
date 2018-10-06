#9 输入成绩（分数）,输出等第，>90A,80-90B，70-80C，60-70D，<60E
a = int(input('输入分数:'))
if a > 90 :
    print('A')
elif a < 90 and a >= 80 :
    print('B')
elif a < 80 and a >= 70 :
    print('C')
elif a < 70 and a >= 60 :
    print('D')
else:
    print('E')