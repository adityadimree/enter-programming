class Car():
    car_count = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.car_count += 1
    def description(self):
        print(f"Brand : {self.__brand}, Model : {self.__model}, Battery size : {self.battery_size}")
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        print("Petrol or diesel")
    staticmethod #self to hai nhi to object to call nhi kr payega but car is method ko call kr skti hai so this types of methods are called staticmethod.
    def gen_description():
        print("Cars are great")
    @property
    def model(self):
        return f"{self.__model} !!"
class Electric_car(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        print("Electric charge.")
class Battery():
    def battery_info(self):
        return "Battery working fine."
    
class Engine():
    def engine_info(self):
        return "Engine working fine."

class Electric_car_two(Car, Engine, Battery):
    pass
        
my_tesla = Electric_car("Tesla", "Smodel", "67Kwh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, Electric_car))
my_new_tesla = Electric_car_two("Tesla", "S class")
print(my_new_tesla.model)
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())