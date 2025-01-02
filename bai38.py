n=int(input("Nhap so nguyen: "))
kq=0

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1,n+1):
        kq+= i/(i+1)
print("Ket Qua:",kq)