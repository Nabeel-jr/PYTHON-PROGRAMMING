j=int(input("enter the number of terms: "))

a=0
b=1
print(a)
print(b)
for i in range(j+1):
    z=a+b
    print(z)        
    a=b
    b=z
