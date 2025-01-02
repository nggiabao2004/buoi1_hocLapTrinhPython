n=int(input("Nhap so nguyen: "))
kq=0
sum=0
mul=1

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1,n+1):
        sum+=i
        mul=mul*i 
        kq+=sum/mul
print("Ket Qua:",kq)