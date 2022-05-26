a=(input("輸入月租費及通話時間"))
list1=list(a.split(","))
b=int(list1[0])
c=int(list1[1])
for i in range(1):
    if b!=186 and b!=386 and b!=586 and b!=986:
        print("超出範圍")
        break
    else:
        if b==186:
            c*=0.09
            if c<=372:
                c*=0.9
            else:
                c*=0.8
        elif b==386:
            c*=0.08
            if c<=772:
                c*=0.8
            else:
                c*=0.7
        elif b==586:
            c*=0.07
            if c<=1272:
                c*=0.7
            else:
                c*=0.6
        elif b==986:
            c*=0.06
            if c<=1972:
                c*=0.6
        else:
            c*=0.5
    print("通話費為",round(c))


#if b==186:
#        c*0.09
#        if c<=372:
#            c*0.9
#        else:
#            c*0.8
#    elif b==386:
#        c*0.08
#        if c<=772:
#            c*0.8
#        else:
#            c*0.7
#    elif b==586:
#        c*0.07
#        if c<=1272:
#            c*0.7
#        else:
#            c*0.6
#    elif b==986:
#        c*0.06
#        if c<=1972:
#            c*0.6
#        else:
#            c*0.5