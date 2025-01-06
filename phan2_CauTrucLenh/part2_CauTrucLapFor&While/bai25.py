#UocSo(12) = {1; 2; 3; 4; 6; 12}
#6=s(6)=1+2+3
n=int(input("Nhap so nguyen: "))
total=0

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1, n):
        if n%i==0:
            total+=i
            i+=1
        else:
            i+=1
          
if total==n:
    print(n,"la so hoan thien")
else:
    print(n,"khong phai la so hoan thien")