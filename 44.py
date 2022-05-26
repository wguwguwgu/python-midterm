from numpy import append


a=int(input("輸入整數T:"))
b=[]
if a<1 or a>10:
    print("超出範圍")
else:
    for i in range(a):
        b.append(int(input("輸入每班人數:")))
        c=(sorted((b),reverse=True))
    print(c[0])

