a,b=map(int,input("Nhập 2 số nguyên dương : ").split())
a>=0 and b>=0
c=(a*b)%10
print ("Phép tích của a và b là : ",a*b)
print ("Hàng đơn vị của phép tích a và b là :",c)
print ("Hàng chục của phép tích a và b là :",((a*b)//10)%10)
        