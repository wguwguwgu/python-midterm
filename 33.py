a=int(input("請輸入國文成績0-100"))
for i in range(1):
    if a<0 or a>100:
        print("超出範圍")
    break
b=int(input("請輸入英文成績0-100"))
for i in range(1):
    if b<0 or b>100:
        print("超出範圍")
    break
c=int(input("請輸入微積分成績0-100"))
for i in range(1):
    if c<0 or c>100:
        print("超出範圍")
    break
d=int(input("請輸入體育成績0-100"))
for i in range(1):
    if d<0 or d>100:
        print("超出範圍")
    break
e=int(input("請輸入程式設計成績0-100"))
for i in range(1):
    if e<0 or e>100:
        print("超出範圍")
    break
list1=[a,b,c,d,e]
f=(a+b+c+d+e)/5
g=round(f,2)
print("平均分數:",g)
h=sorted(list1)
if h[4]==a:
    print("最高分科目:國文",a,"分")
    if h[0]==a:
        print("最低分科目:國文",a,"分")
    elif h[0]==b:
        print("最低分科目:英文",b,"分")
    elif h[0]==c:
        print("最低分科目:微積分",c,"分")
    elif h[0]==d:
        print("最低分科目:體育",d,"分")
    else:
        print("最低分科目:程式設計",e,"分")
elif h[4]==b:
    print("最高分科目:英文",b,"分")
    if h[0]==a:
        print("最低分科目:國文",a,"分")
    elif h[0]==b:
        print("最低分科目:英文",b,"分")
    elif h[0]==c:
        print("最低分科目:微積分",c,"分")
    elif h[0]==d:
        print("最低分科目:體育",d,"分")
    else:
        print("最低分科目:程式設計",e,"分")
elif h[4]==c:
    print("最高分科目:微積分",c,"分")
    if h[0]==a:
        print("最低分科目:國文",a,"分")
    elif h[0]==b:
        print("最低分科目:英文",b,"分")
    elif h[0]==c:
        print("最低分科目:微積分",c,"分")
    elif h[0]==d:
        print("最低分科目:體育",d,"分")
    else:
        print("最低分科目:程式設計",e,"分")
elif h[4]==d:
    print("最高分科目:體育",d,"分")
    if h[0]==a:
        print("最低分科目:國文",a,"分")
    elif h[0]==b:
        print("最低分科目:英文",b,"分")
    elif h[0]==c:
        print("最低分科目:微積分",c,"分")
    elif h[0]==d:
        print("最低分科目:體育",d,"分")
    else:
        print("最低分科目:程式設計",e,"分")
else:
    print("最高分科目:程式設計",e,"分")
    if h[0]==a:
        print("最低分科目:國文",a,"分")
    elif h[0]==b:
        print("最低分科目:英文",b,"分")
    elif h[0]==c:
        print("最低分科目:微積分",c,"分")
    elif h[0]==d:
        print("最低分科目:體育",d,"分")
    else:
        print("最低分科目:程式設計",e,"分")