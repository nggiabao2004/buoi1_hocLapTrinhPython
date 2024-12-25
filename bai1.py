from tokenize import String

program = 1
hoVaTen=String(input("Nhap ho va ten: "))
maSoSinhVien=int(input("Nhap ma so sinh vien: "))
lop=int(input("Nhap lop: "))
soDienThoai=String(input("Nhap so dien thoai: "))
gioiTinh=String(input("Nhap gioi tinh: ")) 

if (hoVaTen == ""):
    print("Ho va ten khong duoc de trong")
else:
    print("Ho va ten: ", hoVaTen)

if (maSoSinhVien == ""):
    print("Ma so sinh vien khong duoc de trong")
elif 10000000 > maSoSinhVien or maSoSinhVien >= 100000000:
    print("Ma so sinh vien khong duoc nho hon 0")
else:
    print("Ma so sinh vien: ", maSoSinhVien)

if (lop == ""):
    print("Lop khong duoc de trong")
elif 100000 > lop or lop >= 1000000:
    print("Nhap lai lop")
else:
    print("Lop: ", lop)

if (soDienThoai == ""):
    print("So dien thoai khong duoc de trong")
elif len(soDienThoai)!=10:
    print("So dien thoai phai co 10 chu so")
else:
    print("So dien thoai: ", soDienThoai)

match gioiTinh:
    case "Nam":
        print("Gioi tinh: ", gioiTinh)
    case "Nu":
        print("Gioi tinh: ", gioiTinh)
    case _:
        print("Nhap lai gioi tinh")