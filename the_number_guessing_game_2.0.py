import random
import csv


def decorated_text(msg, deco, deco_2):
    message = msg
    decoration = deco
    decoration_2 = deco_2

    print(decoration * (len(message) + 4))
    print(decoration_2 + " " + message + " " + decoration_2)
    print(decoration * (len(message) + 4))


def instructions():
    instruction_choice = "placeholder"

    instructions_text = """Instructions:
Type a number between 1 and 10. 
The game will give you a hint
if the number is lower or higher
than the number you guessed.

The number will never be
0 or a negative number.
Simultaneously the number
will never be higher than 10."""

    misunderstood = """I did not catch that.
Did you want to see the
instructions to the game?
Answer 'yes' or 'no'"""

    yes_list = ["y"]

    while not instruction_choice == "y" and not instruction_choice == "n":

        instruction_choice = input("Want to read the instructions? ").lower()

        if instruction_choice == "":
            continue

        if instruction_choice[0] == "y":
            print()
            print(instructions_text)
            print()
            break

        elif instruction_choice[0] == "n":
            print()
            break

        else:
            print()
            print(misunderstood)
            print()


def replay():
    play_again = "placeholder"

    while not play_again == "y" and not play_again == "n":

        play_again = input("Would you like to play again? ")
        print()

        if play_again == "":
            continue

        if play_again[0] == "y":
            return True

        elif play_again[0] == "n":
            return False


def random_number():
    number_to_guess = random.choice(range(1,11))
    # print(number_to_guess)
    print()
    return number_to_guess


def csv_file_creator():
    with open("highscore_file.csv", "w") as csvfile:
        fieldnames = ["score"]
        scorewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        scorewriter.writeheader()


def highscore_reader():
    try:
        score_list = []

        with open("highscore_file.csv", mode="r", newline="") as csvfile:
            scorereader = csv.DictReader(csvfile)
            rows = list(scorereader)

            for row in rows:
                score_list.append(row["score"])

        if len(score_list) < 1:
            score_list.append(10)

        return score_list

    except FileNotFoundError:
        csv_file_creator()


def highscore_writer(score):
    with open("highscore_file.csv", "a") as csvfile:
        fieldnames = ["score"]
        scorewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        scorewriter.writerow({
            "score": score
        })


def highscore_message():
    print("HIGH SCORE: ", min(highscore_reader()))
    print()


def guess_tracker(number):
    if number == 1:
        print("WOW! You got it on your first guess. ")
        print()
    else:
        print("It took you", number, "guesses.")
        print()


def the_number_guessing_game():
    
    highscore_reader()

    number_to_guess = random_number()

    score_count = 0

    player_guess = ''

    game_on = True

    decorated_text("The Number Guessing Game", "*", "*")

    instructions()

    highscore_message()

    while game_on:

        try:
            player_guess = int(input("Guess a number from 1 to 10: "))

        except ValueError:
            print("That's not a number, dum-dum. Try Again.")
            print()

        else:
            if player_guess == 999:
                break

            if player_guess < 1:
                print("Anything lower than 1 is out of range.")
                print()

            elif player_guess > 10:
                print("Anything higher than 10 is out of range.")
                print()

            if player_guess == number_to_guess:
                score_count += 1
                print("You guessed it!")
                print()
                guess_tracker(score_count)
                game_on = replay()
                if game_on == True:
                    highscore_writer(score_count)
                    number_to_guess = random_number()
                    score_count = 0
                    highscore_message()

            elif player_guess < number_to_guess:
                score_count += 1
                print("Higher.")
                print()

            elif player_guess > number_to_guess:
                score_count += 1
                print("Lower.")
                print()

    highscore_writer(score_count)
    highscore_message()
    decorated_text("Game Over", "-", "|")


if __name__ == "__main__":
    the_number_guessing_game()
