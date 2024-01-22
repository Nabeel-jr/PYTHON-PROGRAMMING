a= input("ENTER SENTENCE\n")
b=input("\nenter the word to search\n")
lst=a.split()
count=0
for n in lst:
    if n==b:
        z=n
        count+=1
print("number of",z,"is:", count)
