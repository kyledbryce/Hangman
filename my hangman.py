

def clear_screen():
    for i in range(50):
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
    global has_the_game_concluded
    has_the_game_concluded = True


def ask_user_if_they_want_to_play_again():
    global player_chose_yes_or_no, has_the_game_concluded, valid_answer_chosen, ON
    while not player_chose_yes_or_no:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            player_chose_yes_or_no = True
            has_the_game_concluded = False
            valid_answer_chosen = True
        elif play_again == "no":
            clear_screen()
            print("\n\n\nPROGRAM TERMINATED!!!\n\n\n")
            player_chose_yes_or_no = True
            ON = False
        else:
            clear_screen()
            print("Please choose only Yes or No.\n")


def two_space_bar_invalid_input_error_message():
    clear_screen()
    show_current_hang_stage()
    print("Invalid choice. You typed at least 2 spaces consecutively.")
    show_lives_remaining()


def show_current_hang_stage():
    print(illustration_of_hanged_stage[6 - guesses_remaining] + "\n\n\n")


def update_used_and_notused_characters_lists_and_minus_a_life():
    global characters_not_used_yet
    global characters_already_used
    global guesses_remaining
    characters_not_used_yet = characters_not_used_yet.replace(latest_guess, "")
    characters_already_used += latest_guess
    clear_screen()
    guesses_remaining -= 1
    return characters_already_used, guesses_remaining


def create_array_of_underscores_equivelent_to_answer():
    global array_of_revealed_concealed_characters
    array_of_revealed_concealed_characters = []
    for character in range(len(lower_case_answer)):
        if lower_case_answer[character] == " ":
            array_of_revealed_concealed_characters.append(" ")
        elif lower_case_answer[character] in allowed_special_characters:
            array_of_revealed_concealed_characters.append(lower_case_answer[character])
        else:
            array_of_revealed_concealed_characters.append("_")


def convert_array_into_a_word():
    global view_of_revealed_concealed_characters, array_of_revealed_concealed_characters
    for character in range(len(array_of_revealed_concealed_characters)):
        view_of_revealed_concealed_characters += array_of_revealed_concealed_characters[character]
    return view_of_revealed_concealed_characters


def player_one_must_choose_valid_answer():
    global case_sensitive_answer, lower_case_answer, valid_answer_chosen
    while not valid_answer_chosen:
        case_sensitive_answer = input("Player 1, please choose a : word, phrase, letter, number, equation or ANYTHING for Player 2 to guess: ")
        lower_case_answer = case_sensitive_answer.lower()
        if len(case_sensitive_answer) == 0:
            clear_screen()
            print("\nYou just hit the return key. Please only choose characters from " + characters_not_used_yet + "\n")
        elif case_sensitive_answer[0] == " ":
            clear_screen()
            print("\nYour chosen answer begins with a space. This is forbidden. Please only choose characters from " + characters_not_used_yet + "\n")
        elif "  " in case_sensitive_answer:
            clear_screen()
            print("you are only allowed to use one space between each word/number. Please only choose characters from " + characters_not_used_yet + "\n")
        else:
            for i, any_characters in enumerate(lower_case_answer):
                valid_answer_chosen = True
                if any_characters not in characters_not_used_yet and any_characters not in allowed_special_characters and any_characters != " ":
                    clear_screen()
                    print("\nPlease only choose characters from " + characters_not_used_yet + "\n")
                    valid_answer_chosen = False
                    break
            if valid_answer_chosen:
                for i, any_characters in enumerate(characters_not_used_yet):
                    if any_characters not in lower_case_answer:
                        valid_answer_chosen = False
                    else:
                        valid_answer_chosen = True
                        break
                if not valid_answer_chosen:
                    print("Your choice consists of only special characters. Please include at least")
                    print("one valid character from the list " + characters_not_used_yet)


def update_array_of_concealed_revealed_characters():
    for i, any_characters in enumerate(lower_case_answer):
        if any_characters == latest_guess or any_characters in characters_already_used or any_characters in allowed_special_characters:
            array_of_revealed_concealed_characters.append(case_sensitive_answer[i])
        elif any_characters == " ":
            array_of_revealed_concealed_characters.append(" ")
        else:
            array_of_revealed_concealed_characters.append("_")


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


