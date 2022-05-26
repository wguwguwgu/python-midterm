month=int(input("輸入月份"))
day=int(input("輸入日期"))

if month==1:
    if day<20:
        print("星座為:Capricorn")
    else:
        print("星座為:Aquarius")
elif month==2:
    if day<=19:
        print("星座為:Aquarius")
    else:
        print("星座為:Pisces")
elif month==3:
    if day<=20:
        print("星座為:Pisces")
    else:
        print("星座為:Aries")
elif month==4:
    if day<=20:
        print("星座為:Aries")
    else:
        print("星座為:Taurus")
elif month==5:
    if day<=21:
        print("星座為:Taurus")
    else:
        print("星座為:Gemini")
elif month==6:
    if day<=21:
        print("星座為:Gemini")
    else:
        print("星座為:Cancer")
elif month==7:
    if day<=23:
        print("星座為:Cancer")
    else:
        print("星座為:Leo")
elif month==8:
    if day<=23:
        print("星座為:Leo")
    else:
        print("星座為:Virgo")
elif month==9:
    if day<=20:
        print("星座為:Virgo")
    else:
        print("星座為:Libra")
elif month==10:
    if day<=23:
        print("星座為:Libra")
    else:
        print("星座為:Scorpio")
elif month==11:
    if day<=22:
        print("星座為:Scorpio")
    else:
        print("星座為:Sagittarius")
elif month==12:
    if day<=22:
        print("星座為:Sagittarius")
    else:
        print("星座為:Capricorn")