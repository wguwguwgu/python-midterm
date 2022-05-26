a=int(input("請輸入西元年:"))
if a%12==6:
    print("tiger")
elif a%12==7:
    print("rabbit")
elif a%12==8:
    print("dragon")
elif a%12==9:
    print("snake")
elif a%12==10:
    print("horse")
elif a%12==11:
    print("sheep")
elif a%12==0:
    print("dog")
elif a%12==1:
    print("chicken")
elif a%12==2:
    print("monkey")
elif a%12==3:
    print("pig")
elif a%12==4:
    print("mouse")
else:
    print("ox")