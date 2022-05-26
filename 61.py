a=input("請輸入遊戲時間:")
b=a.split(":")
for i in range(1):
    if int(b[1])>60:
        print("超出範圍")
        break
    c=int(b[0])*60+int(b[1])
    d=(c-75)//30+1
    e=d//3
    f=d//2
    g=d*6+e-f
    print(g,"隻兵")