import random
import re

def run():
    print("Welcome to the Dice Roller!")
    while True:
        user_input = input("Enter dice to roll (e.g., '2d6+3' for two six-sided dice with +3 modifier) or 'q' to exit: ")
        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break

        match = re.match(r'(\d+)d(\d+)([+-]\d+)?', user_input.lower())
        if match:
            num_dice = int(match.group(1))
            die_type = int(match.group(2))
            modifier = int(match.group(3)) if match.group(3) else 0
            rolls = [random.randint(1, die_type) for _ in range(num_dice)]
            total = sum(rolls) + modifier
            modifier_str = f" {modifier:+d}" if modifier != 0 else ""
            print(f"You rolled: {rolls} (Total: {sum(rolls)}{modifier_str} = {total})")
        else:
            print("Invalid input. Please enter in the format 'NdM' optionally followed by '+X' or '-X' where N is number of dice, M is sides per die, and X is the modifier.")


if __name__ == "__main__":
    run()