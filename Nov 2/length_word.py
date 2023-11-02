
n=int(input("\n enter the limit \n"))

lst=[]
a=0
b=0
z=0
for i in range(n):
    m=input("\n enter the word \n")
    a=len(m)
    if a>b:
        z=a
    elif b>a:
        z=b
    else:
        z=a
    b=a
    lst.append(m)
print(lst)
print("\n max lenght of word is: ",z-1)
