import math
n=int(input("\n enter the limit \n"))
lst=[]
for i in range(999,n):
         z=math.sqrt(i)
         if z.is_integer():
            lst.append(str(i))
print("all elements\n",lst)
elst=[]
for i in lst:
    count=0
    for z in i:
        if int(z)%2==0:
                count=count+1
        else:
            break
    if count==4:
        elst.append(int(i))
                
print("four even digit  perfect square\n",elst)    
