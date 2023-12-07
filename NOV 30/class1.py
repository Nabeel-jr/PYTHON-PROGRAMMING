class Rec():
     def __init__(self, l, b):
         self.length = l
         self.breadth = b
     
     def area(self):
         return self.length*self.breadth

     def peri(self):
         return 2*(self.length+self.breadth)


l=int(input("Enter the Lenght of Rectangle 1\n"))
b=int(input("Enter the Breadth of Rectangle 1\n"))
rec1 = Rec(l,b)
print("Area1 = ",rec1.area())
print("Perimeter1 = ",rec1.peri())

l=int(input("Enter the Lenght of Rectangle 2\n"))
b=int(input("Enter the Breadth of Rectangle 2\n"))
rec2 = Rec(l, b)
print("Area2 = ",rec2.area())
print("Perimeter2 = ",rec2.peri())

if (rec1.area()==rec2.area()):
    print("Areas are Equal")
else:
    print("Areas are not Equal")
if (rec1.peri()==rec2.peri()):
    print("perimeters are equal")
else:
    print("perimeters are not Equal")
