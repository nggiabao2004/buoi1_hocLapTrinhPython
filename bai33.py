n=int(input("Nhap so nguyen: "))
kq=1

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1,n+1):
        if i%2!=0:
            kq=kq*i
print("Ket Qua:",kq)