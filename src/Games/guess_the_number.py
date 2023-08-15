# 1. Generate a random number between 1 to 100
# 2. Ask user for his guess
# 3. If user's guess is less than 1 or greater than 100, then print "Out of Bounds"
# 4. For user's first guess, if a guess is with in the range of 10 than that of actual number,
# then print "warm", else "cold"
# 5. From second guess onwards, if user moves closer to actual number than his previous guess,
# then print "warmer", else print "colder"
# 6. Once user guesses the actual number, print number of guesses in which user has guessed the number

"""
Logical Explanation by Self
cases: Exception (guess is less than 1 or greater than 100)
First guess case
    number + 10 > guess > number - 10
        print('Warm')
    else:
        print('Cold')
Second Case Guess onwards
    abs(previous_guess - number) > abs(current_guess - number)
        print('warmer')
    else:
        print('Colder')
"""

import random


previous_guess = 0
current_guess = 0
attempt = 1
number = random.randint(11,90)
while True:
    try:
        current_guess = int(input('Enter Your Guess: '))
    except ValueError:
        print('Enter Int Only!')
        continue
    if 0 > current_guess  or current_guess > 100:
        print('Invalid Guess')
        continue
    if current_guess == number:
        print('Right Guess!, Attempts: ', attempt)
        break
    if not previous_guess:
        if number + 10 > current_guess > number - 10:
            print('Warm')
        else:
            print('Cold')
        attempt +=1
    else:
        if abs(previous_guess - number) > abs(current_guess - number):
            print('Warmer')
        else:
            print('Colder')
        attempt += 1
    previous_guess = current_guess