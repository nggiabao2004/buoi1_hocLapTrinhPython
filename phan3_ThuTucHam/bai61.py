def kiemTraToanChan(n):
    for chuSo in str(n):
        if int(chuSo) % 2 != 0:
            return False
    return True

def kiemTraToanLe(n):
    for chuSo in str(n):
        if int(chuSo) % 2 == 0:
            return False
    return True

n = int(input("Nhap so nguyen duong n: "))

if 0 < n < 100000:
    if kiemTraToanChan(n):
        print(f"Cac chu so cua {n} toan la so chan.")
    elif kiemTraToanLe(n):
        print(f"Cac chu so cua {n} toan la so le.")
    else:
        print(f"Cac chu so cua {n} khong toan chan va khong toan le.")
else:
    print("Khong hop le")