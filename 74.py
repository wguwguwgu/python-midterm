list1=["red","blue","red","green"]
i=0
while (i<10):
    i+=1
    x1=input("輸入顏色順序")
    x2=x1.split(" ")
    out=(" ")
    for j in range(4):
        if (x2[j]==list1[j]):
            out+="1"
            
        elif (x2[j]!=list1[j]and x2[j]in list1):
            out+="2"
            
        else:
            out+="3"
    if (x1=="red blue red green"):
        print("正確答案")
        break
    elif i==10:
        print("挑戰失敗")
        break
    else:
        print(out)
        
