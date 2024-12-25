import math

a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
c=int(input("Nhap c: "))

x=0
delta=b*b-4*a*c
if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x=-c/b
        print("Phuong trinh co nghiem x= ",x)
else:
    if delta>0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem: x1=",x1,", va x2=",x2)
    else:
        if delta<0:
            print("Phuong trinh vo nghiem")
        else:
            x=-b/(2*a)
            print("Phuong trinh co nghiem kep: x1=x2=",x)