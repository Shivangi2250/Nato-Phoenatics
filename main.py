import pandas

phoenatic_data=pandas.read_csv("nato_phonetic_alphabet.csv")
phoenatic_df=pandas.DataFrame(phoenatic_data)
# print(phoenatic_df)

phoenatic_dict={row.letter:row.code for (index,row) in phoenatic_df.iterrows()}
# print(phoenatic_dict)

# for (index,row) in phoenatic_df.items():
#     print(row.letter)
generate_phoenatic=True
while generate_phoenatic==True:
    try:
        user_word=input("enter a word: ").upper()
        phoenatic_list = [phoenatic_dict[letter] for letter in user_word]

    except KeyError:
        print("Sorry, only letters in the alphabet phase")
        p=input("do you want to continue? YES or  NO:\n").upper()
        if p=='NO':
            generate_phoenatic=False
        else:
            generate_phoenatic=True

    else:
        print(phoenatic_list)
        p=input("do you want to continue? YES or  NO:\n").upper()
        if p=='NO':
            generate_phoenatic=False
        else:
            generate_phoenatic=True

