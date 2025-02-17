n=int(input("Nhap 1 so: "))
def square(num):
    return num **2

if n<0:
    print("Nhap lai so nguyen");
else:
    print("Ket qua binh phuong cua",n,"la:",square(n))