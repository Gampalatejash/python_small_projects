import random

while True:
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  roll=input('roll the dice (y/n) : ').lower()
  if roll=="y" :
    print(f'{dice1},{dice2}')
    
  elif roll=="n":
    print('thanks for playing')
    break
  else :
    print('invalid choice')
  play_again = input('Do you want to roll again? (y/n): ').lower()
  if play_again != 'y':
    print('Thanks for playing!')
    break