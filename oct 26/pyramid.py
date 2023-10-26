j=int(input("enter the number of terms: "))

def pr(j):
    for i in range(1,j+1):
        for n in range(1,i+1):
            print(n*i,end=" ")
        print("\n")
pr(j)
