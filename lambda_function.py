f = lambda a, b: a + b
rel = f(1, 2)
print("rel = ", rel)


def myFunc(n):
    f = lambda a: a*n
    return f
f1 = myFunc(2)
rel = f1(5)
print("5*2 = ", rel)
