x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))

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
