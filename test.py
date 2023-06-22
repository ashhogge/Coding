print("You are traveling through the forest when you hear a yell in the forest. Do you INVESTIGATE or LEAVE?")

choice = input().lower()
while choice not in ["investigate", "leave"]:
    print("Invalid choice. Please enter 'INVESTIGATE' or 'LEAVE':")
    choice = input().lower()

if choice == "investigate":
    print("You see a man getting robbed, and the attackers see you coming closer. The man yells for your help! Do you HELP or RUN?")
    choice = input().lower()
    while choice not in ["help", "run"]:
        print("Invalid choice. Please enter 'HELP' or 'RUN':")
        choice = input().lower()

    if choice == "help":
        print("You rush to the man's aid, scaring away the attackers. The man thanks you for saving him then hands you a map and points behind you.")
        print("You turn and look, but when you turn back around the man has vanished. Do you go in that direction and follow the MAP, or go to TOWN?")
        choice = input().lower()
        while choice not in ["map", "town"]:
            print("Invalid choice. Please enter 'MAP' or 'TOWN':")
            choice = input().lower()

        if choice == "map":
            print("You follow the direction and map, and find a chest full of gold hidden in a tree's roots! You're rich!")
        elif choice == "town":
            print("You head to town, and decide to give the map away to someone else. A few weeks later, you hear that man found treasure.")
    elif choice == "run":
        print("You quickly turn around and flee from the scene, leaving the man to fend for himself. You hear the attackers following you. Do you try to HIDE, FIGHT, or try to RUN?")
        choice = input().lower()
        while choice not in ["hide", "fight", "run"]:
            print("Invalid choice. Please enter 'HIDE', 'FIGHT', or 'RUN':")
            choice = input().lower()

        if choice == "hide":
            print("You hide behind a tree and see them walking past you. You accidentally step on a branch, alerting them. Do you FIGHT or RUN?")
            choice = input().lower()
            while choice not in ["fight", "run"]:
                print("Invalid choice. Please enter 'FIGHT' or 'RUN':")
                choice = input().lower()

            if choice == "fight":
                print("You attempt to fight, but are getting overpowered by them. Right as you are about to take a final blow, you see the man who was being attacked throwing a fireball at them. The attackers, being burned now, run off. You look back up and the man has vanished.")
            elif choice == "run":
                print("You run as fast as you can toward the nearest town. You do not hear them anymore and have escaped.")

        elif choice == "fight":
            print("You turn back around and attempt to fight the attackers. You see that there are five of them, and are able to hold off three. As they are about to finish you off, you teleport to where the man was being attacked and see him.\nWhen you blink and open your eyes again, the man is gone. Do you LOOK into where he went, or LEAVE?")
            choice = input
