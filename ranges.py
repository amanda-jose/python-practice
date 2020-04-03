for n in range(5):
    # do something, range generates a list of numbers, here it is non-inclusive of 5
    print(n)

for n in range(3, 10):
    print(n)

for n in range(0, 20, 4):  # start at 0, go up to 20 (non-inclusive) and in multiples of 4)
    print(n)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

for n in range(len(burgers)):
    print(n, burgers[n])

# going backwards in a list, -1 is starting position of the last element in varaible
for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])
