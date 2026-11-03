import random
import super_guesser 

taunts = ['Back for more eh?', 'Ready to lose?!', "Don't you ever give up?", 'Maybe a bit quicker this time!']

wants_to_play = True

while(wants_to_play):
    max_value = input("Enter the maximum possible value for the guessing game: ")
    mystery_number = super_guesser.generate_mystery_number(max_value)
    
    # Invalid data, skip the loop and make the user try again
    if not mystery_number:
        continue

    print(f"I'm thinking of a number between 1 and {max_value}.")

    guess_result = None

    while(guess_result != "="):
        guess = input(f"Enter a guess between 1 and {max_value}): ")

        guess_result = super_guesser.process_player_guess(guess, mystery_number)

        # Invalid data, skip the loop and make the user try again
        if not guess_result:
            continue
        
        if guess_result == '-':
            print("Your guess is too low.")
        elif guess_result == '+':
            print("Your guess is too high")
        elif guess_result == "=":
            print(f"Correct, I was thinking of the nubmer {mystery_number}!")
    
    play_again = None
    while(play_again != 'y' and play_again != 'n'):
        play_again = input("Would you like to play again? (y/n): ")
        if play_again == 'n':
            print("Thanks for playing!")
            wants_to_play = False
        elif play_again == 'y':
            print(f"{random.choice(taunts)}")
        