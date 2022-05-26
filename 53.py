a=int(input("輸入n值:"))
b=[]
c=[]
for i in range(a):
    b.append(str(input("請輸入姓名:")))
    c.append(str(input("請輸入電子郵件:")))
d=str(input("輸入欲查詢電子郵件姓名:"))
for i in range(0,a,1):
    if d==b[i]:
        print(b[i],"電子郵件帳號為",c[i])
    else:
        i+=1