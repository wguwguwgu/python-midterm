a=float(input("輸入路程公里數"))
if a<1.5:
    print("所需車資為",75)
else:
    b=(a-1.5)/0.25*5+75
    print("所需車資為",b)
