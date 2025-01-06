# giai thừa: n!=n*(n-1)*(n-2)*...*1

n=int(input("Nhap n: "))
if (n<=0):
    print("Nhap lai n>0")
else:
    gt=1
    for i in range(1,n+1):
        gt*=i
        #tính gia thừa từ 1 đến n
    print('gt=',gt)