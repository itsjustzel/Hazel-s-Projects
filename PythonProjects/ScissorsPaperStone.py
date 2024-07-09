import random

def main():
    win = False
    while not win:
        response = input("Rock!Paper!Scissors!Shoot!(Give your response here)").lower()
        choice = random.choice(["scissors", "paper", "rock"])

        if response == choice:
            print("Try again!")
        else:
            if response == "scissors" and choice == "paper":
                print("You won! Winner winner chicken dinner!")
                win = True
            elif response == "paper" and choice == "rock":
                print("You won! Winner winner chicken dinner!")
                win = True
            elif response == "rock" and choice == "scissors":
                print("You won! Winner winner chicken dinner!")
                win = True
            elif response == "rock" and choice == "paper":
                print("You lost! Loser!")
            elif response == "scissors" and choice == "rock":
                print("You lost! Loser!")
            elif response == "paper" and choice == "scissors":
                print("You lost! Loser!")
            else:
                print("Are you sure you are playing the right game? ")

if __name__ == "__main__":
    main()