gioVaoCa= int(input("Nhap gio vao ca: "))
gioRaCa= int(input("Nhap gio ra ca: "))

if 6<= gioVaoCa < gioRaCa <= 18:
    giaTruoc12= 6000
    giaSau12= 7500

    if gioRaCa <=12:
        gioTruoc12= gioRaCa - gioVaoCa
        gioSau12= 0
    elif gioRaCa > 12:
        gioTruoc12= 0
        gioSau12= gioRaCa - gioVaoCa
    else:
        gioTruoc12= 12- gioVaoCa
        gioSau12= gioRaCa - 12

    tienLuongNgay= gioTruoc12*giaTruoc12 + gioSau12*giaSau12
    print(f"Tong tien luong ngay tu {gioVaoCa} den {gioRaCa} la: {tienLuongNgay}")
else:
    print("Khong hop le")