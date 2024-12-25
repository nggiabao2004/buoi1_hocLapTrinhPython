# Nhập ba số
a = int(input("Nhập số thứ nhất a: "))
b = int(input("Nhập số thứ hai b: "))
c = int(input("Nhập số thứ ba c: "))

numbers = (a, b, c)

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
