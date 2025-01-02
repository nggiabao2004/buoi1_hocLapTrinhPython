n=int(input("Nhap so nguyen: "))
total=0

if n<=0:
    print("Nhap so lon hon 0")
else:
    for i in range (1,n+1):
        if i%2==0:
            total-=i
            i+=1
        else:
            total+=i
            i+=1
print("total:",total)