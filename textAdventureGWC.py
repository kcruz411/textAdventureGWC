strength = 10
strenth = int(strength)
name = input("Hi! What's your name?")
print("Alright, ", name, ". Welcome to Text Adventure.")
print("Strength level = ", strength)
print("You were hiking on a normal Saturday and decided to leave the trail.")
print("You quickly find that you're lost and the sun is setting quick.")
print("You must find shelter!")

LR = input("Which way do you want to walk? LEFT or RIGHT?")
if(LR == "left"):
    print("Look! A cave!")
    strength -= 2
    print("Strength level = ", strength)
elif(LR == "right"):
    print("You continue to wander the woods, and soon, you feel like your walking in cirlces.")
    print("Days and nights pass. You're still lost.")
    strength = 0
    print("Strength level = ", strength)
    print("Game Over!")
    exit()

print("You continue walking, and you notice there is a small opening.")

inout = input("Would you like to ENTER the cave or CONTINUE walking in the woods?")
if(inout == "enter"):
    print("'Hello?' you shout into the cave. Silence answers.")
    print("With caution, you proceed into the cave.")
elif(inout == "continue"):
    print("You continue to walk for what seems like forever. Finally, you hear a voice and a light reflects off a glowing object.")
    print("'", name, ", I am here to help you,'says the object.")
    angel = input("Should you STAY and listen or RUN away?")
    if(angel == "run"):
        print("You sprint for your life and fall to your knees as you feel you ankles give out from under you.")
        strength = 3
        print("Strength level = ", strength)
        print("Your heart beats quickly in your chest as you realize slowly that you've made a mistake.")
        strength = 0
        print("Strength level = ", strength)
        print("Game Over!")
        exit()
    elif(angel == "stay"):
        print("The object stops glowing suddenly to reveal an angel. 'Um, what the-' you manage to stutter out.")
        print("The angel grabs your hand, and he leads you to a road.")
        print("You've made it out of the woods!")
        print("You won!")
        exit()

print("You suddenly feel a presence looming over you in the dark. Shaking, you reach your hand out to discover a warm, fuzzy grizzly bear.")
print("The grizzly bear roars, and you scream.")
bear = input("Do you want to FIGHT or RUN?")
if(bear == "fight"):
    print("Determination and adrenaline fills your body.")
    strength = 9
    print("Strength level = ", strength)
elif(bear == "run"):
    print("The bear runs after you. You look behind you to see him right behind your back.")
    print("It grabs your torso to prevent you from moving. Quickly, the bear bites down.")
    strength = 0
    print("Strength level = ", strength)
    print("Game Over!")
    exit()

weapon = input("Choose your weapon: SLAP, ROCK, or STICK?")
if(weapon == "slap"):
    print("You raise your hand and hit the bear's face as hard as you can.")
    print("The bear grabs your torso to prevent you from moving. Quickly, the bear bites down.")
    strength = 0
    print("Strength level = ", strength)
    print("Game Over!")
    exit()
elif(weapon == "rock" or "stick"):
    strength1 = 5
    strength1 = int(strength1)
    while (strength1 > 0):
        print("You throw the object, aiming at the eye, and the bear whimpers.")
        print("The bear raises its paw and claws your arm.")
        strength -= 1
        print("Strenth Level = ", strength)
        print("Bear Stregnth = ", strength1)
        strength1 -= 1
    print("You've killed the bear.")

print("You run away from the body of the bear.")
print("You find 3 openings.")
open = input("Which opening do you want to proceed into? 1, 2, or 3?")
if(open == "1" or "3"):
    print("You find a shaky bridge.")
    print("As yo uwalk slowly over the wooden bridge, a piece of wood under you breaks.")
    print("You try to grab the railing, but its too late.")
    print("You've fallen to your death.")
    Strength = 0
    print("Strength level = ", strength)
    print("Game Over!")
    exit()
elif(open == "2"):
    print("You find a glass bridge.")
    print("Grabbing the railing, you slowly make your way over.")
    print("You notice a little bit of light coming from the of the bridge.")
    print("You gain more confidence with each step")
    strength += 1
    print("Strength level = ", strength)
    print("You take one last step off the bridge and step onto a road.")
    print("Looking behind you, you glare at the woods in which you had struggled to leave.")
    print("You've escaped woods! Congratulations, ",name, "! The End.")
    exit()
