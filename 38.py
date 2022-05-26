a=int(input("輸入n個數:"))
b=[]
for i in range(1):
    if a<2 or a>10:
        print("超出範圍")
        break
    else:
        for i in range(a):
            b.append(int(input("小名猜想的點與家的距離k:")))
            if b[i]<1 or b[i]>1000:
                print("超出範圍")
                break
            else:
                
                if b[i]%9==0 or b[i]%11==0:
                    print("第",i+1,"個點",b[i])
                        
                    
                