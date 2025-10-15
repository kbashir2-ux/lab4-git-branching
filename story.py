def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()

    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pick up the sword easily, watching it glisten in the sun.")
    print("Looking to your right you suddenly see a DRAGON.... beetle.")
    print("You squash it, heroicly defeating the vile creature")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
<<<<<<< HEAD

def center_path():
    print(" You head forward and find a regular path.")

=======
    print("You brace yourself for battle")
    print("Suddenly another squirrel jumps from behind you and sticks a gem in your palm")
    print("You feel something pulling inside you......")
    
>>>>>>> villain-path
if __name__ == "__main__":
    intro()
