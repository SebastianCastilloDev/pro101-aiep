
a = 2
b = 90
c = 45

if a > b:
    if a > c:
        if b > c:
            print(a, b, c)
        else:
            print(a, c, b)
    else:
        print(c, a, b)
else:
    if b > c:
        if a > c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        print(c, b, a)
