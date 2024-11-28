import pandas as pd

phonetic = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_df = pd.DataFrame(phonetic)
phonetic_dict = {rows.letter: rows.code for (index, rows) in phonetic_df.iterrows()}

user_input = input("Enter a word: ").upper()

print(user_input)
output_list = [phonetic_dict[letter] for letter in user_input]
print(output_list)