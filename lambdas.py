# a small anonymous function that are only used once
#print(list(map(function, nums)))

nums = [1, 2, 3, 4, 5, 6]


# def square(n):
#     return n * n


print(list(map(lambda n: n * n, nums)))
