#function to display a basic message
def display_message():
    print('This is a file to practice functions.')

#function call
display_message()

#example of a function that uses a parameter.
def favorite_book(title):
    print(f'My favorite book as a teenager was {title.title()}.')

#call the function and pass an argument.
favorite_book("Enders Game")

#positional arguments
def my_pet(animal_type, animal_name):
    '''display information about a pet'''
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name}.")

#call the function
my_pet('dog', 'Bella')

#same function as above using keyword arguments. The function remains unchanged.
def pet_description(animal_type, animal_name):
    '''display information about a pet'''
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name}.")

#call the function using keywords.
pet_description(animal_type='cat', animal_name='Twiggy')

#using default values
def pet_bird(bird_name, bird_type='parrot'):
    '''display info about the bird'''
    print(f"My pet {bird_type} is named {bird_name}.")

#call the pet_bird function.
pet_bird(bird_name="Sniffles")
pet_bird(bird_name="George", bird_type="Canary")

#functions that return
def get_formatted_name(first_name, last_name):
    '''return a full name, formatted.'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

myself = get_formatted_name('Timothy', 'Irwin')
print(myself)

#retur:n a dictionary
def build_person(first_name, last_name, age=None):
    '''return a dictionary regarding a person'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age        
    return person

myself = build_person('Timothy', 'Irwin', age=30)
print(myself)

#passing a list as a parameter
user_list = ['Timothy', 'Carl', 'Jane']
def user_greeting(users):
    '''print a greeting for each user'''
    for user in users:
        print(f"Hello, {user.title()}!")
user_greeting(user_list)

# pass a copy of a list so you dont modify the original
# function_name(list_name[:])

#passing an unknown number of arguments
#you can mix unkown number of arguments and positional arguments.
def make_cake(flavor, *ingredients):
    '''print a list of ingredients'''
    print(f'Making a {flavor} cake with the following ingredients:')
    for ingredient in ingredients:
        print(ingredient)
        
make_cake('chocolate', 'frosting', 'sprinkles', 'candle')

#using an abritray number of keywordd arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

#importing an entire module use format
#module_name.function_name()

#importing a specific function from a module use format
#from module_name import function_name

#using as to give a funtion an alias use format
#from module_name import function_name as fn

#importing all functions from a module
#from module_name import *

