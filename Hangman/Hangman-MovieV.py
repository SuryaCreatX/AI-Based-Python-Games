import random

def choose_word():
    words = ["avatar", "frozen", "jaws", "matrix", "titanic",
             "alien", "brave", "casino", "fargo", "grease",
             "hitch", "inception", "jumanji", "kingdom", "lion",
             "memento", "narnia", "oblivion", "platoon", "rocky",
             "scream", "tangled", "up", "vertigo", "wanted",
             "x-men", "zodiac", "mersal", "kabali", "sarkar", "kaithi", "maari",
             "vedhalam", "petta", "velaikkaran", "raatchasan", "theri",
             "veeram", "vikram", "raja rani", "thadam", "iru mugan",
             "singam", "veeran", "kgf", "jilla", "kathi", "arrambam",
             "mankatha", "vettaikaaran"]
    return random.choice(words)

def display_hangman(attempts):
    stages = [
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        '''
    ]
    return stages[attempts]

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

def main():
    print("🎉 Welcome to the Exciting Hangman Game! 🎉")
    print("🎉 The Movie Mania - Test your Movie Knowledge Here! 🎉")
    player_name = input("🌟 What's your name? ")
    print(f"Hello, {player_name}! Get ready for a thrilling challenge.")

    while True:
        print("\n")
        rounds = input("How many rounds do you want to play? (3/5/10): ")
        if rounds not in ["3", "5", "10"]:
            print("⚠️ Please enter a valid number of rounds.")
            continue
        rounds = int(rounds)
        
        total_score = 0
        
        for round_num in range(1, rounds + 1):
            print(f"\n🔥 Round {round_num} / {rounds} 🔥")
            word = choose_word()
            guessed_letters = []
            attempts = 6
            score = 100

            display_word = ""
            for letter in word:
                if letter in guessed_letters:
                    display_word += letter
                else:
                    display_word += "_"

            print(display_hangman(6 - attempts))
            print("Word:", display_word)

            while attempts > 0:
                
                guess = input("🔮 Guess a letter: ").lower()

                if len(guess) != 1 or not guess.isalpha():
                    print("⚠️ Please enter a valid single letter.")
                    continue

                if guess in guessed_letters:
                    print("⛔ You've already guessed that letter.")
                    continue

                guessed_letters.append(guess)

                if guess in word:
                    print("🎊 Correct! You're on fire!🔥")
                    # Increment the score for correct guess
                    score += 10
                else:
                    print("❌ Incorrect! Keep going, you can do it!")
                    
                    attempts -= 1

                display_word = ""
                for letter in word:
                    if letter in guessed_letters:
                        display_word += letter
                    else:
                        display_word += "_"

                print(display_hangman(6 - attempts))
                print("Word:", display_word)

                if "_" not in display_word:
                    print(f"🌟 Congratulations, {player_name}! You've cracked the word:", word)
                    # Add the remaining attempts to the score
                    score += attempts * 10
                    total_score += score  # Add score for the round
                    print("Score",score)
                    break

            if attempts == 0:
                total_score += score  # Add score even if attempts run out
                print(display_hangman(6 - attempts))
                print("😞 Sorry, you've run out of attempts. The word was:", word)
                print(f"Round {round_num} Score: {score}")
                    
        print("\n🏆 Game Over! Score Report 🏆")
        print(f"Total Rounds Played: {rounds}")
        print(f"Total Score: {total_score}")
    
        if not play_again():
            print(f"🙌 Thank you for playing, {player_name}! You did great. See you next time!")
            break

if __name__ == "__main__":
    main()