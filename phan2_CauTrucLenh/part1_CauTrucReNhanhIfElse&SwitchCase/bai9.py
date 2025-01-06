a=int(input("Nhap a: "))
b=int(input("Nhap b: "))

x=0
if a!=0:
    x=-b/a
    print(x)
else:
    if b!=0:
        print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh vo so nghiem")