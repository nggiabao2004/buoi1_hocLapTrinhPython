import math

x=int(input("Nhap so chinh phuong: "))

if x<0:
    print("Vui long nhap lai so lon hon 0")
else:
    sqrtX=int(math.sqrt(x))
    if x== sqrtX* sqrtX:
        print(x,"la so chinh phuong")
    else:
        print(x,"khong phai la so chinh phuong")