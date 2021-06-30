import random

num = random.randint(1,5)
value = 0
count = 0

while num != value:

    count += 1
    value = input('Print a number between 1 and 5: ')
    if value.isnumeric():
        value = int(value)
else:
    print(f'You guessed it in {count} tries!')