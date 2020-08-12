# Hangman

ON = True
while ON:
    for i in range(50):
        print()
    print("TWO PLAYER HANGMAN\n")
    answer = input("Player 1, please choose a secret word for Player 2 to guess: ")
    for i in range(50):
        print()
    print("You have 6 attempts to guess the correct letters, and you can only")
    print("guess the word once. Here, a word is defined as 2 letters or more.\n")
    guess = ""
    guess_update = ""
    guess_list = []
    game_over = False
    number_of_goes = 6
    yet_to_be_chosen = "abcdefghijklmnopqrstuvwxyz'-"
    already_chosen = ""

    stage = [
        "",
        "O",
        " O\n |",
        "\O/\n |",
        "\O/\n |\n/ \ ",
        "========\n||     |\n||    <O>\n||     |\n||   _/_\_\n||     |\n||     |\n||     |\n||     |",
        "========\n||     |\n||     @\n||    /|\ \n||    / \ \n||\n||        /\n||       /\n||      /\n||     /",
        "<O__\n |\n/ \ "
        ]

    while guess.lower() != answer.lower() and not game_over and number_of_goes > 0 and guess_update.lower() != answer.lower():
        if len(guess_update) > 0:
            print("So far, the clue is: " + guess_update)
        print("Letters yet to be chosen: " + yet_to_be_chosen)
        if len(already_chosen) > 0:
            print("Letters already chosen: " + already_chosen + "\n")
        guess = input("\nPlease guess a letter or guess the word: ")
        print()
        if len(guess) == 1:
            if guess.lower() in answer.lower():
                if guess.lower() in yet_to_be_chosen:
                    yet_to_be_chosen = yet_to_be_chosen.replace(guess.lower(), "")
                    already_chosen += guess.lower()
                    for i in range(50):
                        print()
                    print(stage[6 - number_of_goes] + "\n\n\n")
                    print("Well done, " + guess.lower() + " is in the word!\n")
                    if number_of_goes == 1:
                        print("You have " + str(number_of_goes) + " life left.")
                    else:
                        print("You have " + str(number_of_goes) + " lives left.")
                    guess_list = []
                    for i in range(len(answer)):
                        if answer[i] == guess.lower():
                            guess_list.append(guess.lower())
                        elif answer[i].lower() in already_chosen:
                            guess_list.append(answer[i].lower())
                        else:
                            guess_list.append("_")
                    guess_update = "".lower()
                    for i in range(len(guess_list)):
                        guess_update += guess_list[i].lower()
                elif guess.lower() in already_chosen:
                    for i in range(50):
                        print()
                    print(stage[6 - number_of_goes] + "\n\n\n")
                    print(guess + " has already been chosen. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    if number_of_goes == 1:
                        print("You have " + str(number_of_goes) + " life left.")
                    else:
                        print("You have " + str(number_of_goes) + " lives left.")
            else:
                if guess.lower() in yet_to_be_chosen and number_of_goes > 2:
                    yet_to_be_chosen = yet_to_be_chosen.replace(guess.lower(), "")
                    already_chosen += guess.lower()
                    for i in range(50):
                        print()
                    number_of_goes -= 1
                    print(stage[6 - number_of_goes] + "\n\n\n")
                    print("Unlucky, " + guess.lower() + " is not in the word. You have " + str(number_of_goes) + " lives left.")
                elif number_of_goes < 2:
                    yet_to_be_chosen = yet_to_be_chosen.replace(guess.lower(), "")
                    already_chosen += guess.lower()
                    for i in range(50):
                        print()
                    number_of_goes -= 1
                    print(stage[6 - number_of_goes] + "\n\n\n")
                    print("Unlucky, " + guess.lower() + " is not in the word. The")
                    print("answer was " + answer + ". You have " + str(number_of_goes) + " lives left.")
                elif guess.lower() in yet_to_be_chosen and number_of_goes == 2:
                    yet_to_be_chosen = yet_to_be_chosen.replace(guess.lower(), "")
                    already_chosen += guess.lower()
                    for i in range(50):
                        print()
                    number_of_goes -= 1
                    print(stage[6 - number_of_goes] + "\n\n\n")
                    print("Unlucky, " + guess.lower() + " is not in the word. You have " + str(number_of_goes) + " life left.\n")
                elif guess.lower() in already_chosen:
                    for i in range(50):
                        print()
                    print(stage[6 - number_of_goes] + "\n\n\n")
                    print(guess + " has already been chosen, and it wasn't in")
                    print("the word. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    if number_of_goes == 1:
                        print("You have " + str(number_of_goes) + " life left.")
                    else:
                        print("You have " + str(number_of_goes) + " lives left.")
                else:
                    for i in range(50):
                        print()
                    print(stage[6 - number_of_goes] + "\n\n\n")
                    print("Invalid character. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    if number_of_goes == 1:
                        print("You have " + str(number_of_goes) + " life left.")
                    else:
                        print("You have " + str(number_of_goes) + " lives left.")
        elif len(guess) == len(answer):
            if guess.lower() == answer.lower():
                game_over = True
            else:
                for i in range(50):
                    print()
                print(stage[6])
                print("The word you guessed is incorrect. The answer was " + answer + ".")
                game_over = True
        elif len(guess) < 1:
            for i in range(50):
                print()
            print(stage[6 - number_of_goes] + "\n\n\n")
            print("You didn't choose anything, and only hit the space bar. Please")
            print("choose from the list of characters that are yet to be chosen.\n")
            if number_of_goes == 1:
                print("You have " + str(number_of_goes) + " life left.")
            else:
                print("You have " + str(number_of_goes) + " lives left.")
        else:
            for i in range(50):
                print()
            print(stage[6])
            print("The word you guessed is incorrect. The answer was " + answer + ".")
            game_over = True

    if guess.lower() == answer.lower():
        for i in range(50):
            print()
        print(stage[7])
        print("Well done, you guessed the word right! The answer was " + answer + ".\n")
        choice = False
        while not choice:
            Continue = input("Would you like to play again? (yes/no): ")
            if Continue.lower() == "yes":
                answer = ""
                guess = ""
                guess_update = ""
                guess_list = []
                number_of_goes = 6
                yet_to_be_chosen = "abcdefghijklmnopqrstuvwxyz'-"
                already_chosen = ""
                choice = True
                game_over = False
            elif Continue.lower() == "no":
                for i in range(50):
                    print()
                print("\n\n\nPROGRAM TERMINATED!!!\n\n\n")
                choice = True
                ON = False
            else:
                for i in range(50):
                    print()
                print("Please choose only Yes or No.\n")
    elif guess_update.lower() == answer.lower():
        for i in range(50):
            print()
        print(stage[7])
        print("Well done, you guessed all the letters right!\nThe answer was " + answer + ".\n")
        choice = False
        while not choice:
            Continue = input("Would you like to play again? (yes/no): ")
            if Continue.lower() == "yes":
                answer = ""
                guess = ""
                guess_update = ""
                guess_list = []
                number_of_goes = 6
                yet_to_be_chosen = "abcdefghijklmnopqrstuvwxyz'-"
                already_chosen = ""
                choice = True
                game_over = False
            elif Continue.lower() == "no":
                for i in range(50):
                    print()
                print("\n\n\nPROGRAM TERMINATED!!!\n\n\n")
                choice = True
                ON = False
            else:
                for i in range(50):
                    print()
                print("Please choose only Yes or No.\n")
    else:
        print("\nI'm sorry, but you were hanged! Don't worry though, you can be resurrected.\n")
        choice = False
        while not choice:
            Continue = input("Would you like to play again? (yes/no): ")
            if Continue.lower() == "yes":
                answer = ""
                guess = ""
                guess_update = ""
                guess_list = []
                number_of_goes = 6
                yet_to_be_chosen = "abcdefghijklmnopqrstuvwxyz'-"
                already_chosen = ""
                choice = True
                game_over = False
            elif Continue.lower() == "no":
                for i in range(50):
                    print()
                print("\n\n\nPROGRAM TERMINATED!!!\n\n\n")
                choice = True
                ON = False
            else:
                for i in range(50):
                    print()
                print("Please choose only Yes or No.\n")
