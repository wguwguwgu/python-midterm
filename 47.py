a=int(input("輸入筆數:"))
list1=[]
for i in range(a):
    x1=input()
    x2=x1.split()
    for i in range(2):
        list1.append(x2[i])
for i in range(0,8,2):
    print(list1[i],"牌得到",list1[i+1],"面")