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

#hi@hi
def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pick up the sword easily, watching it glisten in the sun.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print(" You head forward and find a regular path.")

if __name__ == "__main__":
    intro()


#edits edits edits!!!