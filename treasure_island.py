print("welcome to Treasure Island\nyour mission is to find the treasure\n"
      "your at a cross road. Where do you want to go? Type right or left\n")

choice = input().lower()
if choice == "left":
    print("You come to lake. There is an island in the middle of the lake.\n"
          "Type wait to wait for a boat. Type swim to swim cross\n")
    ch1 = input().lower()
    if ch1 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        door = input()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door=="yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")

    else:
        print("You get attacked by an angry crocodile. Game Over.")
else:
    print("You fell into a hole. Game Over.")