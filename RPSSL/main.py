import random
possible_values = ["rock", "paper", "scissors", "spock", "lizard"]

dict_of_values = {x: 0 for x in possible_values}
winner = {"player": 0, "computer": 0}

def main():
    while True:
        show_menu()
        result = int(input(">>> "))
        if result == 1:
            p_v_c()
        elif result == 2:
            stats()
        elif result == 3:
            return
        else:
            print("Wrong input")

def stats():
    print("Anzahl gespielter Symbole")
    for key in dict_of_values.keys():
        print(key, ":", dict_of_values[key])
    print("\nWie oft hat wer gewonnen?")
    for key in winner.keys():
        print(key, ":", winner[key])


def p_v_p():
    pass
    
def p_v_c():
    computer_choice = random.choice(possible_values)
    computer = parser(computer_choice)
    
    user_input = input("Enter your choice >>> ")
    if user_input not in possible_values:
        print("Please choose a correct value!")
        return
    user = parser(user_input)

    dict_of_values[user_input] += 1
    dict_of_values[computer_choice] += 1

    print("Computer chose {} and player chose {}".format(computer_choice, user_input))
    if computer == user:
        print("draw")
        return

    if ((computer - user) % 5) % 2 == 1:
        print("computer wins")
        winner["computer"] += 1
    if ((computer - user) % 5) % 2 == 0:
        print("player wins")
        winner["player"] += 1



def show_menu():
    print("\n\nRock Paper Scissors Spock Lizard")
    print("================================")
    print("Choose one of the following: ")
    print("1) Play a game of RPSSL")
    print("2) Show statistics")
    print("3) Quit the game")

def parser(figure):
    return possible_values.index(figure) 

if __name__ == "__main__":
    main()
