class Car:
    def __init__(self,color,price,kilometer):
        self.color=color
        self.price=price
        self.kilometer=kilometer
        
    def __gt__(self,other):
        if(self.kilometer>other.kilometer):
            return "km of car 1 is greater"
        elif(self.kilometer==other.kilometer):
            return "km of car 2 is greater"
        else:
            return "both ran same km "
    

c1=Car("black",120000,16100)
c2=Car("red",110000,2000000)

if(c1.price>c2.price):    
    print("price of car 1 is greater:",c1.price)
print("kilometer of both cars:",c1.kilometer+c2.kilometer)

#if(c1>c2):
 #   print("km of car 1 is greater")
#else:
 #   print("km of car 2 is greater")
#print(c1>c2)
