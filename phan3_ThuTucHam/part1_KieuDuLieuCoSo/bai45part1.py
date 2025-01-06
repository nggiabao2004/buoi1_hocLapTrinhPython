n=int(input("Nhap ban kinh: "))
Pi=3.14

def chuVi(num):
    return 2*num*Pi
def dienTich(num):
    return num*num*Pi

if n<=0:
    print("Nhap lai ban kinh lon hon 0")
else:
    print("Chu vi hinh tron:",chuVi(n))
    print("Dien tich hinh tron:",dienTich(n))