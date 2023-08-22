import random
import time

def display_text_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_user_name():
    display_text_with_delay("Greetings, daring challenger! What is your name?")
    return input()

def get_user_guess():
    display_text_with_delay("\nEnter your guess: ")
    while True:
        try:
            guess = int(input())
            break
        except ValueError:
            display_text_with_delay("Oops! That's not a valid number. Come on, try again: ")
    return guess

def play_user_guessing_game():
    display_text_with_delay("\nWelcome to the Enigmatic Mindmaster Game!")
    name = get_user_name()
    secret_number = random.randint(1, 100)

    display_text_with_delay(f"\n{name}, I have a mysterious number between 1 and 100 in my mind. Can you unravel its secrets in just 10 tries?")

    for attempt in range(1, 11):
        user_guess = get_user_guess()
        if user_guess < secret_number:
            display_text_with_delay("Too low! Aim higher, brave soul.")
        elif user_guess > secret_number:
            display_text_with_delay("Too high! Lower your sights a bit.")
        else:
            display_text_with_delay(f"Congratulations, {name}! You have cracked the code! The number was {secret_number}. You did it in {attempt} tries!")
            break
    else:
        display_text_with_delay(f"Alas, {name}. You have used up your chances. The elusive number was {secret_number}. Better luck next time!")



def play_ai_guessing_game():
    display_text_with_delay("\nWelcome to the Mysterious AI Guessing Game!")
    name = get_user_name()
    display_text_with_delay(f"\nPrepare yourself, {name}. Conceal a number in your mind between 1 and 100, and I, the AI Mindmaster, will venture to fathom its enigma.")

    time.sleep(1)

    low = 1
    high = 100
    attempts = 1

    while True:
        ai_guess = (low + high) // 2
        display_text_with_delay(f"\nAttempt {attempts}: My intuition leads me to guess {ai_guess}.")

        user_feedback = input("Is your number higher, lower, or correct? (higher/lower/correct): ").lower().strip()
        while user_feedback not in ['higher', 'lower', 'correct']:
            user_feedback = input("Please respond with 'higher', 'lower', or 'correct': ").lower().strip()

        if user_feedback == 'correct':
            display_text_with_delay(f"Yay! I guessed your number {ai_guess} correctly in {attempts} tries!")
            break
        elif user_feedback == 'higher':
            low = ai_guess + 1
        else:
            high = ai_guess - 1

        attempts += 1

    display_text_with_delay(f"Ah, I have discovered your enigma, {name}. Your concealed number was {low}. I did it in {attempts-1} tries!")

def play_again():
    display_text_with_delay("\nWould you dare to play a game ?")
    display_text_with_delay("1. Play User Guessing Game")
    display_text_with_delay("2. Play AI Guessing Game")
    display_text_with_delay("3. Exit the Game")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def main():
    display_text_with_delay("Welcome to the Mysterious Number Guessing Game!")

    while True:
        choice = play_again()

        if choice == '1':
            play_user_guessing_game()
        elif choice == '2':
            play_ai_guessing_game()
        elif choice == '3':
            display_text_with_delay("Thank you for playing the Mindmaster Game! Farewell!")
            break
        else:
            display_text_with_delay("Invalid choice. Please choose a valid option (1/2/3).")

if __name__ == "__main__":
    main()
