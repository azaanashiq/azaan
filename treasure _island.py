print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
side=input("You\'re at a cross road.Where do you want to go?\n        Type \"left\" or \"right\"\n").lower()
if side=="left":
 water=input("You've come to a lake.There is an island in the middle of the lake.\n    Type \"wait\" to wait for a boat.Type \"swim\" to swim across.\n").lower()
 if water=="wait":
     door=input("You arrive at the island unharmed.There is a house with 3 doors.\n  One red, one yellow and one blue.which colour do you choose?\n").lower()  
     if door=="yellow":
        print("You found the treasure!You Win!")
     elif door=="red":
        print("It's a room full of fire.Game Over.")
     elif door=="blue":
        print("You entered a room of beasts.Game Over.")
 elif water=="swim":
     print("You get attacked by an angry trout.Game Over.")
elif side=="right":
    print("You fell into a hole.Game Over.")
