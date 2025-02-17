def tongUocSo(x):
    tong=0
    for i in range(1, x+1):
        if x%i==0:
            tong+=i
    return tong

n=int(input("Nhap so nguyen duong: "))
if 0<n<100000:
    print(f"Tong uoc so la: {tongUocSo(n)}")
else:
    print("không hợp lệ")