ON = True
while ON:
    clear_screen()
    print("TWO PLAYER HANGMAN\n")
    characters_not_used_yet = "abcdefghijklmnopqrstuvwxyz1234567890"
    characters_already_used = ""
    allowed_special_characters = "!?£$%&@#()<>/*-+=^.,;:\"'"
    case_sensitive_answer = ""
    lower_case_answer = ""
    valid_answer_chosen = False
    player_one_must_choose_valid_answer()
    clear_screen()
    print("You have 6 attempts to guess the correct characters, and you can only")
    print("guess the whole answer once. Here, a guess at the whole answer is")
    print("defined as 2 valid characters or more, and must include all/any")
    print("punctuation.\n")
    create_array_of_underscores_equivelent_to_answer()
    view_of_revealed_concealed_characters = ""
    convert_array_into_a_word()
    array_of_revealed_concealed_characters = []
    has_the_game_concluded = False
    guesses_remaining = 6
    latest_guess = ""

    while latest_guess != lower_case_answer and view_of_revealed_concealed_characters != case_sensitive_answer and not has_the_game_concluded and guesses_remaining > 0:
        print("So far, the clue is: " + view_of_revealed_concealed_characters)
        print("Characters yet to be chosen: " + characters_not_used_yet)
        print("Characters already chosen: " + characters_already_used + "\n")
        latest_guess = input("\nPlease guess a character or guess the answer: ").lower()

        if len(latest_guess) == 1:
            if latest_guess == " ":
                clear_screen()
                show_current_hang_stage()
                print("You hit space bar. This is not a valid guess. Please only")
                print("choose from the list of characters yet to be chosen.")
            elif latest_guess in allowed_special_characters:
                clear_screen()
                show_current_hang_stage()
                print(latest_guess + " has already been revealed by default. Please only")
                print("choose from the list of characters yet to be chosen.")
            elif latest_guess in lower_case_answer:
                if latest_guess in characters_not_used_yet:
                    characters_not_used_yet = characters_not_used_yet.replace(latest_guess, "")
                    characters_already_used += latest_guess
                    clear_screen()
                    show_current_hang_stage()
                    print("Well done, " + latest_guess.upper() + " is in the answer!\n")
                    show_lives_remaining()
                    array_of_revealed_concealed_characters = []
                    update_array_of_concealed_revealed_characters()
                    view_of_revealed_concealed_characters = ""
                    convert_array_into_a_word()
                else:
                    clear_screen()
                    show_current_hang_stage()
                    print(latest_guess + " has already been chosen. Please only choose from the")
                    print("list of characters that are yet to be chosen.\n")
                    show_lives_remaining()

            else:
                if latest_guess in characters_not_used_yet:
                    if guesses_remaining > 2:
                        update_used_and_notused_characters_lists_and_minus_a_life()
                        show_current_hang_stage()
                        print("Unlucky, " + latest_guess.upper() + " is not in the answer.")
                        print("You have " + str(guesses_remaining) + " lives left.")
                    elif guesses_remaining < 2:
                        update_used_and_notused_characters_lists_and_minus_a_life()
                        show_current_hang_stage()
                        print("Unlucky, " + latest_guess.upper() + " was not in the answer. The")
                        print("answer was " + case_sensitive_answer + ". You have " + str(guesses_remaining) + " lives left.")
                    elif guesses_remaining == 2:
                        update_used_and_notused_characters_lists_and_minus_a_life()
                        show_current_hang_stage()
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

        elif len(latest_guess) < 1:
            clear_screen()
            show_current_hang_stage()
            print("You didn't choose anything, and only hit the return key. Please")
            print("choose from the list of characters that are yet to be chosen.\n")
            show_lives_remaining()
        else:
            if latest_guess == lower_case_answer:
                has_the_game_concluded = True
            elif "  " in latest_guess:
                two_space_bar_invalid_input_error_message()
            else:
                wrong_guess_ends_game()

    if latest_guess == lower_case_answer:
        clear_screen()
        print(illustration_of_hanged_stage[7])
        print("Well done, you guessed right! The answer is " + case_sensitive_answer + ".\n")
        player_chose_yes_or_no = False
        ask_user_if_they_want_to_play_again()
    elif view_of_revealed_concealed_characters == case_sensitive_answer:
        clear_screen()
        print(illustration_of_hanged_stage[7])
        print("Well done, you guessed all the characters right!\nThe answer is " + case_sensitive_answer + ".\n")
        player_chose_yes_or_no = False
        ask_user_if_they_want_to_play_again()
    else:
        print("\nI'm sorry, but you were hanged! Don't worry though, you can be resurrected.\n")
        player_chose_yes_or_no = False
        ask_user_if_they_want_to_play_again()
