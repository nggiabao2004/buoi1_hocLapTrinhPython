#UocSo(12) = {1; 2; 3; 4; 6; 12}
n=int(input("Nhap so nguyen: "))
x=0
if x<0:
    print("Nhap so lon hon 0")
else:
    for i in range(1, n+1):
        if n%i==0:
            x+=1
print(x)