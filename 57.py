a=input("請選擇主餐及升級的套餐:")
b=a.split()
c=0
while len(b)!=2:
    print("輸入錯誤")
    break
e=input("是否升級成大杯飲料?")
if e==("是"):
    f=7
else:
    f=0
g=input("是否換成大薯?")
if g==("是"):
    h=13
else:
    h=0
if b[1]==("A"):
    d=55
elif b[1]==("B"):
    d=68
else:
    ("輸入錯誤")
if b[0]==("1"):
    c+=72
elif b[0]==("2"):
    c+=62
elif b[0]==("3"):
    c+=82
elif b[0]==("4"):
    c+=44
elif b[0]==("5"):
    c+=60
else:
    print("輸入錯誤")
print("總共為",c+d+h+f,"元")
