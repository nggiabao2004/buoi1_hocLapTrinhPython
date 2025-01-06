#n = 7 => Các số nguyên tố nhỏ hơn 7 là 2, 3, 5

n=int(input("Nhap so nguyen to: "))

#Kiem tra so nguyen to
def soNguyenTo(num):
    if num<2:
        return False
    for i in range (2, int(num**0.5)+1):
    # int(num**0.5) nghia la: 'can bac 2 cua num'= num^(1/2)
    # hoac co the dung: for i in range (2, num-1):
        if num%i==0:
            return False
    return True

#Liet ke cac so nguyen to
def listSoNguyenTo(num):
    listNumber=[]
    testing=2
    while len(listNumber) < num:
        if soNguyenTo(testing):
            listNumber.append(testing)
        testing+=1
    return listNumber

if n<=0:
    print('Nhap lai so nguyen to lon hon 0')
else:
    print(f"{n} so nguyen to la: {listSoNguyenTo(n)}")