from graphics import circ as c 
from graphics import rec
from graphics.threedshape import cuboid,sphere

r=float(input("enter the radius of circle to find area and circumference \n"))
print("The Area of the cicle is: \n",c.cirar(r),"")
print("\nThe circumference  of the cicle is: \n",c.cirpara(r))

l=float(input("enter the length of rectangle to find Area and parameter\n"))
b=float(input("enter the bredth of rectangle to find Area and parameter\n"))
print("\nThe parimeter of the rectangle is: \n",rec.recpara(l,b))
print("\nThe Area of the rectangle is: \n",rec.recare(l,b))

l=float(input("enter the length of cuboid to find area and parimeter\n"))
b=float(input("enter the bredth of cuboid to find area and parimeter\n"))
h=float(input("enter the height of cuboid to find area and parimeter\n"))
print("\nThe Area of the cuboid is: \n",cuboid.cubar(l,b,h))
print("\nThe pereimeter of the cuboid is: \n",cuboid.cubpara(l,b,h))

r=float(input("\nenter the radius of sphere to find area and Volume\n"))
print("The Area of the sphere is: \n",sphere.sphar(r))
print("\nThe Volume of the sphere is: \n",sphere.sphvol(r))

