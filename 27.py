#27 用二分法求2x^3-4x^2+3x-6=0在（-10,10）的根
def f(x):
    return 2*x**3 - 4*x**2 + 3*x - 6


def g(a,b):
    while (b-a)/2 >= 0.01:
        m = (a+b)/2
        if f(m) * f(a) < 0:
            b = m
        else:
            a = m
    return m
k = g(-10,10)
print(k)

