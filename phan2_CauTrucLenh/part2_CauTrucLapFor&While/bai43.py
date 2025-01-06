n=int(input("Nhap so nguyen: "))

kq=0
sum=0
if n<0:
    print("Nhap lai so nguyen")
else:
    for i in range (1,n+1):
        sum+=i
        kq+=sum
print("Ket qua:", kq)