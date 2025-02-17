def laSoNguyenTo(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def demSoNguyenTo(x):
    soNguyenTo=0
    for i in range(x + 1):
        if laSoNguyenTo(i):
            soNguyenTo+=1
    return soNguyenTo

n= int(input("Nhap so nguyen duong n: "))
if 0<n<100000:    
    print(f"Co {demSoNguyenTo(n)} so nguyen to")
else:
    print("Khong hop le")