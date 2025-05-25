import random

user=0

comc=random.randint(1,3)
if comc==1:
    comp=('✊🏻')
elif comc==2:
    comp=('🤚🏻')
else:
    comp=('✌🏻')

print('Rock Paper Scissors')
print('1) ✊🏻')
print('2) 🤚🏻')
print('3) ✌🏻')
user=int(input('Pick a number: '))


if user==1:
    use=('✊🏻')
elif user==2:
    use=('🤚🏻')
else:
    use=('✌🏻')

print(f'You chose: {use}')
print(f'CPU chose: {comp}')

if user==1:
    if comc==1:
      print('Tie')
    elif comc==2:
        print('CPU won')
    else:
        print('Player won')
elif user==2:
    if comc==1:
      print('Player Won')
    elif comc==2:
        print('Tie')
    else:
        print('CPU won')
elif user==3:
    if comc==1:
      print('CPU won')
    elif comc==2:
        print('Player won')
    else:
        print('Tie')
else:
    print('Error')
