print("welcome to treasure island")
cross_road = input("your're at the cross road where do you want to go left or right\n")
if cross_road == "left":
    lake = input("you have welcome ton the lake . therev is an insalnd  the middle of the lake \n you type wait to wait for the boat . type swim to swim\n")
    if lake == "wait":
        room = input("You arrive at the island unharmed. There is a house with 3 doors One red, one yellow and one blue. Which colour do you choose?\n")
        if room == "red":
            print("It's a room full of fire. Game Over.")
        if room == "yellow":
            print("You found the treasure! You Win!")
        if room == "blue":
            print("You enter a room of beasts. Game Over.") 
    else:
        print("You get attacked by an angry trout. Game Over.")   

else:
    print("you fell into a hole. game over")