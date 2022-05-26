from itertools import count


a=str(input("檢測的字串:(end結束):"))
for i in range(1):
    if a=="end":
        print("檢測結束")
        break
    else:
        b=str(input("檢測的單一字元:"))
        for i in range(1):
            if len(b)!=1:
                print("超出範圍")
                break
            else:
                print("單元",str(b),"出現次數為:",a.count(b))