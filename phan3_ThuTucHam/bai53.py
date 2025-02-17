import math


a= float(input("Nhap canh thu nhat: "))
b= float(input("Nhap canh thu hai: "))
c= float(input("Nhap canh thu ba: "))

if a+b>c and a+c>b and b+c>a:
    print("Day la tam giac")

    nuaChuVi= (a+b+c)/2
    dienTich= math.sqrt(nuaChuVi * (nuaChuVi-a) * (nuaChuVi-b) * (nuaChuVi-c))
    print("Dien tich tam giac la: ", dienTich)

    duongCaoA= (2*dienTich)/a
    print("Duong cao tu dinh doi dien canh a la: ", duongCaoA)
    duongCaoB= (2*dienTich)/b
    print("Duong cao tu dinh doi dien canh b la: ", duongCaoB)
    duongCaoC= (2*dienTich)/c
    print("Duong cao tu dinh doi dien canh c la: ", duongCaoC)
else:
    print("Khong phai la tam giac")
