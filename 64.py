a=int(input("請輸入第一個判斷的數字:"))
b=int(input("請輸入第二個判斷的數字:"))
if b>a:
    if b-a==2:
        c =2
        while c<a:
            if a%c ==0:
                print ("N")
                break
            c+=1
        if c==a:
            d=2
            while d<b:
                if b%d==0:
                    print("N")
                    break
                d+=1
            if d==b:
                print("Y")
            
    else:
        print("N")
else:
    if a-b==2:
        c =2
        while c<b:
            if b%c ==0:
                print ("N")
                break
            c+=1
        if c==b:
            d=2
            while d<a:
                if a%d==0:
                    print("N")
                    break
                d+=1
            if d==a:
                print("Y")
            
    else:
        print("N")