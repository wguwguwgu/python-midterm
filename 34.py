a=int(input("輸入一正整數n:"))
for i in range(1):
    if(a<11 or a>1000):
        print("超出範圍")
    break
if(a%2==0 and a%11==0):
    if(a%5!=0 and a%7!=0):
        print(a,"為新公倍數?:YES")
    else:
        print(a,"為新公倍數?:NO")
else:
    print(a,"為新公倍數?:NO")