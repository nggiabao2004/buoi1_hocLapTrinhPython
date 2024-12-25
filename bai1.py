# Nhập thông tin sinh viên
hoTen = input("Họ tên: ")
maSinhVien = input("Mã số sinh viên: ")
lop = input("Lớp: ")
soDienThoai = input("Số điện thoại: ")
gioiTinh = input("Giới tính: ")

# Xuất thông tin sinh viên
print("\nThông tin sinh viên:")
if hoTen != "":
    print(f"Họ tên: {hoTen}")

if len(maSinhVien) == 8:
    print(f"Mã số sinh viên: {maSinhVien}")

if len(lop) == 6:
    print(f"Lớp: {lop}")

if len(soDienThoai) == 10:
    print(f"Số điện thoại: {soDienThoai}")

match gioiTinh:
    case "Nam":
        print(f"Giới tính: {gioiTinh}")
    case "Nu":
        print(f"Giới tính: {gioiTinh}")
