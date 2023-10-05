a= input("ENTER SENTENCE\n")
b=input("\nenter the word to search\n")
lst=a.split()
count=0
for n in lst:
    if n==b:
        count+=1
print("number of",n,"is:", count)