a=int(input("輸入月份"))
if(a<1 or a>12):
    print("超出範圍")
else:
    for i in range(1):
        if a==1 or 3 or 5 or 7 or 8 or 10 or 12:
            b=int(input("輸入出生日期"))
            if(b<1 or b>31):
                print("超出範圍")
                break
            else:
                c=(a*2+b)%3
                if c==0:
                    print("普通")
                elif c==1:
                    print("吉")
                else:
                    print("大吉")
        elif a==4 or 6 or 9 or 11:
            b=int(input("輸入出生日期"))
            if(b<1 or b>30):
                print("超出範圍")
                break
            else:
                c=(a*2+b)%3
                if c==0:
                    print("普通")
                elif c==1:
                    print("吉")
                else:
                    print("大吉")
        else:
            b=int(input("輸入出生日期"))
            if(b<1 or b>28):
                print("超出範圍")
                break
            else:
                c=(a*2+b)%3
                if c==0:
                    print("普通")
                elif c==1:
                    print("吉")
                else:
                    print("大吉")