# A simple text-based interactive story game

def intro():
    print("Welcome to the Adventure of the Lost Kingdom!")
    print("You find yourself in a mysterious forest. The sun is setting, and you hear eerie sounds around you.")
    print("In front of you, you see two paths.")
    print("One path leads to a dark cave, and the other leads deeper into the forest.")
    print("What will you do?")
    print("1. Enter the cave.")
    print("2. Walk deeper into the forest.")

    choice = input("Your choice (1/2): ")

    if choice == "1":
        cave()
    elif choice == "2":
        forest()
    else:
        print("Invalid choice! Please select 1 or 2.")
        intro()


def cave():
    print("\nYou step into the dark cave. It's cold, and you can barely see anything.")
    print("As you walk deeper, you hear a growl. Something is moving in the shadows!")
    print("Suddenly, a large creature leaps out of the darkness!")
    print("What will you do?")
    print("1. Fight the creature.")
    print("2. Run away.")

    choice = input("Your choice (1/2): ")

    if choice == "1":
        print("\nYou fight valiantly, but the creature is too strong. You fall to the ground.")
        print("It looks like this is the end for you...")
        game_over()
    elif choice == "2":
        print("\nYou quickly turn and run. The creature chases you, but you're too fast!")
        print("You manage to escape the cave and find your way back to the forest.")
        forest()
    else:
        print("Invalid choice! Please select 1 or 2.")
        cave()


def forest():
    print("\nYou decide to walk deeper into the forest. The trees are tall and ominous, and you hear strange noises.")
    print("As you continue, you find an old hut in the clearing.")
    print("Do you approach the hut or continue walking?")
    print("1. Approach the hut.")
    print("2. Keep walking.")

    choice = input("Your choice (1/2): ")

    if choice == "1":
        hut()
    elif choice == "2":
        print("\nYou walk deeper into the forest. Suddenly, you trip and fall into a pit!")
        print("You can't escape, and the forest claims you.")
        game_over()
    else:
        print("Invalid choice! Please select 1 or 2.")
        forest()


def hut():
    print("\nYou approach the hut cautiously. The door creaks open, and inside you see an old woman sitting by a fire.")
    print("She looks up and smiles at you. 'Welcome, traveler,' she says. 'I have been expecting you.'")
    print("She offers you a potion that can either heal you or give you great power.")
    print("What will you do?")
    print("1. Drink the healing potion.")
    print("2. Drink the potion of power.")

    choice = input("Your choice (1/2): ")

    if choice == "1":
        print("\nThe healing potion restores your strength. You feel better and ready to continue your journey.")
        print("You leave the hut and decide to explore further. You find a hidden treasure chest!")
        print("Congratulations, you have won!")
    elif choice == "2":
        print("\nThe potion of power surges through your veins. You feel invincible!")
        print("But, soon you begin to lose control. The power overwhelms you, and you become a creature of darkness.")
        print("You have succumbed to the dark forces.")
        game_over()
    else:
        print("Invalid choice! Please select 1 or 2.")
        hut()


def game_over():
    print("\nGame Over.")
    print("Would you like to play again? (yes/no)")
    choice = input("> ").lower()

    if choice == "yes":
        intro()
    else:
        print("Thank you for playing!")
        exit()


# Start the game
intro()
