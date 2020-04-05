
grades = ['A', 'B', 'F', 'C', 'F', 'A']

#filter(testing_function, grades)


def remove_fails(grade):
    return grade != 'F'  # whatever is returned false, will be removed, aka F


print(list(filter(remove_fails, grades)))

# with for loop

# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
# print(filtered_grades)

# with comprehension method
# print([grade for grade in grades if grade != 'F'])
