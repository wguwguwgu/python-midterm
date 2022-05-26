from re import I


a=int(input("輸入階乘值M:"))
b=1
c=1
while b<a:
    c+=1
    b*=c
print("超過M為",a,"的最小階層N值為:",c)