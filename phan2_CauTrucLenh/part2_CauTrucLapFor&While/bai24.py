#UocSo(12) = {1; 2; 3; 4; 6; 12}
#UocSo(15) = {1; 3; 5; 15}
#BoiSo(12) = {12; 24; 36; 48; 60;...}
#BoiSo(15) = {15; 30; 45; 60;...}
#---</>---
# Ước số chung lớn nhất của 12 và 15 là: 3
# Bội số chung nhỏ nhất của 12 và 15 là: 60

a=int(input("Nhap so thu nhat: "))
b=int(input("Nhap so thu hai: "))

def uocLonNhat(a, b):
    while b:
        a, b = b, a% b
    return a

def boiNhoNhat(a, b):
    return a*b // uocLonNhat(a,b)

print(f"Uoc so chung lon nhat cua {a} va {b}:", uocLonNhat(a,b))
print(f"Boi so nho nhat cua {a} va {b}:", boiNhoNhat(a,b))