import random

def start_game():
    # I needed a refresher on how to use randint. 
    # Found answer on (https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/)
    # by Jackson Cooper
    num_to_guess = random.randint(1,10) 
    #print(num_to_guess) # Un-comment to show the number that needs to be guessed

    game_on = True

    num_of_player_guesses = []

    highscore = []
    
    play_again = ""

    welcome_msg = "Welcome to the Number Guessing Game!"

    print(len(welcome_msg) * "*")
    print(welcome_msg)
    print(len(welcome_msg) * "*")

    while game_on:

        try:
            player_guess = int(input("Guess a number: "))

        except ValueError:
            print("Sorry, but that's not a number. We're playing the NUMBER Guessing Game. ;)")

        else:
            if player_guess > 10 or player_guess < 1:
                print("The number {} is out of range.".format(player_guess))

            elif player_guess > num_to_guess:
                print("It's lower")
                num_of_player_guesses.append(player_guess)

            elif player_guess < num_to_guess:
                print("It's higher")
                num_of_player_guesses.append(player_guess)

            elif player_guess == num_to_guess:
                print("You got it! \n")
                num_of_player_guesses.append(player_guess)
                highscore += [len(num_of_player_guesses)]

                game_on = False

                if player_guess == num_to_guess and len(num_of_player_guesses) == 1:
                    print("Wow, lucky! It took you {} try.".format(len(num_of_player_guesses)))
                    
                else:
                    print("It took you {} tries.".format(len(num_of_player_guesses)))

                while not play_again == 'y' or not play_again == 'n':
                    
                    play_again = input("Would you like to play again? (Enter Yes/No): ").lower()

                    if play_again == "":
                        continue

                    if play_again[0] == "y":
                        highscore_msg = "The HIGHSCORE is {}".format(min(highscore))
                        print("")
                        print(highscore_msg)
                        print("-" * len(highscore_msg))
                        # Needed to know tow to clear a list
                        # found answer on (https://www.programiz.com/python-programming/methods/list/clear)
                        num_of_player_guesses.clear()
                        num_to_guess = random.randint(1,10)
                        #print(num_to_guess) # Un-comment to show the number that needs to be guessed next
                        game_on = True
                        break

                    elif play_again[0] == "n":
                        break

    print("")
    print("Thanks for playing! The game will be closing now.")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()