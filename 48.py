a=int(input("輸入筆數n:"))
for i in range(1):
    if a<4:
        print("查詢量太少")
        break
    else:
        
        b=[]
        for i in range(a):
            c=input()
            d=c.split()
            for i in range(2):
                b.append(d[i])
        e=str(input("輸入欲查詢單字:"))
        for i in range(0,a,2):
            if e==b[i]:
                print(b[i],"中文意思為",b[i+1])

    