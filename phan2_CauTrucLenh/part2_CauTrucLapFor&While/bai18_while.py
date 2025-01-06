#UocSo(12) = {1; 2; 3; 4; 6; 12}
n=int(input("Nhap so nguyen: "))

if n<=0:
    print("Nhap so nguyen lon hon 0")
else:
    i=1
    while(i<=n):
        if n%i==0:
            print(i)
            i+=1
        else:
            i+=1