a=int(input("Nhap canh thu nhat: "))
b=int(input("Nhap canh thu hai: "))
c=int(input("Nhap canh thu ba: "))

if a>0 and b>0 and c>0:
    if a*a==(b*b+c*c) or b*b==(a*a+c*c) or c*c==(a*a+b*b):
        print("Day la tam giac vuong")
    elif a==b==c:
        print("Day la tam giac deu")
    elif a==b or a==c or b==c:
        print("Day la tam giac can")
    else:
        print("Day la tam giac thuong")
else:
    print("Vui long nhap lai 3 canh lon hon 0")