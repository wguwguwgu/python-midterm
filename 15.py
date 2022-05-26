a=(input("輸入四位數密碼:"))
while len(a)!=4:
    a=input("輸入四位數密碼:")
b=[]
b=list(a)
c=((int(b[0]))+7)%10
d=((int(b[1]))+7)%10
e=((int(b[2]))+7)%10
f=((int(b[3]))+7)%10
print("輸出加密後的數字為:",e,f,c,d)
