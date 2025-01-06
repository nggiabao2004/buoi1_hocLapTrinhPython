# #So nguyen to la so "chi" co the chia het cho 1 va chinh no
    # Kiểm tra trực tiếp: Duyệt qua mỗi số từ 2 đến n-1 để xem có số nào chia hết cho số đang xét không.
        # Nếu không, số đó là số nguyên tố.
    # Phương pháp căn bậc hai: Chỉ kiểm tra chia hết cho các số từ 2 đến căn bậc hai của số đang xét.
        # Nếu không có số nào chia hết, đó là số nguyên tố.
    # Sàng Eratosthenes: Bắt đầu từ số 2, loại bỏ các bội số của mỗi số nguyên tố tìm được từ danh sách số cho đến n.

import math

n=int(input("Nhap so nguyen to: "))
x=0
if n<2:
    print('Nhap lai so nguyen to lon hon 2')
else:
    sqrtNum=int(math.sqrt(n))
    for i in range(2, sqrtNum+1):
        if n%i==0:
            x+=1

if x==0:
    print(n, "la so nguyen to")
else:
    print(n, "khong phai la so nguyen to")
