def soSanh(Str1, Str2):
    if len(Str1) > len(Str2):
        print(Str1)
    elif len(Str1) < len(Str2):
        print(Str2)
    else:
        print(Str1,"</>",Str2)

String1=input("Nhap chuoi thu nhat: ")
String2=input("Nhap chuoi thu hai: ")
soSanh(String1, String2)