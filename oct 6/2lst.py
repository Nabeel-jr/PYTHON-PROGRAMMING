
i=-1
a=[]
b=[]
while i==-1:
    z=int(input("enter number to list 1 or '0' to exit  \n"))
    if z==0 :
        break;
    else:       
        a.append(z)

while i==-1:
    z=int(input("enter number to list 2 or '0' to exit  \n"))
    if z==0 :
        break;
    else:       
        b.append(z)
print(a)
print(b)
if len (a)==len(b):
     print("list are same length",len(a))
else:
     print("list 1 is",len(a),"length and list 2 is of",len(b),"length")
if sum(a)==sum(b):
     print("lists have same sum  ",sum(a))
else:
     print("list 1 is",sum(a),"sum and list 2 is of",sum(b),"sum")
for n in a:
    for z in b:
        if n==z:
            print("\n",n,"is in both at list 1 in position ",a.index(n),"and list 2 in",b.index(z),"position")
            
     
