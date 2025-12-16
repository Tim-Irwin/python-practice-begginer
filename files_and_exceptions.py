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

