from random import randint

'''
Scissors cuts paper
lizard eats paper
paper covers rock
Spock vaporizes rock
rock crushes lizard
scissors decapitates lizard
lizard poisons Spock
paper disproves Spock
Spock smashes scissors
rock crushes scissors
'''
def main():
    #create a list of play options
    t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    #assign a random play to the computer
    computer = t[randint(0,4)]

    #set player to False
    player = False

    while player == False:
    #set player to True
        player = input("Rock, Paper, Scissors, Lizard, Spock?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            elif computer == "Spock":
                print("You lose!", computer, "vaporises", player)
            else:
                print("You win!", player, "crushes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            elif computer == "Lizard":
                print("You lose!", computer, "eats", player)
            elif computer == "Spock":
                print("You win!", player, "disproves", computer)
            elif computer == "Rock":
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            elif computer == "Spock":
                print("You lose!", computer, "smashes", player)
            elif computer == "Paper":
                print("You win!", player, "cuts", computer)
            elif computer == "Lizard":
                print("You win!", player, "decapitates", computer)
        elif player == "Lizard":
            if computer == "Rock":
                print("You lose...", computer, "crushes", player)
            elif computer == "Scissors":
                print("You lose!", computer, "decapitates", player)
            elif computer == "Paper":
                print("You win!", player, "eats", computer)
            elif computer == "Spock":
                print("You win!", player, "poisons", computer)
        elif player == "Spock":
            if computer == "Lizard":
                print("You lose...", computer, "poisons", player)
            elif computer == "Paper":
                print("You lose!", computer, "dissproves", player)
            elif computer == "Rock":
                print("You win!", player, "vaporises", computer)
            elif computer == "Scissors":
                print("You win!", player, "smashes", computer)
        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,4)]

main()
