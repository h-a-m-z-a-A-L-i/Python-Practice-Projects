import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# print(new_dict)
def generate_phonetic():
    word = input('What is word:').upper()
    try:
        output_list = [new_dict[letter] for letter in word]
    except KeyError:
        print(
            'Sorry! Please write alphabets only')# If user input digits it will call function again to get another input
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
