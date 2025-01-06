a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
c=int(input("Nhap c: "))

if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)