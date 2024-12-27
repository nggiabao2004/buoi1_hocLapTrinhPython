x=int(input("Nhap so km taxi chay duoc: "))
tongTien=0
if x<0:
    print("vui long nhap lai")
else:
    if x==1:
        tongTien=16
    else:
        if 1<x<=30:
            tongTien= 16+(x-1)*15
        else:
            tongTien= 16+29*15+(x-30)*12