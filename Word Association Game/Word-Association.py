import random

word_associations = {
    'Dog': ['pet', 'bark', 'loyal', 'paw', 'tail'],
    'Sun': ['shine', 'day', 'bright', 'warm', 'sky'],
    'Music': ['melody', 'rhythm', 'song', 'notes', 'instrument'],
    'Tree': ['leaves', 'trunk', 'branch', 'shade', 'nature'],
    'Cake': ['sweet', 'dessert', 'celebration', 'birthday', 'delicious'],
    'Sleep': ['rest', 'dreams', 'night', 'bed', 'relax'],
    'Water': ['drink', 'thirst', 'hydrate', 'wet', 'refreshing'],
    'Flower': ['bloom', 'fragrance', 'garden', 'petal', 'colorful'],
    'Game': ['play', 'fun', 'competition', 'win', 'entertainment'],
    'Phone': ['call', 'text', 'communication', 'device', 'mobile'],
    'Rain': ['wet', 'umbrella', 'drops', 'weather', 'storm'],
    'Dance': ['movement', 'music', 'rhythm', 'expression', 'joy'],
    'Beach': ['sand', 'ocean', 'sun', 'waves', 'relaxation'],
    'Moon': ['night', 'lunar', 'orbit', 'crescent', 'astronomy'],
    'Car': ['drive', 'road', 'vehicle', 'transportation', 'engine'],
    'Raincoat': ['wet', 'protect', 'umbrella', 'waterproof', 'weather'],
    'Smile': ['happy', 'joy', 'expression', 'cheerful', 'laugh'],
    'Book': ['reading', 'story', 'pages', 'novel', 'literature'],
    'Soccer': ['sports', 'ball', 'goal', 'team', 'kick'],
    'Bird': ['feather', 'wings', 'fly', 'beak', 'song'],
    'Pizza': ['cheese', 'delicious', 'tomato', 'slice', 'topping'],
    'Garden': ['flowers', 'plants', 'green', 'grow', 'nature'],
    'Moonlight': ['night', 'lunar', 'glow', 'romantic', 'calm'],
    'Bicycle': ['ride', 'pedal', 'wheels', 'cycle', 'transportation'],
    'Mountain': ['peak', 'hiking', 'scenic', 'summit', 'elevation'],
    'Ocean': ['blue', 'waves', 'beach', 'marine', 'tide'],
    'Rainbow': ['colors', 'sky', 'arc', 'rain', 'spectrum'],
    'Family': ['love', 'relatives', 'caring', 'supportive', 'home'],
    'Chocolate': ['sweet', 'indulgence', 'cocoa', 'treat', 'delicious'],
    'Star': ['sky', 'shining', 'celestial', 'twinkle', 'astronomy'],
    'Camera': ['photography', 'lens', 'shutter', 'capture', 'memories'],
    'Summer': ['hot', 'sun', 'vacation', 'season', 'swim'],
    'Friend': ['companion', 'bond', 'trust', 'supportive', 'relationship'],
    'Coffee': ['caffeine', 'aroma', 'mornings', 'espresso', 'beverage'],
    'Adventure': ['explore', 'journey', 'travel', 'excitement', 'thrilling'],
    'Cat': ['meow', 'whiskers', 'purr', 'feline', 'pet'],
    'River': ['water', 'flow', 'bank', 'current', 'nature'],
    'Art': ['creativity', 'expression', 'painting', 'sculpture', 'imagination'],
    'Friendship': ['caring', 'trust', 'companionship', 'bond', 'support'],
    'Spring': ['flowers', 'renewal', 'growth', 'blossom', 'season'],
    'Hat': ['head', 'wear', 'brim', 'fashion', 'sun'],
    'Chair': ['sit', 'furniture', 'seat', 'backrest', 'comfort'],
    'Ball': ['round', 'sports', 'play', 'bounce', 'kick'],
    'Lamp': ['light', 'illuminate', 'bulb', 'table', 'shade'],
    'Apple': ['fruit', 'red', 'bite', 'juicy', 'healthy'],
    'Boat': ['water', 'sail', 'oar', 'float', 'navigate'],
    'Clock': ['time', 'ticking', 'hour', 'minute', 'second'],
    'Shirt': ['clothing', 'wear', 'fabric', 'sleeves', 'button'],
    'Spoon': ['utensil', 'eat', 'stir', 'soup', 'handle'],
    'Window': ['glass', 'view', 'open', 'shut', 'frame'],
    'Candle': ['light', 'wax', 'flame', 'burn', 'decorative'],
    'Banana': ['fruit', 'yellow', 'peel', 'tropical', 'healthy'],
    'Chair': ['sit', 'furniture', 'seat', 'backrest', 'comfort'],
    'Pillow': ['sleep', 'rest', 'cushion', 'bed', 'soft'],
    'Butterfly': ['insect', 'wings', 'fly', 'colorful', 'garden'],
    'Key': ['lock', 'door', 'metal', 'unlock', 'access'],
    'Cloud': ['sky', 'white', 'fluffy', 'rain', 'weather'],
    'Bridge': ['cross', 'river', 'structure', 'connect', 'path'],
    'Guitar': ['music', 'strings', 'play', 'instrument', 'melody'],
    'Moonlight': ['night', 'lunar', 'glow', 'romantic', 'calm'],
    'Orange': ['fruit', 'citrus', 'juice', 'round', 'zest'],
    'Camera': ['photography', 'lens', 'shutter', 'capture', 'memories'],
    'Dolphin': ['ocean', 'mammal', 'swim', 'marine', 'intelligent'],
    'Ice Cream': ['dessert', 'sweet', 'cold', 'flavor', 'scoop'],
    'Flowerpot': ['plant', 'soil', 'garden', 'decorate', 'clay'],
    'Backpack': ['carry', 'school', 'travel', 'straps', 'pockets'],
    'Telescope': ['stars', 'observe', 'astronomy', 'lens', 'sky'],
    'Fireworks': ['celebration', 'explosion', 'night', 'sparkle', 'display'],
    'Puzzle': ['pieces', 'solve', 'challenge', 'game', 'assemble'],
    'Television': ['watch', 'shows', 'entertainment', 'screen', 'remote'],
    'Rainbow': ['colors', 'sky', 'arc', 'rain', 'spectrum'],
    'Pizza': ['cheese', 'delicious', 'tomato', 'slice', 'topping'],
    'River': ['water', 'flow', 'bank', 'current', 'nature'],
    'Moonlight': ['night', 'lunar', 'glow', 'romantic', 'calm'],
    'Music': ['melody', 'rhythm', 'song', 'notes', 'instrument'],
    'Soccer': ['sports', 'ball', 'goal', 'team', 'kick'],
    'Dolphin': ['ocean', 'mammal', 'swim', 'marine', 'intelligent'],
    'Lemon': ['fruit', 'yellow', 'sour', 'juice', 'citrus'],
    'Guitar': ['music', 'strings', 'play', 'instrument', 'melody'],
    'Winter': ['cold', 'snow', 'season', 'cozy', 'holiday'],
    'Forest': ['trees', 'nature', 'green', 'wildlife', 'peaceful'],
    'Penguin': ['bird', 'waddle', 'snow', 'flightless', 'Antarctica'],
    'Camera': ['photography', 'lens', 'shutter', 'capture', 'memories'],
    'Summer': ['hot', 'sun', 'vacation', 'season', 'swim']
}

def get_user_name():
    return input("Greetings, adventurer! What's your name? ")

def display_word_association(word):
    print(f"\nWord: {word}")

#def play_again():
    #return input("\nDo you want to embark on another journey? (yes/no) ").lower().startswith('y')

def show_outro(user_name, score):
    print(f"\nFarewell, {user_name}!")
    print(f"Your quest has come to an end. You achieved a score of {score}.")
    print("May your adventures continue in the realms of knowledge and fun!\n")

def main():
    print("\nWelcome to the Word Association Game!")
    print("# Disclaimer: The association words are limited to the game master.\n")
    user_name = get_user_name()
    score = 0

    while True:
        word = random.choice(list(word_associations.keys()))
        display_word_association(word)

        user_input = input("\nWhat word is associated with the given word? Your answer: ")
        if user_input in (word_associations[word]):
            score += 1
            print(f"Correct! Your current score is: {score}\n")
        else:
            print(f"Alas! That was not the right word.")
            break  
        
        #if not play_again():
           #break

    show_outro(user_name, score)

if __name__ == "__main__":
    main()
