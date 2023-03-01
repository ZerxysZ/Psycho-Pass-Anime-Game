import random

# Some unique string (and suspicious) messages
welcome_message = "Welcome to my number guessing game Mr. Rai! 🤭"
user_guess_message = "Hmmmm... I'm thinking of a number between 1 and 100. Can you guess it? 🧐"
computer_guess_message = "Let's play a game! Think of a number between 1 and 100, and I'll try to guess it. 😇"
win_messages = [
    "Congratulations Mr. Rai! You guessed the number. ╮ (. ❛ ᴗ ❛.) ╭",
    "Great job Mr. Rai! You got it right! ᕦʕ •ᴥ•ʔᕤ",
    "Wow Mr. Rai, you're really good at this game! You guessed it! 🥴",
    "Oh la la, Great heavens! Mr. Rai, you never fail to exceed my expectations... You guessed the number correctly 😍"
]
computer_win_messages = [
    "Skill issue... I win! Try harder next time Mr. Rai",
    "AI continues to develop exponentially considering it will take over the world one day... Mr. Rai, You never stood a chance against me!",
    "Hooray Mr. Rai! I won the game!!!",
    "Mr. Rai, get better, get good, you need to improve at the game, it seems like you lack the capability of beating ME! (i'm joking plz dont deduct marks 😔)"
    ]
invalid_input_message = "Invalid input. Please enter a valid option."

# Define the user guess game
def user_guess_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    # Display the welcome message and instructions
    print(welcome_message)
    print(user_guess_message)
    # Start the guessing loop
    while True:
        # Prompt the user for a guess
        user_guess = input("Enter your guess: ")
        # Check if the input is a valid integer
        if user_guess.isdigit():
            user_guess = int(user_guess)
            # Compare the user's guess to the number to be guessed
            if user_guess < number_to_guess:
                print("Your guess is too low. Try again.")
            elif user_guess > number_to_guess:
                print("Your guess is too high. Try again.")
            else:
                # If the user guesses the number, display a random win message and exit the loop
                print(random.choice(win_messages))
                break
        else:
            # If the input is not a valid integer, display an error message
            print("Invalid input. Please enter a number.")

# Define the computer guess game
def computer_guess_game():
    # Display the welcome message and instructions
    print(welcome_message)
    print(computer_guess_message)
    # Initialize the range of possible numbers and the number of tries
    min_number = 1
    max_number = 100
    tries = 0
    # Start the guessing loop
    while True:
        # Generate a random guess within the range of possible numbers
        computer_guess = random.randint(min_number, max_number)
        # Prompt the user for feedback
        user_feedback = input(f"My guess is {computer_guess}. Is it too high (h), too low (l), or correct (c)? ")
        # Check the user's feedback and adjust the range of possible numbers accordingly
        if user_feedback == "h":
            max_number = computer_guess - 1
        elif user_feedback == "l":
            min_number = computer_guess + 1
        elif user_feedback == "c":
            # If the computer guesses the number, display a random win message and exit the loop
            print(random.choice(computer_win_messages))
            print(f"I guessed your number in {tries} tries.")
            break
        else:
            # If the user enters an invalid input, display an error message
            print(invalid_input_message)
        # Increment the number of tries
        tries += 1

# Start the main loop
while True:
    # Prompt the user for which game to play
    game_choice = input("Which game would you like to play? Enter user guess, computer guess, or type q to quit: ")
    if game_choice == "user guess":
        user_guess_game()
    elif game_choice == "computer guess":
        computer_guess_game()
    elif game_choice == "q":
        break
    else:
        print("Invalid input. Please enter user guess, computer guess, or q.")
