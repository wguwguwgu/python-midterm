a=str(input("輸入一字元為:"))
b=reversed(list(a))
if list( a)==list( b):
    print("YES")
else:
    print("NO")