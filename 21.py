list1=[[123,"Tom","DTGD"],[456,"Cat","CSIE"],[789,"Nana","ASIE"],[321,"Lim","DBA"],[654,"Won","FDD"]]
a=int(input("輸入查詢學號為:"))
if a==list1[0][0]:
    print("學生資料為",list1[0][0],list1[0][1],list1[0][2])
elif a==list1[1][0]:
    print("學生資料為",list1[1][0],list1[1][1],list1[1][2])
elif a==list1[2][0]:
    print("學生資料為",list1[2][0],list1[2][1],list1[2][2])
elif a==list1[3][0]:
    print("學生資料為",list1[3][0],list1[3][1],list1[3][2])
elif a==list1[4][0]:
    print("學生資料為",list1[4][0],list1[4][1],list1[4][2])
else:
    print("查無此人")