gioBatDau=int(input("Nhap gio bat dau: "))
gioKetThuc=int(input("Nhap gio ket thuc: "))

if 6<= gioBatDau < gioKetThuc <=21:
    giaTruoc17= 2500
    giaSau17= 3000

    if gioKetThuc <= 17:
        gioTruoc17= gioKetThuc - gioBatDau
        gioSau17=0
    elif gioBatDau > 17:
        gioTruoc17= 0
        gioSau17= gioKetThuc - gioBatDau
    else:
        gioTruoc17= 17- gioBatDau
        gioSau17= gioKetThuc - 17
    
    tongTien= gioTruoc17*giaTruoc17 + gioSau17*giaSau17
    print(f"Tong chi phi thue tu {gioBatDau} den {gioKetThuc} la: {tongTien}")
else:
    print("Khong hop le")
