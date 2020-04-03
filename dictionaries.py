# ninja_belts = {"amanda": "red", "ryu": "black"}

# # ninja_belts["amanda"]

# 'ryu' in ninja_belts

# ninja_belts.keys()  # prints out keys: dict_values(['amanda', 'ryu'])

# list(ninja_belts.keys())  # ['amanda', 'ryu']

# ninja_belts.values()  # prints out values: dict_values(['red', 'black'])

# vals = list(ninja_belts.values())  # ['red', 'black']

# vals.count('black')  # answer: 1

# # adding a new ninja
# ninja_belts['yoshi'] = 'red'
# # answer = {'crystal': 'red', 'ryu': 'black', 'yoshi': 'red'}


# def ninja_intro(dictionary):
#     for ninja in ninjas


# # defining a new dictionary
# person = dict(name="amanda", age=24, height="5ft2")
# # person
# # {'name': 'amanda', 'age': 24, 'height': '5ft2'}


def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')


ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter a belt colour:')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)
