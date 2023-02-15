import random

ROCK = "rock"

# consider whether multiple functions might be better
# -- suggestions -- 

# no documentation


def play_game():

    # nice design with the list and choosing a random val from that list
    options = [ROCK, 'paper', 'scissors']
    computer_choice = random.choice(options)
    # consider using .lower() at the end of this line to avoid it in the if belo
w    user_choice = input("Enter your choice (rock/paper/scissors): ")

    while user_choice.lower() not in options:
        print("Invalid choice, please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ")

    print("You chose:", user_choice)
    print("The computer chose:", computer_choice)


    # suggest using constants for rock, paper, scissors
    if user_choice.lower() == computer_choice:
        print("It's a tie!")
    elif user_choice.lower() == ROCK and computer_choice == 'scissors':
        print("You win!")
    elif user_choice.lower() == 'paper' and computer_choice == 'rock':
        print("You win!")
    elif user_choice.lower() == 'scissors' and computer_choice == 'paper':
        print("You win!")
    else:
        print("The computer wins!")

play_game()
