#Vehicle Rental
class Vehicle():
    # Created a base class of Vehicle
    def __init__(self, model, rental_rate):
        # Initialized the class constructor, with attributes of model, rental_rate
        self.model = model
        self.rental_rate = rental_rate


    def calculate_rental(self, duration):
        # Parent class method calculate_salary created for polymorphism
        pass
        # Enforcing method implementation in subclasses

class Car(Vehicle):
    # Child class of Car from parent class Vehicle
    def __init__(self, model, rental_rate, luxury_tax):
        # Initialized the class constructor
        Vehicle.__init__(self, model, rental_rate)
        # Explicitly calling parent constructor
        self.luxury_tax = luxury_tax

    def calculate_rental(self, duration):
        # Child class method calculate_rental created for polymorphism
        return (self.rental_rate * duration) + self.luxury_tax
        # Return the value

class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_fee):
        # Initialized the class constructor
        Vehicle.__init__(self, model, rental_rate)
        # Explicitly calling parent constructor
        self.helmet_fee = helmet_fee

    def calculate_rental(self, duration):
    # Child class method calculate_rental created for polymorphism
        return (self.rental_rate * duration) + self.helmet_fee
        # Return the value

class Truck(Vehicle):
    def __init__(self, model, rental_rate, cargo_fee):
        # Initialized the class constructor
        Vehicle.__init__(self, model, rental_rate)
        # Explicitly calling parent constructor
        self.cargo_fee = cargo_fee

    def calculate_rental(self, duration):
    # Child class method calculate_rental created for polymorphism
        return (self.rental_rate * duration) + self.cargo_fee
        # Return the value

# Example usage:
car = Car("Sedan", 1000, 500)
bike = Bike("Sports Bike", 500, 100)
truck = Truck("Mini Truck", 2000, 500)
car1 = Car("Ford-Figo", 2000, 1000)
bike1 = Bike("Race Bike", 1000, 100)
truck1 = Truck("Heavy Truck", 2500, 800)


rental_duration = 5  # Days
#print the values
print("Input Values - Set1")
print("Car rental for Model-Sedan, Rental rate-1000 with Luxury tax-500")
print(f"Car Rental Cost: {car.calculate_rental(rental_duration)}")
print("Bike rental for Model-Sports Bike, Rental rate-500 with Helmet Fees-100")
print(f"Bike Rental Cost: {bike.calculate_rental(rental_duration)}")
print("Truck rental for Model-Mini Truck, Rental rate-2000 with Cargo Fees-500")
print(f"Truck Rental Cost: {truck.calculate_rental(rental_duration)}")

print("Input Values - Set2")
print("Car rental for Model-Ford-Figo, Rental rate-2000 with Luxury tax-1000")
print(f"Car Rental Cost: {car1.calculate_rental(rental_duration)}")
print("Bike rental for Model-Race Bike, Rental rate-1000 with Helmet Fees-100")
print(f"Bike Rental Cost: {bike1.calculate_rental(rental_duration)}")
print("Truck rental for Model-Heavy Truck, Rental rate-2500 with Cargo Fees-800")
print(f"Truck Rental Cost: {truck1.calculate_rental(rental_duration)}")