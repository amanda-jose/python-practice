# w is the second argument to be able to write text to a txt file
with open('files/write.txt', 'w') as write_file:
    write_file.write('Yo yo yo python is awesome')

# a = ammend, so you can write more lines to a file without overriding what's already written there
with open('files/write.txt', 'a') as write_file:
    write_file.write('\n I love it so much, I dream in python')

# \n = new line
quotes = [
    '\n i can resist everything except temptation',
    '\n we are all in the gutter, but some of us are looking at the stars',
    '\n always forgive your enemies, nothing annoys them so much',
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
