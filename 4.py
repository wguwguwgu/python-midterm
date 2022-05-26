s = float(input("輸入X座標點:"))
t = float(input("輸入y座標點:"))
u=s**2+t**2

if s>0 and t>0:
    print("該點位於第一象限，離原點距離為根號",u)
else:
    if s>0 and t<0:
        print("該點位於第二象限，離原點距離為根號",u)
    else:
        if s<0 and t<0:
            print("該點位於第三象限，離原點距離為根號",u)
        else:
            if s<0 and t>0:
                print("該點位於第四象限，離原點距離為根號",u)
            else:
                if t==0 and s>0:
                    print("該點位於右半X軸上，離原點距離為根號",u)
                elif t==0 and s<0:
                    print("該點位於左半X軸上，離原點距離為根號",u)
                elif s==0 and t>0:
                    print("該點位於上半Y軸上，離原點距離為根號",u)
                elif s==0 and t<0:
                    print("該點位於下半Y軸上，離原點距離為根號",u)
                else:
                    print("該點位於原點")