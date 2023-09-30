a=int(input("enter NUM1 \n"))
b=int(input("enter NUM2 \n"))
c=int(input("enter NUM3 \n"))
if a>b and a>c:
    print(a,"is greater than",b,"and", c)
elif b>a and b>c:
    print(b,"is greater than",a ,"and", c)
elif a==b==c:
     print(a,b,c," all are equal")
elif a==b:
    if c>b:
        print(c, "is the greatest")
    else:
        print(a,"&",b,"is the greatest")
elif c==b:
    if a>b:
        print(a, "is the greatest")
    else:
        print(c,"&",b,"is the greatest")    
else:
     print(c,"is greater than",b ,"and", a)
    
    
    
