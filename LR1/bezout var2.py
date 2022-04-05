def bezout(a, b, x, y):
    if a == 0:
        x = 0
        y = 1;
        return b
    x1 = 0
    y1 = 0
    d = bezout (b % a, a, x1, y1)
    x =  y1 - (b / a) * x1
    y = x1
    return d

x = 0
y = 0

print(bezout(15, 12, x, y), x, y)
