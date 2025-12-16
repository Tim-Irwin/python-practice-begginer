from pathlib import Path

#Establish a path to access data
path = Path('pi_digits.txt')
#Read the data from path and strip any trailing newline characters.
contents = path.read_text().rstrip()

print(contents)
print('\n')

#Split to read long strings into sets of lines.
split_lines = contents.splitlines()
for line in split_lines:
    print(line)
print('\n')


#Builsd a single string from split_lines 
#Use an empty string to store the single string.
pi_string = ''
#Loop through the string and add each line to pi_string
for line in split_lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))

#write to a file. Keep in mind write_text will delete current contents if the file already exists.
ff_path = Path('fun_facts.txt')
new_content = 'I love Python!\n'
new_content += "I love creating with Python! \n"
new_content += "I will succeed at being a Pythonista!"
ff_path.write_text(new_content)
#read and print the data.
ff_read = ff_path.read_text()
print(ff_read)
print('\n')

#exception handling
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")