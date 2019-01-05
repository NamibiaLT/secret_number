# Guess the number
import random
print('Hello! What\'s your name?')
name = input()

secretNum = random.randint(1, 50)

print('Awesome ' + name + '! I am thinking of a number between 1 and 50.' )

try:
  for takeGuess in range(1, 10):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNum:
      print('Your guess is too low')
    elif guess > secretNum:
      print('Your guess is too high')
    else:
      break

  if guess == secretNum:
    print('Great job, ' + name + '! You got the correct guess in ' + str(takeGuess) +' guesses' )
  else:
    print('Next time! The number I was thinking of was ' + str(secretNum))
except ValueError:
  print('Hmmm, ' + name + 'looks like you didn\'t provide a numerical value. Rerun the program.')

