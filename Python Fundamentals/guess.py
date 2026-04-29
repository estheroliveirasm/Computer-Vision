import random
import math

# Objective: Find a random number between 1 and 100, competing against an AI.
# This code uses input handling, if/else logic, and basic math.

def play_game():
    secret_number = random.randint(1, 100)
    user_won = False
    ai_won = False
    
    # AI boundaries (used for the AI's logic)
    ai_min = 1
    ai_max = 100
    
    print("--- Welcome to the Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100. Can you beat the AI?")

    while not user_won and not ai_won:
        # --- User's Turn ---
        # Based on your previous 'happy birthday' and 'operations' scripts
        print("\nYour turn!")
        user_guess = int(input("Enter your guess: "))

        if user_guess == secret_number:
            user_won = True
            break
        elif user_guess < secret_number:
            print("The number is Higher! ↑")
        else:
            print("The number is Lower! ↓")

        # --- AI's Turn ---
        # The AI uses math.floor to calculate the midpoint, similar to your 'n.py' logic
        ai_guess = math.floor((ai_min + ai_max) / 2)
        print(f"AI's turn: The AI guesses {ai_guess}")

        if ai_guess == secret_number:
            ai_won = True
            break
        elif ai_guess < secret_number:
            print("The AI was told: Higher! ↑")
            ai_min = ai_guess + 1
        else:
            print("The AI was told: Lower! ↓")
            ai_max = ai_guess - 1

    # Final feedback based on the win condition
    if user_won:
        print(f"\nCongratulations! You found the number {secret_number} and beat the AI!")
    else:
        print(f"\nGame Over! The AI found the number {secret_number} first.")

if __name__ == "__main__":
    play_game()