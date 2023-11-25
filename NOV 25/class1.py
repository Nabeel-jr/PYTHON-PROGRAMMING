class Bike:
    bike_stroke=4
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

b1=Bike("dominar 400",161)
print("bike name:",b1.name,"\n speed:",b1.speed)
print("engine stroke:",Bike.bike_stroke)
b1.cost=260000
print("cost:",b1.cost)

Bike.bike_stroke=2

b2=Bike("max 100",100)
print("\n \n bike name:",b2.name,"\n speed:",b2.speed)
print("engine stroke:",Bike.bike_stroke)

b2.cost=10000
print("cost:",b2.cost)
