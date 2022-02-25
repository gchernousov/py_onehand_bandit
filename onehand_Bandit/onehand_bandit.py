run_program = True

print('Привет, бандит!')

name = input('\nКак тебя называть? : ')

print(f'\nХорошо, {name}, давай сыграем!')
print('\nПравила просты:')

while run_program == True:
    user_choice = input('>>> ')
    if user_choice == '1':
        print('1')
    elif user_choice == 'q':
        run_program = False
        print(f'До следующей встречи, {name}!') 
    else:
        print('Такой команды нет')
else:
    input('\nНажмите любую клавишу, чтобы выйти...')
    