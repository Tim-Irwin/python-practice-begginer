#User input
#message = input('Please enter your name:\n')
#print(f'Hello, {message}')

#age = input('How old are you?')
#age = int(age)
#if age >= 21:
#    print('You are old enough to purchase alcohol!')
#else:
#    print('You are not old enough to drink!')

#while loops
count = 1
while count <= 5:
    print(count)
    count += 1


prompt = '\nTell me your name:'
prompt += "\nEnter 'quit' to exit the program. "

active = True
while active:
    message = input(prompt)
    #test for user to quit. if quit then active is false and loop does not continue.
    if message == 'quit':
        active = False
        #if not quit then print message and while loop runs again.
    else:
        print(message)

#using continue 
#print odd nums
current_num = 0
while current_num < 5:
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(current_num)

#Movie ticket price
prompt = '\nTell me your age and I will let you know how much your movie ticket is.'
prompt += "\nType 'quit' to exit.\n"

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    elif int(message) < 3:
        print('The ticket is free.')
    elif int(message) <= 12:
        print('The ticket will cost you $10')
    elif int(message) > 12:
        print('The ticket will cost you $15')

#remove all instaces in a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

print(pets)

#filling a dictionary with user input
responses = {}

#set a flag to continue
active = True
#while active
while active:
    #prompt the user for name and favortie car brand
    name = input('\nPlease enter your name:\n')
    car = input('\nWhat is your favorite car brand:\n')
    #Store response in dict
    responses[name] = car

    #ask for another user. If no then terminate loop.
    repeat = input('\nWould another user like to respond? (Y/N)')
    if repeat == 'N':
        active = False

    #loop through key, value in dict to print messages.
    for key, value in responses.items():
        print(f"{key}'s favorite car brand is {value}.")
    