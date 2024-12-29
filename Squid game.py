import random
import time


def red_light_green_light():
    print("Welcome to Red Light, Green Light!")
    print("You must type 'run' repeatedly to move forward during green light.")
    print("Stop typing during red light to survive!")

    position = 0
    while position < 5:
        light = random.choice(["Green", "Red"])
        print(f"Light: {light}")

        if light == "Green":
            action = input("Type 'run' to move: ").strip()
            if action.lower() == "run":
                position += 1
                print(f"You moved forward. Current position: {position}/7")
            else:
                print("You didn't move!")
        else:
            print("Type 'run' to move: ")

            action = input("Type 'run' to move: ").strip()
            if action.lower() == "run":
                print("You moved during Red Light. You're out!")
                return False

    print("Congratulations! You passed Red Light, Green Light!")
    return True


def glass_bridge():
    print("Welcome to the Glass Bridge!")
    print(
        "Choose the correct platform to step on (1 or 2). One is safe, the other breaks!"
    )

    platforms = [random.randint(1, 2) for _ in range(5)]
    for i, correct_platform in enumerate(platforms):
        print(f"Step {i + 1}: Choose a platform (1 or 2): ")
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. You're out!")
            return False

        if choice == correct_platform:
            print("Safe! Move to the next step.")
        else:
            print("Wrong choice! The platform breaks. You're out!")
            return False

    print("Congratulations! You passed the Glass Bridge!")
    return True


def play_squid_game():
    print("Welcome to Squid Game!")
    print("You must survive all challenges to win.")

    if red_light_green_light():
        print("\nMoving to the next game...\n")
        time.sleep(2)
        if glass_bridge():
            print("\nCongratulations! You survived all the games and won Squid Game!")
        else:
            print("Game Over at the Glass Bridge.")
    else:
        print("Game Over at Red Light, Green Light.")


if __name__ == "__main__":
    play_squid_game()
