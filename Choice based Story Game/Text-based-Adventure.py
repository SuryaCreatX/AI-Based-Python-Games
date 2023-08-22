import random
import time

# Global variables to track the player's progress and choices
player_name = ""
friend_names = []
skills = []

# Helper function to get user input
def get_input(prompt):
    return input(prompt).strip().lower()

# Helper function to display character info
def display_character_info():
    print("\nCharacter Info:")
    print(f"Name: {player_name}")
    print(f"Friends: {', '.join(friend_names)}")
    print(f"Skills: {skills}")

# Helper function to display story text with a pause effect
def display_with_pause(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Hero Legacy
def hero_legacy():
    global skills

    display_with_pause("\nThe Hero's Legacy\n")
    display_with_pause("The story concludes with multiple endings based on your choices throughout the game:\n")
    display_with_pause("\nConclusion: Multiple Endings\n")

    if "Victory" in skills and "Combat" in skills:
        display_with_pause("Ending 1 - The Hero's Triumph:")
        display_with_pause(f"{player_name} embraces his destiny as a true hero, defeats Morgana, and brings peace to Aetheria.")
        display_with_pause("He becomes a revered figure in history, with monuments erected in his honor across the land.")
    if "Defeated" in skills and "Insight" in skills:
        display_with_pause("Ending 2 - The Fallen Hero:")
        display_with_pause(f"{player_name} succumbs to the allure of dark magic, leading to his downfall.")
        display_with_pause("He becomes a dark lord, wreaking havoc upon Aetheria, and players face the challenging task of taking him down to save the realm from darkness.")
    if "Victory" in skills and "Courage" in skills and "Stealth" in skills:
        display_with_pause("Ending 3 - The Sacrifice:")
        display_with_pause(f"In a heart-wrenching twist, {player_name} makes the ultimate sacrifice to save his friends and Aetheria.")
        display_with_pause("His selfless act leaves a lasting impact on Aetheria, inspiring generations to come.")
    if "Victory" in skills and "Diplomacy" in skills and "Bargaining" in skills:
        display_with_pause("Ending 4 - The Uniter:")
        display_with_pause(f"{player_name} realizes that unity and cooperation are the keys to victory.")
        display_with_pause("He forges alliances with various factions, including former enemies, to defeat Morgana and create a new era of peace and harmony.")
    if "Victory" in skills and "Stealth" in skills and "Thievery" in skills:
        display_with_pause("Ending 5 - The Sorcerer King:")
        display_with_pause(f"{player_name} accumulates immense power and becomes a benevolent ruler, guiding Aetheria to an age of enlightenment and prosperity.")


# Helper function for boss battles
def boss_battle(boss_name, boss_health, player_health, player_attack):
    display_with_pause(f"\nA fierce battle begins with {boss_name}!")

    while boss_health > 0 and player_health > 0:
        boss_damage = random.randint(10, 20)
        player_damage = random.randint(player_attack - 5, player_attack + 5)

        display_with_pause(f"\n{boss_name} attacks! You receive {boss_damage} damage.")
        player_health -= boss_damage

        if player_health <= 0:
            display_with_pause("\nYou have been defeated!")
            return False

        display_with_pause(f"\nYou attack {boss_name}! You deal {player_damage} damage.")
        boss_health -= player_damage

    display_with_pause(f"\nYou have defeated {boss_name}!")
    return True

# Scenario 1: The Enchanted Forest - The Dragon's Lair
def dragon_lair():
    global skills

    display_with_pause("\nChapter 1: The Enchanted Forest\n")
    display_with_pause("Scenario 1: The Dragon's Lair\n")
    display_with_pause(f"As {player_name} enters the mystical world of Aetheria, he stumbles upon an ancient dragon's lair.")
    display_with_pause("The dragon, a guardian of the forest, challenges him to prove his worthiness.")

    display_with_pause("\nChoice 1: Stand and face the dragon valiantly.")
    display_with_pause("Choice 2: Try to reason with the dragon.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} stands and faces the dragon valiantly.")
        if "Courage" in skills:
            display_with_pause("The dragon acknowledges your courage and offers you a chance to prove your worth in a series of trials.")
        else:
            display_with_pause("The dragon finds you lacking and chases you away, leaving you injured and humiliated.")
    elif decision == "2":
        display_with_pause(f"{player_name} tries to reason with the dragon.")
        if "Diplomacy" in skills:
            display_with_pause("The dragon respects your diplomacy and gives you a quest to recover a stolen artifact from cunning goblins.")
        else:
            display_with_pause("The dragon sees this as a sign of weakness and becomes more hostile.")

# Scenario 2: The Enchanted Forest - The Goblin Ambush
def goblin_ambush():
    global skills

    display_with_pause("\nChapter 1: The Enchanted Forest\n")
    display_with_pause("Scenario 2: The Goblin Ambush\n")
    display_with_pause(f"While on the quest to recover the stolen artifact, {player_name} faces an ambush by clever goblins.")

    display_with_pause("\nChoice 1: Engage in a full-on battle with the goblins.")
    display_with_pause("Choice 2: Try to outsmart the goblins using cunning tactics.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} engages in a full-on battle with the goblins.")
        if "Combat" in skills:
            display_with_pause("You successfully defeat the goblins, but your health is significantly reduced.")
        else:
            display_with_pause("The goblins overpower you, and you are forced to flee, leaving behind valuable items.")
    elif decision == "2":
        display_with_pause(f"{player_name} tries to outsmart the goblins using cunning tactics.")
        if "Tactics" in skills:
            display_with_pause("You outwit the goblins and recover the stolen artifact without a fight.")
        else:
            display_with_pause("Your lack of tactics leads to a confrontation with the goblins.")

# Scenario 3: The Fabled City of Etherea - The Mysterious Shopkeeper
def mysterious_shopkeeper():
    global skills, inventory

    display_with_pause("\nChapter 2: The Fabled City of Etherea\n")
    display_with_pause("Scenario 1: The Mysterious Shopkeeper\n")
    display_with_pause(f"Upon reaching the city of Etherea, {player_name} encounters a peculiar shop filled with mystical items.")
    
    display_with_pause("\nChoice 1: Buy a rare health potion from the shopkeeper.")
    display_with_pause("Choice 2: Try to negotiate with the shopkeeper for a better deal.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} buys a rare health potion from the shopkeeper.")
        if "Bargaining" in skills:
            display_with_pause("The shopkeeper offers you a discount and reveals valuable information about a hidden treasure.")
        else:
            display_with_pause("The potion turns out to be a fake, and you've wasted your coins.")
    elif decision == "2":
        display_with_pause(f"{player_name} tries to negotiate with the shopkeeper for a better deal.")
        if "Bargaining" in skills:
            display_with_pause("The shopkeeper refuses to negotiate and becomes hostile, forcing you to leave empty-handed.")
        else:
            display_with_pause("The shopkeeper respects your diplomacy and gives you a quest to recover a stolen artifact from cunning goblins.")

# Scenario 4: The Fabled City of Etherea - The Underground Catacombs
def underground_catacombs():
    global skills, inventory

    display_with_pause("\nChapter 2: The Fabled City of Etherea\n")
    display_with_pause("Scenario 2: The Underground Catacombs\n")
    display_with_pause(f"While exploring the city, {player_name} stumbles upon the entrance to the mysterious catacombs beneath Etherea.")

    display_with_pause("\nChoice 1: Venture into the catacombs to uncover its secrets.")
    display_with_pause("Choice 2: Decide to avoid the catacombs and explore other areas of the city.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} ventures into the catacombs to uncover its secrets.")
        if "Curiosity" in skills:
            display_with_pause("You find ancient relics and treasures that will aid you on your journey.")
            inventory.append("Ancient Relics")
        else:
            display_with_pause("The catacombs prove to be too dangerous, and you get lost, having to fight your way back to the surface.")
    elif decision == "2":
        display_with_pause(f"{player_name} decides to avoid the catacombs and explore other areas of the city.")
        if "Resourcefulness" in skills:
            display_with_pause("You find a powerful ally or gain valuable information from the city's inhabitants.")
        else:
            display_with_pause("Ignoring the catacombs leads to missing vital clues that could have helped you in a future encounter.")

# Scenario 5: The Shadow Realm - Confrontation with the Shadow Guardian
def shadow_guardian():
    global skills

    display_with_pause("\nChapter 3: The Shadow Realm\n")
    display_with_pause("Scenario 1: Confrontation with the Shadow Guardian\n")
    display_with_pause(f"The protagonist discovers that they must pass through the treacherous Shadow Realm to progress further in their quest.")

    display_with_pause("\nChoice 1: Confront the Shadow Guardian head-on.")
    display_with_pause("Choice 2: Attempt to sneak past the Shadow Guardian.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} decides to confront the Shadow Guardian head-on.")
        if "Courage" in skills:
            display_with_pause("You engage in an epic battle, and if victorious, you gain the Guardian's respect and are granted passage.")
        else:
            display_with_pause("The Shadow Guardian proves too powerful, and you are banished from the realm, losing precious time.")
    elif decision == "2":
        display_with_pause(f"{player_name} attempts to sneak past the Shadow Guardian.")
        if "Stealth" in skills:
            display_with_pause("Your stealth skills succeed, and you pass through the realm unnoticed, preserving your strength for later challenges.")
        else:
            display_with_pause("You're caught by the Guardian, and it curses you, reducing your abilities temporarily.")

# Scenario 6: The Shadow Realm - The Crystal Caves
def crystal_caves():
    global skills, inventory

    display_with_pause("\nChapter 3: The Shadow Realm\n")
    display_with_pause("Scenario 2: The Crystal Caves\n")
    display_with_pause(f"Inside the Shadow Realm, {player_name} discovers the Crystal Caves, guarded by malevolent spirits.")
    
    display_with_pause("\nChoice 1: Purify the crystals with a blessed artifact.")
    display_with_pause("Choice 2: Engage in combat with the malevolent spirits.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} purifies the crystals with a blessed artifact.")
        if "Purification" in skills:
            display_with_pause("The spirits are pacified, and you gain the favor of the realm's benevolent beings.")
        else:
            display_with_pause("The artifact fails to work, and the spirits attack, leaving you severely weakened.")
    elif decision == "2":
        display_with_pause(f"{player_name} decides to engage in combat with the malevolent spirits.")
        if "Combat" in skills:
            display_with_pause("You manage to defeat the spirits, but it takes a toll on your health and resources.")
        else:
            display_with_pause("The spirits overpower you, and you must find an alternate path out of the caves, avoiding the risk of further confrontation.")

# Scenario 7: The Timeless Plains - The Time Traveling Watchmaker
def time_traveling_watchmaker():
    global skills, inventory

    display_with_pause("\nChapter 4: The Timeless Plains\n")
    display_with_pause("Scenario 1: The Time Traveling Watchmaker\n")
    display_with_pause(f"In the Timeless Plains, {player_name} meets a mysterious watchmaker who can manipulate time.")
    
    display_with_pause("\nChoice 1: Ask the watchmaker to teach you the art of time manipulation.")
    display_with_pause("Choice 2: Buy a time-manipulating device from the watchmaker.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} asks the watchmaker to teach him the art of time manipulation.")
        if "Time Manipulation" in skills:
            display_with_pause("You gain the ability to rewind time during difficult encounters, giving you a strategic advantage.")
        else:
            display_with_pause("The watchmaker refuses to share his knowledge, and you must find another way to overcome upcoming challenges.")
    elif decision == "2":
        display_with_pause(f"{player_name} buys a time-manipulating device from the watchmaker.")
        if "Time Device" in inventory:
            display_with_pause("The device proves useful in critical situations, allowing you to skip past dangerous encounters.")
        else:
            display_with_pause("The device malfunctions and transports you to an even more perilous location.")

# Scenario 8: The Timeless Plains - The Eternal Guardian
def eternal_guardian():
    global skills

    display_with_pause("\nChapter 4: The Timeless Plains\n")
    display_with_pause("Scenario 2: The Eternal Guardian\n")
    display_with_pause(f"As {player_name} progresses through the Timeless Plains, he encounters a powerful guardian who controls the fabric of reality.")
    
    display_with_pause("\nChoice 1: Attempt to defeat the guardian through brute force.")
    display_with_pause("Choice 2: Try to reason with the guardian, seeking its wisdom.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} attempts to defeat the guardian through brute force.")
        if "Courage" in skills:
            display_with_pause("You engage in a breathtaking battle of cosmic powers, emerging victorious and gaining celestial abilities.")
        else:
            display_with_pause("The guardian overwhelms you with its cosmic might, leaving you battered and lost in the cosmos.")
    elif decision == "2":
        display_with_pause(f"{player_name} tries to reason with the guardian, seeking its wisdom.")
        if "Wisdom" in skills:
            display_with_pause("The guardian reveals crucial information that will lead to a specific ending in the game.")
        else:
            display_with_pause("The guardian remains cryptic and dismissive, leaving you to navigate the mysteries on your own.")

# Scenario 9: The Elemental Peaks - The Elemental Trials
def elemental_trials():
    global skills

    display_with_pause("\nChapter 5: The Elemental Peaks\n")
    display_with_pause("Scenario 1: The Elemental Trials\n")
    display_with_pause(f"Upon reaching the Elemental Peaks, {player_name} encounters trials set forth by the elemental spirits.")
    
    display_with_pause("\nChoice 1: Embrace the elemental trials, proving your worth to the spirits.")
    display_with_pause("Choice 2: Choose to bypass the trials and find an alternative route.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} decides to embrace the elemental trials and prove his worth to the spirits.")
        if "Elemental Prowess" in skills:
            display_with_pause("You gain the respect of the elemental spirits, granting you elemental powers for future encounters.")
        else:
            display_with_pause("The trials prove too demanding, and you fail, leading to a confrontation with enraged spirits.")
    elif decision == "2":
        display_with_pause(f"{player_name} chooses to bypass the trials and find an alternative route.")
        if "Resourcefulness" in skills:
            display_with_pause("You discover a hidden passage that offers a shortcut through the peaks, avoiding potential dangers.")
        else:
            display_with_pause("Ignoring the trials results in missing out on powerful elemental abilities and resources.")

# Scenario 10: The Elemental Peaks - The Legendary Phoenix
def legendary_phoenix():
    global skills

    display_with_pause("\nChapter 5: The Elemental Peaks\n")
    display_with_pause("Scenario 2: The Legendary Phoenix\n")
    display_with_pause(f"Deep within the Elemental Peaks, {player_name} comes across the legendary Phoenix, an ancient and wise creature.")
    
    display_with_pause("\nChoice 1: Seek the Phoenix's guidance for the upcoming challenges.")
    display_with_pause("Choice 2: Attempt to forge a bond with the Phoenix to gain its powers.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} seeks the Phoenix's guidance for the upcoming challenges.")
        if "Insight" in skills:
            display_with_pause("The Phoenix imparts valuable advice, enhancing your chances of reaching a particular ending.")
        else:
            display_with_pause("The Phoenix refuses to help, claiming that the path ahead must be forged without outside interference.")
    elif decision == "2":
        display_with_pause(f"{player_name} attempts to forge a bond with the Phoenix to gain its powers.")
        if "Phoenix's Bond" in skills:
            display_with_pause("You successfully bond with the Phoenix, granting you the ability to resurrect once during your journey.")
        else:
            display_with_pause("The Phoenix rejects your bond, leaving you vulnerable to future fatal encounters.")

# Scenario 11: The Celestial Spire - Ascending the Celestial Spire
def celestial_spire():
    global skills, inventory

    display_with_pause("\nChapter 6: The Celestial Spire\n")
    display_with_pause("Scenario 1: Ascending the Celestial Spire\n")
    display_with_pause(f"As {player_name} approaches the Celestial Spire, he must ascend its treacherous heights to reach its peak.")
    
    display_with_pause("\nChoice 1: Scale the spire through daring acrobatics and climbing skills.")
    display_with_pause("Choice 2: Use an ancient floating elevator within the spire.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} decides to scale the spire through daring acrobatics and climbing skills.")
        if "Agility" in skills:
            display_with_pause("Your skillful ascent grants you a view of the world, uncovering new locations and potential allies.")
        else:
            display_with_pause("The climb proves too perilous, and you risk falling, causing significant injuries.")
    elif decision == "2":
        display_with_pause(f"{player_name} uses an ancient floating elevator within the spire.")
        if "Elevator Key" in inventory:
            display_with_pause("The elevator transports you safely to the peak, saving your strength for the challenges ahead.")
        else:
            display_with_pause("The elevator malfunctions, leaving you stranded, forcing you to find an alternative way up.")

# Scenario 12: The Celestial Spire - The Celestial Guardian
def celestial_guardian():
    global skills

    display_with_pause("\nChapter 6: The Celestial Spire\n")
    display_with_pause("Scenario 2: The Celestial Guardian\n")
    display_with_pause(f"Upon reaching the Celestial Spire's peak, {player_name} encounters the Celestial Guardian, a being of cosmic power.")
    
    display_with_pause("\nChoice 1: Offer to aid the Celestial Guardian in its celestial duties.")
    display_with_pause("Choice 2: Engage the Celestial Guardian in a cosmic duel.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} offers to aid the Celestial Guardian in its celestial duties.")
        if "Cosmic Duty" in skills:
            display_with_pause("The Guardian grants you cosmic knowledge, unlocking hidden lore and potential for a specific ending.")
        else:
            display_with_pause("The Guardian sees your offer as an insult, attacking you for your audacity.")
    elif decision == "2":
        display_with_pause(f"{player_name} decides to engage the Celestial Guardian in a cosmic duel.")
        if "Cosmic Power" in skills:
            display_with_pause("You engage in a breathtaking battle of cosmic powers, emerging victorious and gaining celestial abilities.")
        else:
            display_with_pause("The Guardian overwhelms you with its cosmic might, leaving you battered and lost in the cosmos.")

# Scenario 13: The Forgotten Crypts - The Enigmatic Crypt Keeper
def forgotten_crypts():
    global skills

    display_with_pause("\nChapter 7: The Forgotten Crypts\n")
    display_with_pause("Scenario 1: The Enigmatic Crypt Keeper\n")
    display_with_pause(f"In the Forgotten Crypts, {player_name} encounters the enigmatic crypt keeper, who guards the secrets of the ancients.")
    
    display_with_pause("\nChoice 1: Seek the crypt keeper's wisdom.")
    display_with_pause("Choice 2: Attempt to steal the crypt keeper's hidden knowledge.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} decides to seek the crypt keeper's wisdom.")
        if "Ancient Knowledge" in skills:
            display_with_pause("The crypt keeper imparts profound knowledge about the past, present, and future, affecting your choices in the game.")
        else:
            display_with_pause("The crypt keeper cryptically warns you of dangers ahead without providing substantial information.")
    elif decision == "2":
        display_with_pause(f"{player_name} attempts to steal the crypt keeper's hidden knowledge.")
        if "Thievery" in skills:
            display_with_pause("You successfully obtain forbidden knowledge, gaining a tactical advantage for future encounters.")
        else:
            display_with_pause("The crypt keeper catches you, placing a powerful curse on you that hampers your abilities.")

# Scenario 14: The Forgotten Crypts - The Eternity Gauntlet
def eternity_gauntlet():
    global skills, inventory

    display_with_pause("\nChapter 7: The Forgotten Crypts\n")
    display_with_pause("Scenario 2: The Eternity Gauntlet\n")
    display_with_pause(f"Deep within the Forgotten Crypts, {player_name} finds the Eternity Gauntlet, a relic capable of bending reality.")
    
    display_with_pause("\nChoice 1: Embrace the power of the Eternity Gauntlet.")
    display_with_pause("Choice 2: Choose to leave the Eternity Gauntlet untouched.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} decides to embrace the power of the Eternity Gauntlet.")
        if "Reality Manipulation" in skills:
            display_with_pause("The gauntlet grants you godlike powers temporarily, allowing you to alter reality and shape your destiny.")
        else:
            display_with_pause("The immense power of the gauntlet overwhelms you, causing you to lose control and face dire consequences.")
    elif decision == "2":
        display_with_pause(f"{player_name} chooses to leave the Eternity Gauntlet untouched.")
        if "Wisdom" in skills:
            display_with_pause("Respecting the artifact's power grants you a hidden blessing from the crypt keeper, bolstering your abilities.")
        else:
            display_with_pause("Ignoring the gauntlet leads to missing out on an opportunity to change the course of your journey.")

# Scenario 15: The Final Showdown - The Ultimate Confrontation
def final_showdown():
    global skills

    display_with_pause("\nChapter 8: The Final Showdown\n")
    display_with_pause("Scenario: The Ultimate Confrontation\n")
    display_with_pause(f"Finally, {player_name} reaches the climax of the journey and faces the ultimate antagonist threatening Aetheria.")

    display_with_pause("\nChoice 1: Engage in a full-scale battle to save Aetheria.")
    display_with_pause("Choice 2: Attempt to reason with the antagonist, seeking a peaceful resolution.")

    decision = get_input("Enter your choice (1/2): ")

    if decision == "1":
        display_with_pause(f"{player_name} decides to engage in a full-scale battle to save Aetheria.")
        if "Heroic Prowess" in skills or 'Combat' in skills or 'Courage' in skills:
            display_with_pause("You engage in an epic battle, leading to multiple possible outcomes based on your choices and abilities.")
            # Start the boss fight
            boss_name = "Morgana"
            boss_health = 100
            player_health = 100
            player_attack = 25
            if boss_battle(boss_name, boss_health, player_health, player_attack):
                display_with_pause("Congratulations! You have defeated Morgana and saved Aetheria!")
                skills.append('Victory')
            else:
                display_with_pause("Despite your best efforts, Morgana proves too powerful, and Aetheria falls into darkness.")
                skills.append('Defeated')
        else:
            display_with_pause("Despite your best efforts, you struggle to defeat the antagonist, leading to a potentially bittersweet ending.")
    elif decision == "2":
        display_with_pause(f"{player_name} attempts to reason with the antagonist, seeking a peaceful resolution.")
        if "Diplomacy" in skills:
            display_with_pause("Your diplomatic efforts lead to a surprising twist, uncovering a hidden truth and potential for a unique ending.")
            skills.append('Victory')
        else:
            display_with_pause("The antagonist remains unyielding, forcing you into a difficult final confrontation.")
            skills.append('Defeated')



# Conclusion - Multiple Endings
def conclusion():
    global skills

    display_with_pause(f"Congratulations, {player_name}! Your journey through Aetheria has come to an end.")
    display_with_pause("Your choices, skills, and interactions throughout the adventure have shaped the outcome of your story.")
    display_with_pause("Depending on your decisions, you may have unlocked multiple endings, each with its own significance.")
    display_with_pause("Thank you for playing 'The Chronicles of Aetheria'!")


# Main function to initiate the game
def main():
    global player_name, friend_names, inventory, skills

    display_with_pause("Welcome to 'The Chronicles of Aetheria', an epic text-based adventure!")
    player_name = get_input("Enter your character's name: ")
    
    display_with_pause(f"Welcome, {player_name}! Prepare yourself for a journey into the mystical world of Aetheria.")
    display_with_pause("Throughout your adventure, you'll face challenges, make choices, and uncover ancient secrets.")
    display_with_pause("As you progress, your skills and choices will influence the outcome of your story.")

    # Friend Names
    friend_names.append(get_input("\nEnter the name of your first friend: "))
    friend_names.append(get_input("Enter the name of your second friend: "))

    display_with_pause(f"\nYou are joined by {friend_names[0]} and {friend_names[1]}, your loyal companions in this quest.")
    display_with_pause("Together, you embark on a journey that will determine the fate of Aetheria.")

    # Initial Skills
    display_with_pause("\nBefore we begin, you can select three initial skills that will aid you on your journey.")
    display_with_pause("Choose from the following skills:\n")

    available_skills = [
        "Courage", "Diplomacy", "Combat", "Tactics", "Resourcefulness",
        "Stealth", "Purification", "Bargaining", "Agility", "Insight",
        "Elemental Prowess", "Wisdom", "Time Manipulation", "Thievery", "Reality Manipulation"
    ]

    for i, skill in enumerate(available_skills, start=1):
        print(f"{i}. {skill}")

    while len(skills) < 3:
        try:
            choice = int(get_input(f"\nChoose skill {len(skills) + 1} (enter the corresponding number): "))
            if 1 <= choice <= len(available_skills):
                selected_skill = available_skills[choice - 1]
                if selected_skill not in skills:
                    skills.append(selected_skill)
                    display_with_pause(f"You have chosen '{selected_skill}' as one of your skills.")
                else:
                    display_with_pause("You've already selected that skill. Please choose a different one.")
            else:
                display_with_pause("Invalid input. Please enter the number corresponding to your chosen skill.")
        except ValueError:
            display_with_pause("Invalid input. Please enter the number corresponding to your chosen skill.")

    # Introduction and Scenarios
    display_character_info()
    display_with_pause("\nYour journey begins now. Prepare to face the challenges that await you in Aetheria.")
    dragon_lair()
    goblin_ambush()
    mysterious_shopkeeper()
    underground_catacombs()
    shadow_guardian()
    crystal_caves()
    time_traveling_watchmaker()
    eternal_guardian()
    elemental_trials()
    legendary_phoenix()
    celestial_spire()
    celestial_guardian()
    forgotten_crypts()
    eternity_gauntlet()
    final_showdown()

    # Conclusion and Endings
    display_character_info()
    hero_legacy()
    print()
    conclusion()

if __name__ == "__main__":
    main()
