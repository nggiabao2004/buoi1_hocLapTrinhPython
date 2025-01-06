# j.append(i) //dua vào mang
# 2,3// print(',' .join()) //noi vao

#mảng chứa nhiều kết quả
j=[]
for i in range(2000,3200+1):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print(','.join(j))