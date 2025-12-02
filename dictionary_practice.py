alien_0 = {'color': 'green', 'points': 5}
#access values   
print(alien_0['color'])
print(alien_0['points'])

#use an empty dictionary
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = '6'
print(alien_1)

print(f'The first alien in {alien_0['color']}.')
print(f'The second alien scored {alien_1['points']} points.')

#alien position tracking
alien_2 = {'x-pos': 0, 'y_pos': 25, 'speed': 'medium'}

#move alien to the right
#Determine how far to move based on current speed.
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    #all fast aliens
    x_increment = 3

#The new postition is the old position plus the increment.
alien_2['x-pos'] = alien_2['x-pos'] + x_increment

print(f'The new position of alien 2 is {alien_2["x-pos"]}!')

#removing key/vlaue pairs
del alien_0['points']
print(alien_0)


alien_0_points = alien_0.get('points', 'No points currently assigned.')
print(alien_0_points)

alien_1_points = alien_1.get('points', 'No points currently assigned.')
print(alien_1_points)

print('\n')

#format with better readibility
person = {
    'first_name': 'Joe',
    'last_name': 'Smith',
    'age': 31,
    'city': 'Chicago'
}
print(person.get('first_name', 'Jane'))
print(person.get('last_name', 'Doe'))
print(f'{person.get('first_name')} {person.get('last_name')} has an age of {person.get('age')} and lives in {person.get('city')}!')


print('\n')
#Use a for loop to traverse a dictionary
user_0 = {
    'username': 'tirwin',
    'first_name': 'Tim',
    'last_name': 'Irwin'
}

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

print('\n')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, lang in favorite_languages.items():
    print(f'{name.title()}\'s fovorite language is {lang.title()}!')


print('\n')
#Looping through keys
for name in favorite_languages.keys():
    print(name.title())


print('\n')
#Looping through values
for lang in favorite_languages.values():
    print(lang.title())

#Using set()
for lang in favorite_languages.values():
    print(lang.title())

print('\n')
#Sets are built using {}
langs = {'Python', 'Java', 'Javascript'}
print(langs)

print('\n')
#Nesting
#empty list of aliens
aliens = []

#create 10 aliens
for alien_num in range(10):
    new_alien = {'color': 'Blue', 'score': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)
print(len(aliens))

print('\n')
#lists in dictionaries
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite languages are:")
    for val in value:
        print(val.title())
    print('\n')

print('\n')
#dict inside dict
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f'Username: {username}')
    print(f'Full Name: {user_info['first'].title()} {user_info['last'].title()}')
    print(f'Location: {user_info['location'].title()}')
    print('\n')