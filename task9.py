from datetime import date
#Class, Object and Members
class Car:
    wheels = 4
    
    def __init__(self, make, model):
        self.make = make      
        self.model = model    
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Wheels: {self.wheels}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display_info()  
car2.display_info()

#Data Hiding and Object Printing
class Car:
    __engine_type = "V6"  # private attribute 
    _num_wheels = 4       # protected attribute

    def display_specs(self):
        print("Engine Type:", self.__engine_type)
        print("Number of Wheels:", self._num_wheels)

my_car = Car()


my_car.display_specs()
# trying to access attribute outside the class 
print("Outside the class:", my_car._num_wheels)    

#Inheritance, examples of object, issubclass and super
# Inheritance in Python
class Parents:
    def Lands(self):
        print("Having their own properties")

class Child(Parents):
    def Money(self):
        print("Access parents' property")

C = Child()
C.Lands() 
C.Money() 

#issubclass
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Sedan(Car):
    pass

print(issubclass(Car, Vehicle))         
print(issubclass(Vehicle, Sedan))      
print(issubclass(Sedan, Vehicle))      
print(issubclass(Vehicle, Vehicle))     

#superclass
class Laptop:
    def __init__(self):
        self.memory = "16GB"
        self.disk = "1TB"
        print("Laptop class constructor")

class GamingLaptop(Laptop):
    def __init__(self):
        super().__init__() 
        self.graphics = "NVIDIA GTX 3060"
        print("GamingLaptop class constructor")

my_laptop = GamingLaptop()
print(my_laptop.__dict__)  

# Polymorphism in Python
print("Welcome")        
print(10 + 5)           
print(3.14)            

print(len("Python"))     
print(len([1, 2, 3, 4])) 
print(len((9, 8, 7)))   
# class and static variables in python 
# class variables
class Car:
    wheels = 4

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

print(Car.wheels) 

car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Ford")
print(car1.wheels)  
print(car2.wheels)  

# Static variables
class MathOperations:
    pi = 3.14159

    @staticmethod
    def multiply(a, b):
        return a * b

result = MathOperations.multiply(5, 4)
print(result) 

# Class method and static method in python
# Class Method
class Car:
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year

    def description(self) -> str:
        return f"{self.model} was manufactured in {self.year}."

    @classmethod
    def from_age(cls, model: str, age: int):
        current_year: int = date.today().year
        year = current_year - age
        return cls(model, year)

if __name__ == "__main__":
    my_car = Car.from_age("Toyota Camry", 5)
    print(my_car.description())  

#Staticmethod
class Geometry:
    def __init__(self, version: int):
        self.version = version

    def description(self):
        print(f"Running geometry module in version: {self.version}")

    @staticmethod
    def calculate_rectangle_area(length: float, width: float) -> float:
        return length * width

if __name__ == '__main__':
    geo1 = Geometry(1)
    geo2 = Geometry(2)
    
    geo1.description() 
    geo2.description() 
    
    # Calculate the area of a rectangle
    length = 5
    width = 10
    area = Geometry.calculate_rectangle_area(length, width)
    print(f"Area of the rectangle: {area}") 

