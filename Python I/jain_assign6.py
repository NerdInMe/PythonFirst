### Assignment 6: Palindrome checker
### Author: Niyati Jain
# Program to find out whether the user inputted string is a palindrome or not
import string
def main():
    while True:
        #Prompt user to input a string
        input_str = input("Enter a string:")    
        #remove punctuation from the string
        for char in string.punctuation:
            input_str = input_str.replace(char, "")
        #remove whitespace from the string
        input_str = input_str.replace(" ", "")
        #check whether string is palindrome or not
        if(input_str == input_str[::-1]):
            print("the string is a palindrome")
        else:
            print("the string is not a palindrome")
        #ask user for checking another string
        if(input("Do you want to check another string? (y/n)").lower() == "y"):
            continue
        else:
            break
    

if __name__ == "__main__":
    main()
