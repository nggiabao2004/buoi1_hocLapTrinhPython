#n!=n×(n−1)×(n−2)×…×1
#5!=5×4×3×2×1=120

n=int(input("Nhap so nguyen: "))
kq=1

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1,n+1):
        kq=kq*i
        i+=1
print("Ket Qua:",kq)