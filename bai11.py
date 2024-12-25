
do=0
while True:
    a=int(input("Nhap so co 3 chu so: "))
    if 100<=a <999:
        break
    else:
        print("Nhap so co 3 chu so: ")

x=a//100
y=a//10%10
z=a%10
       
numbers = (x, y, z)

match numbers:
    case (x, y, z) if x >= y and x >= z:
        print("Chữ số lớn nhất ở hàng trăm:", x)
    case (x, y, z) if y >= x and y >= z:
        print("Chữ số lớn nhất ở hàng chục:", y)
    case (x, y, z) if z >= x and z >= y:
        print("Chữ số lớn nhất ở hàng đơn vị:", z)