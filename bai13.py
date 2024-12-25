h=int(input("Nhap gio:"))
m=int(input("Nhap phut:"))
s=int(input("Nhap giay:"))

if 0<=h<=23:
    if 0<=m<60:
        if 0<=s<60:
            print("Thoi gian hop le")
            print(h,":",m,":",s)
        else:
            print("Thoi gian khong hop le")
    else:
        print("Thoi gian khong hop le") 
else:
    print("Thoi gian khong hop le")      
