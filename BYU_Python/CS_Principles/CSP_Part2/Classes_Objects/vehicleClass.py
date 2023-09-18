class Vehicle: # Define a class called Vehicle
    def weight_per_passenger(self): # Define a function in the class
        return self.weight / self.passengers
    def passenger_economy(self): # Define another class function
        return self.vehicle_economy * self.passengers
    def passenger_distance_cost(self, fuel_price):
        return fuel_price / self.passenger_economy()

#car object
my_car = Vehicle()
my_car.weight = 1500
my_car.passengers = 5
c = my_car.weight_per_passenger()
print(c)

#ship object
titanic = Vehicle()
titanic.weight = 54000
titanic.passengers = 2400
titanic.vehicle_economy = 0.75
print(titanic.weight_per_passenger())
print(titanic.passenger_economy())

print(titanic.passenger_distance_cost(72))

print(Vehicle)