n=int(input("Nhap so nguyen: "))

if n<=0:
    print("Nhap so lon hon 0")
else:
    i=1
    while(i<=n):
    #vong lap while phai nhap dieu kien dung thi moi thuc hien cau lenh  trong vong lap
        print(i, i*i)
        i+=1
    #chi khi dieu kien trong vong lap while sai thi moi thoat khoi vong lap    