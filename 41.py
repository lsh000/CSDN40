#41 归并排序
def f(x):
    if len(x) <= 1:
        return x
    m = int(len(x)/2)
    left = f(x[:m])
    right = f(x[m:])
    return g(left,right)
def g(left,right):
    r = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            r.append(left[i])
            i += 1
        else:
            r.append(right[j])
            j += 1
    r += left[i:]
    r += right[j:]
    return r

    