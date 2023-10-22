a=input("enter file name\n")
if '.' in a:
    b=a.split(".")
    print(b)  
    print(b[1])
else:
    print("format is wrong")
