#43 冒泡排序
def f(list):
    n = len(list)
    for i in range(n):
        for j in range(i+1,n):
            if list[i] >= list[j]:
                list[i],list[j] = list[j],list[i]
    return list

print(f(list))