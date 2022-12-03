from random import randint
import os
from time import sleep


class bcolors:  # noqa
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# works like this "print(f"{bcolors.BLUE} Hello, World!{bcolors.END}")"


def list_maker(string):
    string_to_list = []
    string_to_list[:0] = string
    return string_to_list


def word_picker():
    list_of_words = ["parameter", "wonder", "muscle", "established", "aluminium", "communist", "application",
                     "pneumonia", "chorus", "grave", "dialogue", "feather", "unpleasant", "urgency", "fascinate",
                     "discipline", "beam", "drive"]
    random_value = randint(0, len(list_of_words) - 1)
    final_word = list_of_words[random_value]
    return final_word


def main(play_mode_selector):
    lives = 6
    empty_list = []
    bad_guess = []
    if play_mode_selector.lower() == "m":
        final_word = input("Enter the word! ")
        os.system('cls')
    else:
        final_word = word_picker()
    final_word_list = list_maker(final_word)
    for char in range(len(final_word_list)):
        empty_list.append("_")
        if final_word_list[char] == " ":
            empty_list[char] = " "
    while True:
        correctness = 0
        print(empty_list)
        print(f"Lives: {lives}")
        if empty_list == final_word_list:
            print(f"{bcolors.GREEN}You win!")
            sleep(5)
            exit()
        print(f"Wrong characters:\n{bad_guess}")
        user_input = input("Guess a letter! ")
        if len(user_input) == 1:
            for chars in range(len(empty_list)):
                if user_input == final_word_list[chars]:
                    empty_list[chars] = user_input
                    correctness = 1
            if correctness == 0:
                for chars in range(len(bad_guess)):
                    if bad_guess[chars] == user_input:
                        print(f"{bcolors.YELLOW}You already tried that! It is incorrect!{bcolors.END}")
                        correctness = 1
                if correctness == 0:
                    lives -= 1
                    print(f"{bcolors.RED}The character {user_input} is incorrect!{bcolors.END}")
                    bad_guess.append(user_input)
            if correctness == 1:
                print(f"{bcolors.GREEN}Character {user_input} is correct!{bcolors.END}")
        else:
            print("Invalid string!")
        if lives == 0:
            print(f"{bcolors.RED}You died! The word was {final_word} and you only got this far:\n{empty_list}")
            sleep(10)
            exit()
        sleep(2)
        os.system('cls')


if __name__ == '__main__':
    play_mode = input("Single- or multiplayer? (m/s) ")
    main(play_mode)
