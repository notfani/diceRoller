import random

def run():
    print("Welcome to the Dice Roller!")
    while True:
        user_input = input("Enter dice to roll (e.g., '2d6' for two six-sided dice) or 'q' to exit: ")
        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break
        try:
            num_dice, die_type = map(int, user_input.lower().split('d'))
            rolls = [random.randint(1, die_type) for _ in range(num_dice)]
            print(f"You rolled: {rolls} (Total: {sum(rolls)})")
        except (ValueError, IndexError):
            print("Invalid input. Please enter in the format 'NdM' where N is number of dice and M is sides per die.")


if __name__ == "__main__":
    run()