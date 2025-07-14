import random
import time


# Print a message and pause for a specified time
def print_sleep(message, wait_time):
    # Print a message and pause for a specified time
    if "\n" in message:
        # split the message into lines and print each line
        for line in message.split("\n"):
            print(line)
            time.sleep(wait_time)
    else:
        print(message)
        time.sleep(wait_time)


# List of enemies that the player might encounter
enemies = [
    "angry siamese",
    "feral cat",
    "mysterious black cat",
    "giant tabby",
    "wild lynx",
    "pirate tuxedo",
]
# List of whimsical weapons the player can choose from
weapons = [
    "rubber chicken",
    "banana peel",
    "feather duster",
    "squeaky toy",
    "water pistol",  # Fatal weapon
    "water balloon",  # Fatal weapon
]
# List of fatal weapons that can defeat the enemies
fatal_weapons = ["water pistol", "water balloon"]
# Define global variables to store the player's weapon, enemy, and name
weapon = None  # Global variable to store the chosen weapon
enemy = None  # Global variable to store the current enemy
name = None  # Global variable to store the player's name


# Get the player's name
def get_name():
    global name
    while not name or name.strip() == "" or len(name) < 2:
        name = input("What is your name, brave adventurer? ")
    print_sleep(f"Welcome, {name}! Your quest begins now.", 2)


# Introductory function to set the scene and start the adventure
def intro():
    print_sleep(
        (
            f"=^.^=   =^.^=   =^.^=   =^.^=   =^.^=\n"
            f"Once upon a time, a peaceful village was plagued by\n"
            f"mysterious cats lurking in the nearby forest.\n"
            f"Brave souls like {name} ventured into the woods, hoping to\n"
            f"restore peace and rid the land of these feline foes.\n\n"
            f"{name}, you find yourself at the edge of a dense forest.\n"
            f"Rumor has it that a dangerous cat is hiding deep within.\n"
            f"Before you enter, you spot a pile of odd weapons in a clearing."
        ),
        3,
    )
    choose_weapon()


# Run back to the village if the player chooses to run away
def run_away():
    print_sleep(
        f"{name}, you reveal yourself as a chicken and run away in shame!\n",
        2,
    )
    play_again()


# Prompt the player to choose whether to enter the forest or run away
def enter_forest_or_run():
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Do you want to (1) enter the forest or (2) run away? ")
        if choice == "1":
            print_sleep(
                "You bravely step into the forest, ready for adventure!",
                2,
            )
            enter_forest()
        elif choice == "2":
            run_away()


# Prompt the player to choose a weapon from the available options
def choose_weapon():
    global weapon
    print_sleep("You may choose one weapon to take with you:", 2)
    for idx, w in enumerate(weapons, 1):
        print_sleep(f"{idx}. {w}", 1)
    choice = ""
    while choice not in [str(i) for i in range(1, len(weapons) + 1)]:
        choice = input(f"Pick a weapon (1-{len(weapons)}): ")
    weapon = weapons[int(choice) - 1]
    print_sleep(
        f"You pick up the {weapon}—a true hero's choice! \n"
        f"Its spirit matches your courage and determination.\n",
        2,
    )
    enter_forest_or_run()


# Choose a random enemy from the list and start combat
def enter_forest():
    global enemy
    enemy = random.choice(enemies)
    print_sleep(f"As you walk further, a {enemy} appears from the shadows!", 2)
    combat()


# The combat function handles the battle logic
# Prompts the player to fight or run away
def combat():
    global weapon
    print_sleep(f"The {enemy} pounces at you!", 2)
    print_sleep(f"You ready your {weapon} for battle.", 2)
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Please choose (1) to fight or (2) to run away: ")
        if choice == "1":
            print_sleep(
                f"You bravely face the {enemy} with your {weapon}...",
                2,
            )
            if weapon in fatal_weapons:
                print_sleep(
                    f"The {enemy} hates water! It flees into the trees. "
                    f"You have saved the village!\n"
                    f"You are a hero, {name}! The villagers celebrate your "
                    f"bravery and offer you a glass of milk.\n",
                    2,
                )
            else:
                print_sleep(
                    f"Your {weapon} is no match for the cunning cat. "
                    f"You are defeated!\n"
                    f"The cat toys with {name}, circling and pouncing, "
                    f"savoring its victory.\n"
                    f"The cat eats you while you scream in terror!\n",
                    2,
                )
        elif choice == "2":
            run_away()
    play_again()


# Prompt the player to play again or exit the game
def play_again():
    choice = ""
    while choice not in ["y", "n"]:
        choice = input("Would you like to play again? (y/n) ")
        if choice == "n":
            print_sleep("Thanks for playing! May your days be cat-free!", 2)
            return
        elif choice == "y":
            print_sleep("Excellent! Restarting the adventure ...", 2)
            start_game()


# Start the game with a welcome message and player name input
def start_game():
    print_sleep(
        "Welcome to the Cat Quest Adventure Game! \n"
        "Prepare for a whimsical journey through a land of cats and courage.",
        2,
    )
    # Get the player's name before starting the adventure
    get_name()
    intro()


# Execute the game
start_game()
