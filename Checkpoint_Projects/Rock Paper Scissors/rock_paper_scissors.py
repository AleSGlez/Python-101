import random

player_choice_number=0

computer_choice_number=random.randint(1,3)
if computer_choice_number==1:
    computer_choice=('✊🏻')
elif computer_choice_number==2:
    computer_choice=('🤚🏻')
else:
    computer_choice=('✌🏻')

print('Rock Paper Scissors')
print('1) ✊🏻')
print('2) 🤚🏻')
print('3) ✌🏻')
player_choice_number=int(input('Pick a number: '))


if player_choice_number==1:
    player_choice =('✊🏻')
elif player_choice_number==2:
    player_choice =('🤚🏻')
else:
    player_choice =('✌🏻')

print(f'You chose: {player_choice}')
print(f'CPU chose: {computer_choice}')

if player_choice_number==1:
    if computer_choice_number==1:
      print('Tie')
    elif computer_choice_number==2:
        print('CPU won')
    else:
        print('Player won')
elif player_choice_number==2:
    if computer_choice_number==1:
      print('Player Won')
    elif computer_choice_number==2:
        print('Tie')
    else:
        print('CPU won')
elif player_choice_number==3:
    if computer_choice_number==1:
      print('CPU won')
    elif computer_choice_number==2:
        print('Player won')
    else:
        print('Tie')
else:
    print('Error')