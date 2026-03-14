### Assignment 4: Dice Roller
### Author: Niyati Jain
#!/usr/bin/env python3
import random

#function to display the title
def display_title():
    print("Welcome to Dice Roller!")

#function to return the random number between 1 & 6
def roll():
    return random.randint(1,6)

#function to roll the dice twice and calculate total and print the dice rolls
def roll_dice():
    if(input("Roll the dice?(y/n)").lower() == "y"):
        while True:
            roll_1 = roll()
            roll_2 = roll()
            total = roll_1 + roll_2
            print("Die 1:",roll_1)
            print("Die 2:",roll_2)
            print("Total:",total)
            if(total == 2):
                print("Snake eyes!")
            if(total == 12):
                print("Boxcars!")
            if(input("Roll again?(y/n)").lower() == "y"):
                continue
            else:
                break

def main():
    display_title()
    roll_dice()

if __name__ == "__main__":
    main()
