i=-1
a=[]
b=[]
while i==-1:
    z=int(input("enter number to list 1 or '0' to exit  \n"))
    if z==0 :
        break;
    else:       
        a.append(z)
for n in a:
    if n%2==0:
        b.append(n)
print("list=",a)
print("even=",b)
