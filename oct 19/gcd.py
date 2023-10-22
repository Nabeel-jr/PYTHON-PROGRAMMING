a=int(input("enter number 1:   "))
b=int(input("enter number 2:   "))
if a>0 and b>0:
    gcd=1
    for i in range(1, min(a,b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    print(gcd)
else:
    print("+ve numbers only")