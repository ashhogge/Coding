"""
Ashton Hogge

Comment: Only one outcome from all the choices is what I would consider the correct outcome. All others lead to nothing.
"""

print("You are traveling through the forest when you hear a yell in the forest. Do you INVESTIGATE or LEAVE?")

choice = input().upper()

if choice == "INVESTIGATE":
    print("You see a man getting robbed, and the attackers see you coming closer. The man yells for your help! Do you HELP or RUN?")
    choice = input().upper()

    if choice == "HELP":
        print("You rush to the man's aid, scaring away the attackers. The man thanks you for saving him then hands you a map and points behind you. You turn and look, but when you turn back around the man has vanished. Do you go in that direction and follow the MAP, or go to TOWN?")
        choice = input().upper()
        if choice == "MAP":
            print("You follow the direction and map, and find a chest full of gold hidden in the root of a tree! You're rich!")
        elif choice == "TOWN":
            print("You head to town, and decide to give the map away to someone else. A few weeks later, you hear that man found treasure.")
        else:
            print("Invalid Choice.")

    elif choice == "RUN":
        print("You quickly turn around and flee from the scene, leaving the man to fend for himself. You hear the attackers following you. Do you try to HIDE, FIGHT, or try to RUN?")
        choice = input().upper()
    
        if choice == "HIDE":
            print("You hide behind a tree and see them walking past you. You accidently step on a branch, alerting them. Do you FIGHT or RUN?")
            if choice == "FIGHT":
                print ("You attempt to fight, but are getting overpowered by them. Right as you are about to take a final blow, "
                       "you see the man who was being attacked throwing a fireball at them. The attackers, being burned now, run off. You look back up and the man has vanished.")
            elif choice == "RUN":
                print("You run as fast as you can toward the nearest town. You do not hear them anymore and have escaped.")
        
        if choice == "FIGHT":
            print("You turn back around and attempt to fight the attackers. You see that there are five of them, and are able to hold off three. As they are about to finish you off, " 
                  "you teleport to where the man was being attacked and see him. When you blink and open your eyes again, the man is gone. Do you LOOK into where he went, or LEAVE?")
            choice = input().upper()
            if choice == "LOOK":
                print("You go to where he was, and can feel a magical aura about the spot he was in. " 
                    "You can hear the attackers walking back in your direction, so you run toward the nearest town and escape.")
            if choice == "LEAVE":
                print("You don't question where he went and decide it is best to get out of here before the attackers show back up. You head towards the nearest town and have escaped.")
        
        if choice == "RUN":
            print("You attempt to run from the attackers, but trip over a tree branch. They catch up to you and swing a sword at you. " 
                  "Do you try to DODGE the attack or try to BLOCK it with your bag?")
            choice = input().upper()
            if choice == "DODGE":
                print("You dodge the attack, but get a slight cut on your leg. Do you FIGHT back, or attempt to RUN again?")
                choice = input().upper()
                if choice == "FIGHT":
                    print("You grab a tree branch nearby and land a solid blow to one of the attackers. You see four more running toward you, so you run away. You have escaped the attack.")
                if choice == "RUN":
                    print("You run as fast as you can from the man, and manage to escape. You go to the nearest town and are safe.")
            if choice == "BLOCK":
                print("You successfully block the attack with your bag, and get an opportunity to run. " 
                      "You see four others running your direction when they all vanish in front of you. "
                      "You don't know where they went, but you do know that you are finally safe.")

    else:
        print("Invalid choice.")

# Leaving choice starts here
elif choice == "LEAVE":
    print("You leave and hear rustling in the bushes coming closer to you. Do you HIDE or STAND your ground?")
    choice = input().upper()

    if choice == "HIDE":
        print("You find a hiding spot and wait silently. You peek out of the spot and see a group of five walking past. You hear them talk about a map they just obtained. Do you REVEAL yourself, or continue to HIDE?")
        choice = input().upper()
        if choice == "REVEAL":
            print("The men turn around and see you. As you ask them about the map they were talking about, a fireball comes out of nowhere and burns all five of them. A man who looks a little beat up appears, and takes the map. He looks at you, then vanishes.")
        elif choice == "HIDE":
            print("The group walks by and do not notice you.")
            
    elif choice == "STAND":
        print("You decide to stand your ground, ready to face whatever comes your way. A man walks towards you while looking at a map. He doesn't seem to notice you yet. Do you ALERT him or SURPRISE attack him?")
        choice = input().upper()
        if choice == "ALERT":
            print("The man looks up, then vanishes away in an instant. There are no physical traces of where he went.")
        elif choice == "SURPRISE":
            print("You surprise the man as he walks by and attack him. He gets knocked unconcious. You find a map on him, but the map makes no sense. You get a bad feeling and decide to run.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")
