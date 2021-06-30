import random

num = random.randint(1,5)
guess = 0
count = 0

print('Guess a number between 1 and 10')
while num != guess:

    count += 1

    guess = input(f'Enter guess #{count}: ')
    if guess.isnumeric() == False:
        print('Numbers only, please!')
        continue
    
    guess = int(guess)
    if guess < num:
        print('Your guess is too low, try again!')
    elif guess > num:
        print('Your guess is too high, try again!')
else:
    print(f'You guessed it in {count} tries!')