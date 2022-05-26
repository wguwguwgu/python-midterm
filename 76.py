aa = input("輸入傳送密碼(6位數):")
while len(aa)!=6:
    aa = input("輸入傳送密碼(6位數):")

print("解密後的密碼：",end=" ")
for i in aa:
    for j in range(10):
        if(j*4%7 == int(i)):
            print(j,end=" ")
            break