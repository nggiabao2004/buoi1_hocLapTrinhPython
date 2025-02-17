n=int(input("Nhap so nguyen co 3 chu so: "))

def docSo(num):
    #Bang chu so tieng viet
    chuSo=["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
    
    ketQua= " "
    tram=num//100
    chuc=num//10%10
    donVi=num%10

    #Doc cac chu so
    if tram > 0:
        ketQua += chuSo[tram] + " tram"

    if chuc > 1:
        ketQua += " " + chuSo[chuc] + " muoi"
        if donVi == 5:
            ketQua += " lam"
        elif donVi > 0:
            ketQua += " " + chuSo[donVi]
    elif chuc == 1:
        ketQua += " muoi"
        if donVi == 5:
            ketQua += " lam"
        elif donVi>0:
            ketQua += " " + chuSo[donVi]
    elif chuc == 0:
        if donVi > 0:
            ketQua += " " + chuSo[donVi]
        elif tram == 0:
            ketQua += chuSo[donVi]

    return ketQua.strip()

if 0>n or n>=1000:
    print("Nhap lai so nguyen co 3 chu so")
else:
    print(n,":",docSo(n))