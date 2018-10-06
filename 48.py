x = int(input())
import math
a = math.exp(x)
b = math.exp(-x)
def sinh(x):
    return (a-b)/2

y = sinh(math.exp(sinh(x)))
print(y)