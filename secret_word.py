secret_word = 'raspberry'
correct_letter = ''
attempts = 0

while True:
    entered_letter = input('ENTER A LETTER: ')
    attempts += 1

    if len(entered_letter) > 1:
        print('Invalid length')
        continue

    for letter in secret_word:
        if entered_letter in secret_word:
            correct_letter += entered_letter
    
    new_str = ''

    for secret_letter in secret_word:
        if secret_letter in correct_letter:
            new_str += secret_letter
        else:
            new_str += '*'

    print(f'{new_str}')

    if new_str == secret_word:
        print(f'YOU WON AFTER {attempts} attempts')
        break
