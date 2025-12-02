
name = 'tim'

print(f'Hello {name}, would you like to learn Python today?')

print(name.lower())
print(name.upper())
print(name.title())

#A famous quote
print('Albert Einstein once said, “A person who never made a mistake never tried anything new."')

famous_person = 'Albert Einstein'
message = f'{famous_person} once said, “A person who never made a mistake never tried anything new."'
print(message)

white_space_name = '  tim  '
print(white_space_name.rstrip())
print(white_space_name.lstrip())
print(white_space_name.strip())

filename = 'pyhton_notes.txt'
print(filename.removesuffix('.txt'))