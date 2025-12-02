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
