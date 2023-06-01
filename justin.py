def start_game():
    print("Welcome to 'The Mysterious Mansion'!")
    print("You find yourself standing in front of an old, creepy mansion.")
    print("Do you dare to enter?")
    print("1. Yes, I'm fearless!")
    print("2. No way, it's too spooky!")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        enter_mansion()
    elif choice == "2":
        print("You chicken out and decide to leave. Game over!")
    else:
        print("Invalid choice. Try again.")
        start_game()

def enter_mansion():
    print("You enter the mansion and see two doors ahead.")
    print("Which door do you choose?")
    print("1. Door on the left")
    print("2. Door on the right")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        left_door()
    elif choice == "2":
        right_door()
    else:
        print("Invalid choice. Try again.")
        enter_mansion()

def left_door():
    print("You enter a room filled with treasure!")
    print("Congratulations! You're rich!")
    print("1. Leave the mansion with the treasure")
    print("2. Keep exploring the mansion")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You successfully escape the mansion with the treasure. You win!")
    elif choice == "2":
        print("As you explore further, you encounter a ghost and get scared to death. Game over!")
    else:
        print("Invalid choice. Try again.")
        left_door()

def right_door():
    print("You enter a dark room with a locked door.")
    print("What do you do?")
    print("1. Look for a key")
    print("2. Try to break down the door")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You find a key hidden under a rug. You unlock the door and discover a secret passage!")
        secret_passage()
    elif choice == "2":
        print("You attempt to break down the door but fail. The noise attracts a group of monsters who capture you. Game over!")
    else:
        print("Invalid choice. Try again.")
        right_door()

def secret_passage():
    print("The secret passage leads you to a room with a mystical artifact.")
    print("1. Take the artifact")
    print("2. Leave it and continue exploring")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("As you grab the artifact, a curse is triggered, and you're trapped in the mansion forever. Game over!")
    elif choice == "2":
        print("You wisely decide to leave the artifact behind and keep exploring.")
        print("You eventually find an exit and escape the mansion. You win!")
    else:
        print("Invalid choice. Try again.")
        secret_passage()

start_game()
