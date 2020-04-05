# new_list = map(function, data)

from random import shuffle


def jumble(word):
    anagram = list(word)  # ['b', 'e', 'e', etc]
    shuffle(anagram)
    return ''.join(anagram)


words = ['beetroot', 'carrots', 'potatoes']

anagrams = []

# with for loop

# for word in words:
#     anagrams.append(jumble(word))
#     print(anagrams)


# With map method

# print(map(jumble, words))
# print(list(map(jumble, words)))


# with comprehension method

print([jumble(word) for word in words])
