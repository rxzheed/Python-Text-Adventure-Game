
print("The Murder Mystery of the Blackwater Tavern\n")

print("Music and laughter echoes through the lodge of the Blackwater Tavern. Drinks flowing, smiles from ear to ear, and strangers lean on each other like old friends. The storm brewing is almost forgotten until a sudden thunderous boom shakes the tavern. Glasses break, windows shake, and the lanterns suddenly go out. Right before the pitch dark, you faintly spot a shadowy figure rushing towards the bar. The lights are all relit, you remember what you saw and sprint to the bar. Blueno, the owner, is in horrendous shape lying unconscious and bleeding. You lockdown the tavern before anyone can still escape, narrowing your focus on Ashe the Security Guard, Marshall the Wallflower, and Kaido the Grunt. Now it’s up to you.\n")

murderer = "kaido"
clue_points = 0

game_over = False

while not game_over:


    print("\nHmm, Who should I investigate first?")
    suspect = input("Ashe, Marshall, or Kaido: ").lower()

    if suspect == "ashe":
        print("Clue: Ashe says she was guarding the door, but no one saw her there.")
        clue_points += 1
    elif suspect == "marshall":
        print("Clue: Marshall looks nervous when you mention the bar, but keeps his filty glaze on you.")
        clue_points += 1
    elif suspect == "kaido":
        print("Clue: Kaido has bruised knuckles but its widely know how he likes to fight.")
        clue_points += 2
    else:
        print("That is not a valid suspect.")


    print("\nWhat should I do next?")
    print("a) Investigate another suspect")
    print("b) Investigate Blueno’s crime scene")
    print("c) Make a final accusation")
    choice = input("Enter a, b, or c: ").lower()

    if choice == "a":
        print("You decide to question another suspect.")
        print("You notice nervous glances and avoidant behavior from the other suspects.")
    elif choice == "b":
        print("You inspect Blueno’s crime scene carefully.")
        print("Clue: A torn piece of fabric is near the shattered lantern.")
        clue_points += 1
    elif choice == "c":
        
        accusation = input("\nWho do you accuse? Ashe, Marshall, or Kaido: ").lower()

        if accusation == murderer:
            print("You were right! They confess. YOU WIN!")
            game_over = True
        else:
            print("Wrong! The culprit is still free. Keep investigating and guessing.")
    else:
        print("That was not a clear choice. Time passes...")
