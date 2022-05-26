a=float(input("輸入a值"))
b=float(input("輸入b值"))
c=float(input("輸入c值"))
d=b**2-4*a*c
if d>0:
    e=(-b+(d**0.5))/2*a
    f=(-b-(d**0.5))/2*a
    print(e,f)
elif d==0:
    g=(-b+(d**0.5))/2*a
    print(g)
else:
    print(0)