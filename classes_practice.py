
class Dog:
    '''A simple class to model a dog'''

    def __init__(self, name, age):
        '''inititialize name and age attributes.'''
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over. Hahaha, {self.name} would never roll over unless it is to sleep.")

my_dog = Dog('Bella',  4)
print(f"my dogs name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Make the dog sit and roll over.
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Rover', 2)
your_dog.sit()
print('\n')
class Restaurant:
    '''A simple class that prints information about a resaurant.'''
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"This restaurant's name is {self.name}.")
        print(f"The restaurant serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.name} is open for business!")

restaurant_one = Restaurant('Georgios', 'pizza')
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

print('\n')

class Car:
    '''A simple class to represent a car'''

    def __init__(self, make, model, year):
        '''Initialize attributes'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 590

    def get_descriptive_name(self):
        '''return a formated car description'''
        description = f"{self.year}, {self.make} {self.model}"
        return description.title()
    
    def read_odometer(self):
        print(f"The car has {self.odometer} miles on it.")

    def update_odometer(self, miles):
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print('You are not allowed to roll back an odometer!')
    
my_new_car = Car('Audi', "R8", 2026)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(560)
my_new_car.read_odometer()

#A child class
class ElectricCar(Car):
    '''Has all aspects of the parent class Car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes'''
        super().__init__(make, model, year)
        self.battery = 40
    
    def battery_size(self):
        print(f"The battery size is {self.battery}-kWh.")

    def get_descriptive_name(self):
        '''Overide a superclass method'''
        description = f"A {self.make} {self.model} from {self.year}."
        return description

my_electric_car = ElectricCar('Chevy', 'Bolt', 2018)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery_size()

