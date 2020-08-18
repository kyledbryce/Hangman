def not_in_answer():
    global already_chosen
    already_chosen += guess
    fifty_lines()
    global guesses_remaining
    guesses_remaining -= 1
    print(hang_stage[6 - guesses_remaining] + "\n\n\n")


def fifty_lines():
    for x in range(50):
        print()


def lives():
    if guesses_remaining == 1:
        print("You have " + str(guesses_remaining) + " life left.")
    else:
        print("You have " + str(guesses_remaining) + " lives left.")


def wrong_guess():
    fifty_lines()
    print(hang_stage[6])
    print(text[4])
    global game_over
    game_over = True


def while_not_choice():
    global choice, game_over, answer_limit, ON
    while not choice:
        play_again = input(text[3]).lower()
        if play_again == "yes":
            choice = True
            game_over = False
            answer_limit = False
        elif play_again == "no":
            fifty_lines()
            print(text[1])
            choice = True
            ON = False
        else:
            fifty_lines()
            print(text[2])


def invalid():
    fifty_lines()
    print(hang_stage[6 - guesses_remaining] + "\n\n\n")
    print("Invalid choice. You typed at least 2 spaces consecutively.")
    lives()


ON = True
while ON:
    fifty_lines()
    print("TWO PLAYER HANGMAN\n")
    yet_to_be_chosen = "abcdefghijklmnopqrstuvwxyz1234567890!?£$%&@#()<>/*-+=^.,;:\"'"
    already_chosen = ""
    answer_limit = False
    answer_limit_count = 0
    raw_answer = ""
    answer = ""
    while not answer_limit:
        raw_answer = input("Player 1, please choose a secret word, phrase or letter for Player 2 to guess: ")
        answer = raw_answer.lower()
        for i in range(len(answer)):
            if answer[i] not in yet_to_be_chosen and answer[i] != " ":
                answer_limit_count += 1
        if answer_limit_count == 0:
            answer_limit = True
        else:
            print("\nPlease only choose characters from " + yet_to_be_chosen + "\n")
            answer_limit_count = 0
    fifty_lines()
    print("You have 6 attempts to guess the correct characters, and you can only")
    print("guess the word(s) once. Here, a word is defined as 2 letters or more.\n")
    guess_list = []
    for i in range(len(answer)):
        if answer[i] == " ":
            guess_list.append(" ")
        else:
            guess_list.append("_")
    guess_update = ""
    for i in range(len(guess_list)):
        guess_update += guess_list[i]
    guess = ""
    guess_list = []
    game_over = False
    guesses_remaining = 6

    hang_stage = [
        "",
        "O",
        " O\n |",
        "\O/\n |",
        "\O/\n |\n/ \ ",
        "========\n||     |\n||    <O>\n||     |\n||   _/_\_\n||     |\n||     |\n||     |\n||     |",
        "========\n||     |\n||     @\n||    /|\ \n||    / \ \n||\n||        /\n||       /\n||      /\n||     /",
        "<O__\n |\n/ \ "
        ]

    text = [
        "\nI'm sorry, but you were hanged! Don't worry though, you can be resurrected.\n",
        "\n\n\nPROGRAM TERMINATED!!!\n\n\n",
        "Please choose only Yes or No.\n",
        "Would you like to play again? (yes/no): ",
        "Your guess was incorrect. The answer was " + raw_answer + "."
    ]

    while guess != answer and guess_update != raw_answer and not game_over and guesses_remaining > 0:
        print("So far, the clue is: " + guess_update)
        print("Characters yet to be chosen: " + yet_to_be_chosen)
        print("Characters already chosen: " + already_chosen + "\n")
        guess = input("\nPlease guess a character or guess the word(s): ").lower()
        print()
        if len(guess) == 1:
            if guess in answer and guess != " ":
                if guess in yet_to_be_chosen:
                    yet_to_be_chosen = yet_to_be_chosen.replace(guess, "")
                    already_chosen += guess
                    fifty_lines()
                    print(hang_stage[6 - guesses_remaining] + "\n\n\n")
                    print("Well done, " + guess.upper() + " is in the answer!\n")
                    lives()
                    guess_list = []
                    for i in range(len(answer)):
                        if answer[i] == guess or answer[i] in already_chosen:
                            guess_list.append(raw_answer[i])
                        elif answer[i] == " ":
                            guess_list.append(" ")
                        else:
                            guess_list.append("_")
                    guess_update = ""
                    for i in range(len(guess_list)):
                        guess_update += guess_list[i]
                else:
                    fifty_lines()
                    print(hang_stage[6 - guesses_remaining] + "\n\n\n")
                    print(guess + " has already been chosen. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    lives()
            else:
                if guess in yet_to_be_chosen:
                    if guesses_remaining > 2:
                        yet_to_be_chosen = yet_to_be_chosen.replace(guess, "")
                        not_in_answer()
                        print("Unlucky, " + guess.upper() + " is not in the answer.")
                        print("You have " + str(guesses_remaining) + " lives left.")
                    elif guesses_remaining < 2:
                        yet_to_be_chosen = yet_to_be_chosen.replace(guess, "")
                        not_in_answer()
                        print("Unlucky, " + guess.upper() + " was not in the answer. The")
                        print("answer was " + raw_answer + ". You have " + str(guesses_remaining) + " lives left.")
                    elif guesses_remaining == 2:
                        yet_to_be_chosen = yet_to_be_chosen.replace(guess, "")
                        not_in_answer()
                        print("Unlucky, " + guess.upper() + " is not in the answer.")
                        print("You have " + str(guesses_remaining) + " life left.\n")
                elif guess in already_chosen:
                    fifty_lines()
                    print(hang_stage[6 - guesses_remaining] + "\n\n\n")
                    print(guess + " has already been chosen, and it wasn't in")
                    print("the answer. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    lives()
                else:
                    fifty_lines()
                    print(hang_stage[6 - guesses_remaining] + "\n\n\n")
                    print("Invalid character. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    lives()
        elif len(guess) == len(answer):
            if guess == answer:
                game_over = True
            elif "  " in guess:
                invalid()
            else:
                wrong_guess()
        elif len(guess) < 1:
            fifty_lines()
            print(hang_stage[6 - guesses_remaining] + "\n\n\n")
            print("You didn't choose anything, and only hit the return key. Please")
            print("choose from the list of characters that are yet to be chosen.\n")
            lives()
        else:
            if "  " in guess:
                invalid()
            else:
                wrong_guess()
    if guess == answer:
        fifty_lines()
        print(hang_stage[7])
        print("Well done, you guessed right! The answer is " + raw_answer + ".\n")
        choice = False
        while_not_choice()
    elif guess_update == raw_answer:
        fifty_lines()
        print(hang_stage[7])
        print("Well done, you guessed all the characters right!\nThe answer is " + raw_answer + ".\n")
        choice = False
        while_not_choice()
    else:
        print(text[0])
        choice = False
        while_not_choice()
