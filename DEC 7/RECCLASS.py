class Rectangle():
 def __init__(self):
      self.__length = 1.0
      self.__width = 1.0
 def __str__(self):
      return "This is class Rectangle\n"
 def set_length(self,len=1.0):
      self.__length = len
 def set_width(self,wid=1.0): 
      self.__width = wid
 def get_length(self):
      return self.__length
 def get_width(self):
      return self.__width
 def get_area(self):
      return self.get_width() * self.get_length()
 def __lt__(self, other):
      if(self.get_area()<other.get_area()):
           return "1st Rectangle is Smaller."
      elif(self.get_area()==other.get_area()):
           return "Rectangle are of same area"
      else:
           return "2nd Rectangle is Smaller."
my_rect1 = Rectangle()
a=int(input("enter length of rectangle "))
my_rect1.set_length(a)
a=int(input("enter width of rectangle "))
my_rect1.set_width(a)
print ("The length is ", my_rect1.get_length())
print ("The width is ", my_rect1.get_width())
print ("The area is ", my_rect1.get_area())
print (my_rect1)
my_rect2 = Rectangle()
a=int(input("enter length of rectangle "))
my_rect2.set_length(a)
a=int(input("enter width of rectangle "))
my_rect2.set_width(a)
print ("The length is ", my_rect2.get_length())
print ("The width is ", my_rect2.get_width())
print ("The area is ", my_rect2.get_area())
print (my_rect2)
print(my_rect1 < my_rect2)
