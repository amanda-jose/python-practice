# function filter/ removes >lines
def sequence_filter(line):
    return '>' not in line  # if "'>' not in line" is true, then the line is kept in the the list. otherwise if it's false, "> is in line" then it will be filtered out


# with the txt file saved in sequence_file variable,
with open('files/sequence.txt') as sequence_file:
    lines = sequence_file.readlines()
    print(list(filter(sequence_filter, lines)))

# Carry on dont need to stop and close the file
