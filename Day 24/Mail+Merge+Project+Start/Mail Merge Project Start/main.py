PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt', 'r') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt', 'r') as letter_file:
    letters = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters.replace(PLACEHOLDER, stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.doc', 'w') as invited_file:
            invited_file.write(new_letter)


