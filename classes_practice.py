
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