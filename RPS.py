import random

while True:
    user_action = input("Enter your choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nyou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"both players have selected {user_action}. Its a Tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You have Won!")
        else:
            print("Paper Covers Rock, You Lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper Covers Rock, You Win!")
        else:
            print("Paper Cuts Scissors, You Lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
         print("Scissors Cuts Paper, You Win!")
        else:
            print("Rock Smashes Scissors, You Lose!")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
            
    

    
        




    


    
