a=int(input("小明身上有幾元:"))
while a<0 or a>100:
    print("超出範圍")
    break
b=int(input("販賣機有幾種飲料:"))
while b<0 or b>30:
    print("超出範圍")
    break
d=0

for i in range (b):
    c=int(input("輸入每種飲料的價格:"))
    while c<10 or c>50:
        print("超出範圍")
        break
    if c<=a:
        d+=1      
print(d)