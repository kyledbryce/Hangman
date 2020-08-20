def not_in_answer():
    global characters_already_used
    characters_already_used += latest_guess
    clear_screen()
    global guesses_remaining
    guesses_remaining -= 1
    show_current_hang_stage()


def clear_screen():
    for x in range(50):
        print()


def show_lives_remaining():
    if guesses_remaining == 1:
        print("You have " + str(guesses_remaining) + " life left.")
    else:
        print("You have " + str(guesses_remaining) + " lives left.")


def wrong_guess_ends_game():
    clear_screen()
    print(illustration_of_hanged_stage[6])
    print("Your guess was incorrect. The answer was " + case_sensitive_answer + ".")
    global game_concluded
    game_concluded = True


def ask_user_if_they_want_to_play_again():
    global choice, game_concluded, player_one_answer_not_yet_chosen, ON
    while not choice:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            choice = True
            game_concluded = False
            player_one_answer_not_yet_chosen = False
        elif play_again == "no":
            clear_screen()
            print("\n\n\nPROGRAM TERMINATED!!!\n\n\n")
            choice = True
            ON = False
        else:
            clear_screen()
            print("Please choose only Yes or No.\n")


def two_space_bar_invalid_input():
    clear_screen()
    show_current_hang_stage()
    print("Invalid choice. You typed at least 2 spaces consecutively.")
    show_lives_remaining()


def show_current_hang_stage():
    print(illustration_of_hanged_stage[6 - guesses_remaining] + "\n\n\n")


ON = True

