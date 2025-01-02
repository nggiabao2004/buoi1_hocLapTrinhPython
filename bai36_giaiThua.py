#n!=n×(n−1)×(n−2)×…×1
#5!=5×4×3×2×1=120

n=int(input("Nhap so nguyen: "))
kq=0
mul=1

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1,n+1):
        mul=mul*i
        kq+=mul        
print("Ket Qua:",kq)