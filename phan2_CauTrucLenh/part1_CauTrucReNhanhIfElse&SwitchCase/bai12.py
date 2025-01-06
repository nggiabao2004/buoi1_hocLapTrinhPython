while True:
   a=int(input("Nhap so co 3 chu so: "))
   if 100<=a <999:
       break
   else:
       print("Khong hop le")

x=a//100
y=a//10%10
z=a%10
numbers = (x, y, z)

match numbers:
    case (x, y, z) if x <= y <= z:
        print(x, y, z)
    case (x, y, z) if x <= z <= y:
        print(x, z, y)
    case (x, y, z) if y <= x <= z:
        print(y, x, z)
    case (x, y, z) if y <= z <= x:
        print(y, z, x)
    case (x, y, z) if z <= x <= y:
        print(z, x, y)
    case (x, y, z) if z <= y <= x:
        print(z, y, x)
