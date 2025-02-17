def demChanLe(n):
    soChan=0
    soLe=0

    for chuSo in str(n):
        if int(chuSo) % 2 == 0:
            soChan += 1
        else:
            soLe +=1
    return soChan, soLe

n= int(input("Nhap so nguyen duong n: "))

if 0<n<100000:
    soChan, soLe= demChanLe(n)
    print(f"So {n} co {soChan} chu so chan, va co {soLe} chu so le")
else:
    print("Khong hop le")