def hoanVi(a, b):
    return b, a

a= int(input("Nhap so thu nhat: "))
b= int(input("Nhap so thu hai: "))

a, b= hoanVi(a, b)
print(f"Sau khi hoan vi: a= {a}, b= {b}")