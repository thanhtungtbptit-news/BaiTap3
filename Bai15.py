a=int(input("Nhập số nguyên dương a: "))
if a <= 0:
    print("Vui lòng nhập số nguyên dương!")
    a=int(input("Nhập số nguyên dương a: "))
else:    
    b=6*a*(a-1)+1
    print("Số lớp của hình lập phương là: ",b)