a=str(input("輸入值為(1<=N<=7)"))
list1=(a.split(","))
for i in range(len(list1)):
    list1[i]=int(list1[i])
if len(list1)>7:
    print("超出範圍")
else:
    s=""
    g=""
    int_list = [int(i) for i in list1]
    list1=(sorted(list1))
    for i in range(len(list1)):
        s+=str(list1[i])
    list1=sorted((int_list),reverse=True)
    for i in range(len(list1)):
        g+=str(list1[i]) 

print("最大值數列與最小值數列差值為:",int(g)-int(s))