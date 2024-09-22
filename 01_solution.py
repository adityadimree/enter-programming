#to ye class ek form jesa hai... isme do blank spaces hai jisme aapko car ka brand and model ye do fillings krni padti hai.
class Car():
    total_car = 0
#as an telephone line... class ke andar hamesha self ka use le. Jese aap call krte hai to aap batate ho ki me aditya bol raha hu or directly ye nhi bolte ki me bol raha hu... to ye jo aap batate ho na yhi self krta hai yaha pe.
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1 
    def full_name(self):
        return f"{self.__brand} {self.__model}"
#so this is encapsulation, brand class ke inside to accesesible hai but class ke outside use koi bhi access nhi kr skta....
    def get_brand(self):
        return self.__brand + " !"
    def fuel_type(self):
        return "Petrol or Diesel"
#Static method.... a method which only belongs to the class but not the instance(mtlb object) of the class    
    staticmethod
    def general_description():
        return "We don't pray for love we just pray for cars."
#using property decorator you cannot overrite the value of any attribute of the object plus aap ko uski original value ko obtain krne ke liye koi method ko call nhi krna padta... 
    @property
    def model(self):
        return self.__model + "!"
# ye getter method setup krne se user ko ab getter method ke zariye hi brand ka access milega or kisi bhi tareeke se nhi milega...
#yaha pe ElectricCar ne Car class se inheritence li hai, mtlb jo jo car class ke pass hai vo ab ElectricCar class ke pass bhi hai... tbhi to bina full name vali funcionality define kre bhi ElectricCar me use access krr paye.
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,  model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
class Battery:
    def battery_info(self):
        return "This is Lithium ion battery."
class Engine:
    def engine_info(self):
        return "Engine working fine"
class ElectricCarTwo(Battery, Engine, Car):
    pass
my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
my_car1 = Car("Mahindra", "Nexon")
#double hash lagane se attribute privatize ho jata hai... to object directly to us attribute ko kbhi call nhi kr skta... ab use access krne ke liye getter methhod ko call krna padega but double hash lagane ke baad agar property decorator ke use kr liya jaye to object directly call to kr skta hai attribute ko but overrite nhi kr skta 
my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
