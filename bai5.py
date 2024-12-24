n=int(input("Nhap n: "))
if n<10 or n>99:
    #phải đáp ứng điều kiện if đúng mới thực thi mệnh lệnh if
    print("Nhap so co 2 chu so") 
else:
    a=n//10
    b=n%10
    c=a+b
    print('tong:', c)