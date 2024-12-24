tongTien=0
while True:
    print("Nhấn 1 là nạp tiền")
    print("Nhấn 2 là rút tiền")
    print("Nhấn 0 là thoát")
    choice=int(input("-> HÃY NHẬP ĐỂ CHỌN: "))
    try:
        match choice:
            case 1:
                #nạp tiền
                tienNap=int(input("-> Nhập số tiền cần nạp: "))
                #kiểm tra tiền không phải số âm
                if tienNap<0:
                    print("Số tiền nạp không hợp lệ")
                #ngược lại tiền không âm tongTien+=tienNap
                else:
                    tongTien+=tienNap
                    print("Số tiền hiện tại là: ",tongTien)
            case 2:
                #rút tiền
                tienRut=int(input("-> Nhập số tiền cần rút: "))
                #kt tiền rút >0 và tongTien<tienRut
                if tienRut<0 or tongTien<tienRut:
                    print("Số tiền không đủ để rút")  
                    print("Số tiền hiện tại là: ",tongTien) 
                #ngược lại tongTien-=tienRut
                else:
                    tongTien-=tienRut
                    print("Số tiền hiện tại là: ",tongTien)
            case 0:
                #thoát chương trình
                break
    except ValueError:
        print("Phải nhập số")
