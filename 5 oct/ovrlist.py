
a=int(input("\n enter limit of list \n"))
i=0
lst=[]
while i<a:
    z=int(input("enter number"))
    if z > 100 :
        lst.append("over listed")
    else:       
        lst.append(z)
    i+=1
print(lst)
