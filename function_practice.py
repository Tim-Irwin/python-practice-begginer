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

#return a dictionary
def build_person(first_name, last_name, age=None):
    '''return a dictionary regarding a person'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age        
    return person

myself = build_person('Timothy', 'Irwin', age=30)
print(myself)