age = 25
num = 0

while num < age:
    # block of code
    if num == 0:
        num += 1
        # to skip this iteration. The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
        continue
    if num % 2 == 0:
        print(num)  # inifinte loop
    if num < 10:
        break
    num += 1
