import random

# List of riddles and their corresponding answers
riddles = {
    "I have keys that fit no locks, and space without doors. What am I?": "typewriter",
    "I'm full of holes, but I can still hold water. What am I?": "sponge",
    "I can be cracked, made, told, and played. I can also be blue, sad, and confused. What am I?": "joke",
    "I have keys but don't open locks. I'm meant to be read, but I'm not a book. What am I?": "newspaper",
    "I have no legs, but I can travel the world. What am I?": "stamp",
    "I'm a word of letters three, add two and fewer there will be. What am I?": "few",
    "I have a heart that doesn't beat. What am I?": "artichoke",
    "I'm not alive, but I can die. I'm not solid, but I can melt. What am I?": "snow",
    "I'm tall when I'm young and short when I'm old, and I have leaves but no branches. What am I?": "candle",
    "I'm not a planet, but I'm round, spinning, and bright. What am I?": "coin",
    "I have keys that open doors to a world of imagination. What am I?": "book",
    "I'm black and white and loved all over the world. What am I?": "panda",
    "I have a heart that never beats, I have a home but I never sleep. What am I?": "artichoke",
    "I have cities but no houses, forests but no trees, and rivers but no water. What am I?": "map",
    "I'm always in front of you, but you'll never see me. What am I?": "future",
    "I have keys that open no locks, I have space but no room, and I allow you to travel the world. What am I?": "internet",
     "I have keys but open no locks. I have space but no room. You can enter but can't go outside. What am I?": "keyboard",
    "You see me once in June, twice in November, and not at all in May. What am I?": "the letter 'e'",
    "I can fly without wings. I cry without eyes. Whenever I go, darkness follows me. What am I?": "cloud",
    "I'm not alive, but I can grow. I don't have lungs, but I need air. What am I?": "fire",
    "The more you take, the more you leave behind. What am I?": "footsteps",
    "I'm tall when I'm young and short when I'm old. What am I?": "candle",
    "I can be cracked, made, told, and played. What am I?": "joke",
    "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?": "echo",
    "I have keys but open no locks. I have strings but make no sound. What am I?": "piano",
    "I'm not alive, but I can die. I'm not solid, but I can be carved. What am I?": "ice",
    "I'm a fruit, a color, and a feeling. What am I?": "orange",
    "I'm found in a shell and can't be told. What am I?": "secret",
    "I'm a button on a website and a thing that crawls. What am I?": "spider",
    "I'm a planet and a type of metal. What am I?": "mercury",
    "I'm a type of wave and a way to greet. What am I?": "hello",
    "I can be popped and tell you a story. What am I?": "popcorn",
    "I'm a green vegetable and a form of money. What am I?": "cabbage",
    "I'm a season and a seasoning. What am I?": "pepper",
    "I'm made of rubber and help you erase. What am I?": "eraser",
    "I'm a part of your face and a type of card. What am I?": "nose",
    "I'm a type of transport and a type of game. What am I?": "bike",
    "I'm a type of dance and a source of light. What am I?": "disco",
    "I'm a part of a plant and a unit of time. What am I?": "leaf",
    "I'm a type of shoe and a part of your body. What am I?": "heel",
    "I'm a type of wave and a large gathering. What am I?": "wave",
    "I'm a type of nut and a shade of brown. What am I?": "chestnut",
    "I'm a way to communicate and a type of fruit. What am I?": "pear",
    "I'm a small insect and a type of kiss. What am I?": "butterfly",
    "I'm a unit of temperature and a form of measurement. What am I?": "degree",
    "I'm a type of star and a shape you draw. What am I?": "star",
    "I'm a type of flower and a girl's name. What am I?": "rose",
    "I'm a type of code and a type of text. What am I?": "binary",
    "I'm a type of ball and a type of clock. What am I?": "basketball",
    "I'm a type of bird and a tool for writing. What am I?": "pen",
    "I'm a type of fish and a type of card game. What am I?": "trout",
    "I'm a type of animal and a unit of electricity. What am I?": "horse",
    "I'm a type of game and a type of bread. What am I?": "cricket",
    "I'm a type of light and a type of sword. What am I?": "lightsaber",
    "I'm a type of tree and a place to study. What am I?": "oak",
    "I'm a type of fruit and a type of color. What am I?": "apple",
    "I'm a type of cake and a type of desert. What am I?": "cheesecake",
    "I'm a type of meat and a type of candy. What am I?": "ham",
    "I'm a type of dog and a form of currency. What am I?": "pound",
    "I'm a type of tool and a type of dance move. What am I?": "hammer",
    "I'm a type of flower and a type of game. What am I?": "daisy",
    "I'm a type of bird and a type of currency. What am I?": "eagle",
    "I'm a type of animal and a type of leap. What am I?": "frog",
    "I'm a type of light and a type of party. What am I?": "spotlight",
    "I'm a type of card and a type of garden. What am I?": "wildcard",
    "I'm a type of bird and a type of tool. What am I?": "crowbar",
    "I'm a type of dance and a type of cereal. What am I?": "breakdance",
    "I'm a type of tree and a type of ball. What am I?": "pine",
    "I'm a type of fruit and a type of pet. What am I?": "banana",
    "I'm a type of fish and a type of instrument. What am I?": "bass",
    "I'm a type of plant and a form of paper. What am I?": "palm",
    "I'm a type of animal and a type of board. What am I?": "chess",
    "I'm a type of wave and a type of haircut. What am I?": "wave",
    "I'm a type of bird and a type of message. What am I?": "tweet",
    "I'm a type of music and a type of street. What am I?": "jazz",
    "I'm a type of fruit and a type of capital. What am I?": "kiwi",
    "I'm a type of tree and a type of building. What am I?": "palm",
    "I'm a type of flower and a type of story. What am I?": "tulip",
    "I'm a type of animal and a type of dessert. What am I?": "elephant",
    "I'm a type of light and a type of insect. What am I?": "firefly",
    "I'm a type of bird and a type of fruit. What am I?": "bluejay",
    "I'm a type of dance and a type of storm. What am I?": "hurricane"

}

