import random


def select_word():
    file = open('words.txt')
    words = file.readlines()
    my_word = 'a'
    while len(my_word) < 5:  # makes sure word is at least 5 letters long
        my_word = random.choice(words)

    my_word = str(my_word).strip("\n")
    # my_word = str(my_word).strip("\r")  # W I N D O W
    my_word = my_word.upper()

    return my_word


random_word = select_word()

total_lives = len(random_word)
str_total_lives = "Total lives:"
print(str_total_lives, total_lives)

game_board_list = []


def game_board(user_input_parameter):
    blanks = "_" * len(random_word)
    blanks_list_parameter = list(blanks)

    if len(game_board_list) == 0:
        game_board_list.extend(blanks_list_parameter)

    for i in range(0, len(random_word)):
        if user_input_parameter == random_word[i]:
            game_board_list[i] = random_word[i]

    return "                                   " + '  '.join(game_board_list)


while total_lives > 0:

    user_input = input("Enter a letter: ").upper()
    print(" ")
    print("--------------------------------------------------------")

    if user_input in list(random_word):

        print(str_total_lives, total_lives)
        print(" ")

        game_board_variable = game_board(user_input)
        print(game_board_variable)

        print(user_input, "is in the word.")
        print("--------------------------------------------------------")
        print(" ")

        if "_" in game_board_list:
            continue
        else:
            break

    else:
        total_lives -= 1
        print(str_total_lives, total_lives)
        print(" ")

        game_board_variable = game_board(user_input)
        print(game_board_variable)

        print(user_input, "is not in the word.")
        print("--------------------------------------------------------")
        print(" ")

        if "_" in game_board_list:
            continue
        else:
            break

if total_lives > 0:
    print("You won!")
else:
    print("You lost")
    print("The word was", random_word)
