#define a class
class Cat:
    species = "meow" #class attribute


    def __init__(self, name, age):  #it automaticaly initializes object attributes when an object is created. Automaticaly called when the object is created
        self.name = name #Instance attribute
        self.age = age #Instance attribute


    def meow(self): #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class 
        #it does not have to be named self always, you can call whatever you like, but it has to be the first parameter of any function in the class
        print(f"{self.name} is meowing")


         
# Create an object from the class
cat1 = Cat("Garfield", 5)

print(cat1.name)
print(cat1.age)

#Access the class attribute
print(cat1.species)


cat1.meow()
#Inside meow() self.name accesses the specific cat's name and prints it 
class Dog():
    species = "Canine"
    
    def __init__(anything, weight, age):#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class 
        #it does not have to be named self always, you can call whatever you like, but it has to be the first parameter of any function in the class
        anything.weight = weight
        anything.age = age

    def get_weight(random):
        return f"Weight of the dog is {random.weight} kgs"


dog1 = Dog(10, 2)
print(dog1.weight)
print(Dog.get_weight(dog1))