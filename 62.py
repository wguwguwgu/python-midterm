dict1={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
a=input("請輸入水果")
if a in dict1:
    print(a,"是",str(dict1[a]))
else:
    print("超出範圍")