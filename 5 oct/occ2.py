
lst=["jabbar","ganeshan","bapputty","hajiyar","ayamu","mayami","kunjayamu","ambili","ambu","ramani","abu"]
count=0
print(lst)
a=input("enter the letter to find the occurance\n")
for n in lst:
   for f in n:
        if f==a:
            count+=1
print("number of ",a," is:", count)