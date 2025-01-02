x=int(input("Nhap so X: "))
y=int(input("Nhap mu Y: "))

#x^y = x*x*... (y lan)
kq=1
if x<0 & y<0:
    print("Nhap lai hai so nguyen")
else:
    for i in range (1,y+1):
        kq*=x
print("Ket qua:", kq)