while ON:
    clear_screen()
    print("TWO PLAYER HANGMAN\n")
    characters_not_used_yet = "abcdefghijklmnopqrstuvwxyz1234567890"
    characters_already_used = ""
    case_sensitive_answer = ""
    lower_case_answer = ""
    player_one_answer_not_yet_chosen = True
    while player_one_answer_not_yet_chosen:
        case_sensitive_answer = input("Player 1, please choose a : word, phrase, letter, number, equation or ANYTHING for Player 2 to guess: ")
        lower_case_answer = case_sensitive_answer.lower()
        if len(case_sensitive_answer) == 0:
            clear_screen()
            print("\nYou just hit the return key. Please only choose characters from " + characters_not_used_yet + "\n")
        elif case_sensitive_answer[0] == " ":
            clear_screen()
            print("\nYour chosen answer begins with a space. This is forbidden. Please only choose characters from " + characters_not_used_yet + "\n")
        else:
            for i in range(len(lower_case_answer)):
                if lower_case_answer[i] not in characters_not_used_yet and lower_case_answer[i] != " ":
                    clear_screen()
                    print("\nPlease only choose characters from " + characters_not_used_yet + "\n")
                else:
                    player_one_answer_not_yet_chosen = False
    clear_screen()
    print("You have 6 attempts to guess the correct characters, and you can only")
    print("guess the whole answer once. Here, a guess at the whole answer is defined as 2 valid characters or more.\n")
    array_of_revealed_concealed_characters = []
    allowed_special_characters = "!?£$%&@#()<>/*-+=^.,;:\"'"
    for i in range(len(lower_case_answer)):
        if lower_case_answer[i] == " ":
            array_of_revealed_concealed_characters.append(" ")
        elif lower_case_answer[i] in allowed_special_characters:
            array_of_revealed_concealed_characters.append(lower_case_answer[i])
        else:
            array_of_revealed_concealed_characters.append("_")
    view_of_revealed_concealed_characters = ""
    for i in range(len(array_of_revealed_concealed_characters)):
        view_of_revealed_concealed_characters += array_of_revealed_concealed_characters[i]
    array_of_revealed_concealed_characters = []
    game_concluded = False
    guesses_remaining = 6

    illustration_of_hanged_stage = [
        "",
        "O",
        " O\n |",
        "\O/\n |",
        "\O/\n |\n/ \ ",
        "========\n||     |\n||    <O>\n||     |\n||   _/_\_\n||     |\n||     |\n||     |\n||     |",
        "========\n||     |\n||     @\n||    /|\ \n||    / \ \n||\n||        /\n||       /\n||      /\n||     /",
        "<O__\n |\n/ \ "
        ]
    latest_guess = ""
    while latest_guess != lower_case_answer and view_of_revealed_concealed_characters != case_sensitive_answer and not game_concluded and guesses_remaining > 0:
        print("So far, the clue is: " + view_of_revealed_concealed_characters)
        print("Characters yet to be chosen: " + characters_not_used_yet)
        print("Characters already chosen: " + characters_already_used + "\n")
        latest_guess = input("\nPlease guess a character or guess the answer: ").lower()
        if len(latest_guess) == 1:
            if latest_guess in lower_case_answer and latest_guess != " ":
                if latest_guess in characters_not_used_yet:
                    characters_not_used_yet = characters_not_used_yet.replace(latest_guess, "")
                    characters_already_used += latest_guess
                    clear_screen()
                    show_current_hang_stage()
                    print("Well done, " + latest_guess.upper() + " is in the answer!\n")
                    show_lives_remaining()
                    array_of_revealed_concealed_characters = []
                    for i in range(len(lower_case_answer)):
                        if lower_case_answer[i] == latest_guess or lower_case_answer[i] in characters_already_used or lower_case_answer[i] in allowed_special_characters:
                            array_of_revealed_concealed_characters.append(case_sensitive_answer[i])
                        elif lower_case_answer[i] == " ":
                            array_of_revealed_concealed_characters.append(" ")
                        else:
                            array_of_revealed_concealed_characters.append("_")
                    view_of_revealed_concealed_characters = ""
                    for i in range(len(array_of_revealed_concealed_characters)):
                        view_of_revealed_concealed_characters += array_of_revealed_concealed_characters[i]
                else:
                    clear_screen()
                    show_current_hang_stage()
                    print(latest_guess + " has already been chosen. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    show_lives_remaining()
            else:
                if latest_guess in characters_not_used_yet:
                    if guesses_remaining > 2:
                        characters_not_used_yet = characters_not_used_yet.replace(latest_guess, "")
                        not_in_answer()
                        print("Unlucky, " + latest_guess.upper() + " is not in the answer.")
                        print("You have " + str(guesses_remaining) + " lives left.")
                    elif guesses_remaining < 2:
                        characters_not_used_yet = characters_not_used_yet.replace(latest_guess, "")
                        not_in_answer()
                        print("Unlucky, " + latest_guess.upper() + " was not in the answer. The")
                        print("answer was " + case_sensitive_answer + ". You have " + str(guesses_remaining) + " lives left.")
                    elif guesses_remaining == 2:
                        characters_not_used_yet = characters_not_used_yet.replace(latest_guess, "")
                        not_in_answer()
                        print("Unlucky, " + latest_guess.upper() + " is not in the answer.")
                        print("You have " + str(guesses_remaining) + " life left.\n")
                elif latest_guess in characters_already_used:
                    clear_screen()
                    show_current_hang_stage()
                    print(latest_guess + " has already been chosen, and it wasn't in")
                    print("the answer. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    show_lives_remaining()
                else:
                    clear_screen()
                    show_current_hang_stage()
                    print("Invalid character. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    show_lives_remaining()
        elif len(latest_guess) == len(lower_case_answer):
            if latest_guess == lower_case_answer:
                game_concluded = True
            elif "  " in latest_guess:
                two_space_bar_invalid_input()
            else:
                wrong_guess_ends_game()
        elif len(latest_guess) < 1:
            clear_screen()
            show_current_hang_stage()
            print("You didn't choose anything, and only hit the return key. Please")
            print("choose from the list of characters that are yet to be chosen.\n")
            show_lives_remaining()
        else:
            if "  " in latest_guess:
                two_space_bar_invalid_input()
            else:
                wrong_guess_ends_game()
    if latest_guess == lower_case_answer:
        clear_screen()
        print(illustration_of_hanged_stage[7])
        print("Well done, you guessed right! The answer is " + case_sensitive_answer + ".\n")
        choice = False
        ask_user_if_they_want_to_play_again()
    elif view_of_revealed_concealed_characters == case_sensitive_answer:
        clear_screen()
        print(illustration_of_hanged_stage[7])
        print("Well done, you guessed all the characters right!\nThe answer is " + case_sensitive_answer + ".\n")
        choice = False
        ask_user_if_they_want_to_play_again()
    else:
        print("\nI'm sorry, but you were hanged! Don't worry though, you can be resurrected.\n")
        choice = False
        ask_user_if_they_want_to_play_again()
