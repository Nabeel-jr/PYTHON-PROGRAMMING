b=int(input("enter current year \n"))
a=int(input("enter future year \n"))

for n in range(b,a+1):
    if n%400==0 or (n%4==0 and n%100!=0):
        print(n," is a leap year")
   # else:
   #     print(n," is a Normal year")
