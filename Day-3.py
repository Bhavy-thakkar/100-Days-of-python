# Treasurehunt Island Game

print("Welcome to the Treasurehunt Island!!")
side = input("Which side you will go?? Left or Right\n")
if side.lower() == "left":
    print("There are two way.There is a lake.You will swim or you will wait.")
    path = input("What will you do?? Swim or Wait\n")
    if path.lower() == "wait":
        print("There are 3 doors. Red,Green and Blue")
        doors = input("Which door you will open?? Green, Red or Blue\n")
        if doors.lower() == "green":
            print("You found the treasure")
        else:
            print("You have choose the wrong door.GAME OVER!!")
    else:
        print("There are many crocodiles in the lake.GAME OVER!!")
else:
    print("There is nothing, GAME OVER!!")
