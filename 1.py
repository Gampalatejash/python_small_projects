import random
random_number=random.randint(1,100)

attems=0
max_attems=10
print('welcome to guessing game')
print('here 10 chances we have to find correct number ')
print('hint ! the correct number in between 1 to 100')

while attems<max_attems:
  try:
    guess=int(input('guess a number : '))
    attems+=1  
    if attems==max_attems:
      print('your guesses is over')
    if guess < random_number:
      print('too low')
    elif guess > random_number:
      print('too high')
    elif guess==random_number:
      print('correct you win')
      break
  except ValueError:
    print('please enter a valid number')
