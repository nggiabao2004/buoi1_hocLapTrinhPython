def maxUocSoLe(x):
    max=0
    for i in range(1, x+1):
        if x%i==0:
            if i%2==1:
                if max<i:
                    max=i
    return max

n=int(input("Nhap so nguyen duong: "))
if 0<n<100000:
    print(f"Uoc so le cua {n} la: {maxUocSoLe(n)}")
else:
    print("không hợp lệ")