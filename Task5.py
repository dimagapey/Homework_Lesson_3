import random
some_numb = random.randint(0, 10)

attempts = 0
while attempts < 3:
    enter_number = (input('Введите число от 1 до 10: '))
    if int(enter_number) == some_numb:
        print('You won :)')
        break
    else:
        print('One more chance...')
    attempts += 1
else:
    print('You lose :(')
print(f'Ответ is {some_numb}')