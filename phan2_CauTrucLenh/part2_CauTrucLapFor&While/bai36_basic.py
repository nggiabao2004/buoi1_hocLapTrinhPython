n=int(input("Nhap so nguyen: "))
kq=0
mul=1

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1,n+1):
        kq+= i*mul
        mul*=i
print("Ket Qua:",kq)