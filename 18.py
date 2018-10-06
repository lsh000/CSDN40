#18 输入成绩a及素质分b，若a,b都>=90，则输出great。若a,b有一个>=60，则输出so-so。否则，则输出bad
a=int(input("a: "))
b=int(input("b: "))
if a>=90 and b>=90:
    print("great")
elif 60<=a or b>=60:
    print("so-so")
else:
    print("bad")