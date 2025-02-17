def soNguyenTo(x):
    if x<2:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x%i==0:
                return False
        return True
    
def inSoNguyenTo(y):
    soDem=0
    soHienTai=2
    while soDem < y:
        if soNguyenTo(soHienTai):
            print(soHienTai)
            soDem+=1
        soHienTai+=1

n=int(input("Nhap so nguyen: "))
if n>0:
    inSoNguyenTo(n)
else:
    print("Khong hop le")