def get_hint(answer, attempt):
    # Generate a hint based on the attempt number
    if attempt == 1:
        return "Here's a clue: It starts with the letter '{}'.".format(answer[0])
    elif attempt == 2:
        return "Here's another clue: The first two letters are '{}'.".format(answer[:2])
    else:
        return "Sorry, you're out of attempts. The correct answer is: '{}'.".format(answer)

def main():
    print("Welcome to RiddleQuest!")
    player_name = input("What's your name? ")
    print("\nGreetings, {}. Embark on a journey to solve riddles and earn points!".format(player_name))
    
    while True:
        total_score = 0
        rounds = int(input("How many rounds would you like to play? (3/5/10): "))
        
        if rounds not in [3, 5, 10]:
            print("Oops, that's an invalid number of rounds. Please choose 3, 5, or 10.")
            continue
        
        print("\nFantastic, {}! Prepare for {} rounds of riddle-solving in RiddleQuest.".format(player_name, rounds))
        
        for round_num in range(1, rounds + 1):
            riddle = random.choice(list(riddles.keys()))
            
            print("\nRound {}: Here's your riddle:".format(round_num))
            print("Riddle: " + riddle)
            
            for attempt in range(3):
                guess = input("Your answer (Attempt {}): ".format(attempt + 1)).lower()
                
                if guess == riddles[riddle]:
                    if attempt == 0:
                        score = 100
                    elif attempt == 1:
                        score = 50
                    else:
                        score = 25
                    print("Bravo, {}! You cracked the riddle! You earn {} points.".format(player_name, score))
                    total_score += score
                    break
                else:
                    hint = get_hint(riddles[riddle], attempt + 1)
                    print("Oops, that's not quite right. Here's a hint: " + hint)
            
            print("Score for round {}: {}".format(round_num, total_score))
        
        print("\nCongratulations, {}! You've completed all {} rounds of RiddleQuest.".format(player_name, rounds))
        print("Your total score is: {}".format(total_score))
        if total_score > 0:
            play_again = input("Would you like to embark on another RiddleQuest, {}? (yes/no): ".format(player_name)).lower()
            if play_again != "yes":
                print("Thank you for playing RiddleQuest, {}. May your wit stay sharp!".format(player_name))
                break
        else:
            print("It looks like you didn't score any points this time, {}. Don't give up, and try again!".format(player_name))
            play_again = input("Would you like to embark on another RiddleQuest, {}? (yes/no): ".format(player_name)).lower()
            if play_again != "yes":
                print("Thank you for playing RiddleQuest, {}. May your next adventure be more rewarding!".format(player_name))
                break

if __name__ == "__main__":
    main()
