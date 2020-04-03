ny_name = 'ryu'


def print_name():
    global my_name  # globally changes this variable to yoshi even though it's currenty in local scope
    my_name = 'yoshi'
    print('the name inside the function is', my_name)


print_name()
print('outside the function the name is', my_name)
