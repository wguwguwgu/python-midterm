a=int(input("組數為:"))
for i in range(a):
    b=input("第"+str(i+1)+"組:")
    c=b.split(" ")
    print("第",i+1,"組應收費用:",int(c[0])*250+int(c[1])*175)