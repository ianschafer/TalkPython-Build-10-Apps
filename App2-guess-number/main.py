import random

print('---------------------------------')
print('   GUESS THE NUMBER GAME')
print('---------------------------------')
print()

# Generate a random number
the_number = random.randint(0, 100)
guess = -1

# Get player's name using input function
Player_name = input('Enter your name: ')

# While loop to cycle the game until player wins
while guess != the_number:
    # get player guess as a string
    stringGuess = input('Guess a number between 0 and 100: ')
    # Convert string to int
    guess = int(stringGuess)

    # Output result
    if guess < the_number:
         print('Sorry {}, your guess of {} was too LOW.'.format(Player_name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(Player_name, guess))
    else:
        print('Excellent work {}, you succeeded, it was indeed {}!'.format(Player_name, guess))

print('done')

