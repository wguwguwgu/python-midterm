a=int(input("輸入所使用度數"))
if(a<120):
    print("Summer months:",round( a*2.1,2),"Non-Summer months",round( a*2.1))
if(120<a<330):
    print("Summer months",round( a*3.02,2),"Non-Summer months",round( a*2.68,2))
if(331<a<500):
    print("Summer months",round( a*4.39,2),"Non-Summer months",round( a*3.61,2))
if(501<a<700):
    print("Summer months",round(a*4.97,2),"Non-Summer months",round(a*4.01,2))
else:
    print("Summer months",round(a*5.63,2),"Non-Summer months",round(a*4.5,2))