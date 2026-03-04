#codingan yg sudah di fix

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def drive(self):                                    
        try:
            print(f"The {self.brand} {self.model} is driving.")
        except AttributeError as e:
            print(f"Error: {e}")

    
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def honk(self):                                     
        print("Beep! Beep!")

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity
    
    def load(self, weight):                             
        try:
            print(f"Loaded {weight} kg.")
        except TypeError as e:
            print(f"Error: {e}")
        
def main():
    my_car = Car("Toyota", "Corola", 4)
    my_truck = Truck("Ford", "F-150", 1000)

    try:
        my_car.drive()
        my_car.honk()
    except ArithmeticError as e:
        print(f"Error in Car: {e}")

    try:
        my_truck.drive()
        my_truck.load(1200)
    except AttributeError as e:
        print(f"Error in Truck: {e}")

if __name__ == "__main__":
    main()