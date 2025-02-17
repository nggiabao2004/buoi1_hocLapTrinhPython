n=int(input("Nhap so nguyen: "))

def soHoanHao(num):
    total=0
    if num<=0:
        return False
    else:
        for i in range (1,num):
            if num%i==0:
                total+=i
    if total==num:
        return True
    else:
        return False

def listSoHoanHao(num):
    listNumber=[]
    testing=0
    while testing < num:
        if soHoanHao(testing):
            listNumber.append(testing)
        testing += 1
    return listNumber

if n<=0:
    print("Nhap so lon hon 0")
else:
    print(f"Cac so hoan hao nho hon {n} la: {listSoHoanHao(n)}")