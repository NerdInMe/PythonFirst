#1. Write a code segment that opens a file named file.txt for input and prints the number of lines in that file.
with open("file.txt", "r") as file:
    content = file.read()
count = content.count('\n')
print("Number of lines:", count + 1)  # Adding 1 to count the last line if it doesn't end with a newline character
#2. Write a code segment that opens a file for input and prints the number of five-letter words in the file.

content_list = content.split()
five_letter_count = 0   
for word in content_list:
    if len(word) == 5:
        print(word)
        five_letter_count += 1
print("Number of five-letter words:", five_letter_count)

#3. Write a code segment that prints the names of all the items in the current working directory.
import os 
print("All items in current directory:")
print(os.listdir('.'))

#4. Write a code segment that prompts the user for a file. If the file does not exist then the program should print an error.
#Otherwise, the program should print its contents.
print("which file you want to read?")
file_name = input().strip()
if os.path.isfile(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
else:
    print("File does not exist.")

#5. Create a file called accounts.txt and enter the following information in the file
with open("accounts.txt", "w") as file:
    file.write(f"100 Mary 34.58\n 200 Alison 345.67\n300 Marc 3.00\n400 Zoltar -32.16\n500 Kathleen 24.32\n")

#6. Read the file and replace Zoltar with Robert
with open("accounts.txt", "r") as file:
    content = file.read()
    new_content = content.replace("Zoltar", "Robert")

#6.  Create a temp file with the new data
temp_file_path = 'accounts_temp.txt'
with open(temp_file_path, 'w') as temp:
    temp.write(new_content)

# Remove the original file
os.remove('accounts.txt')

# Rename the tempfile to myaccounts.txt (overwrite if it already exists)
# os.replace will atomically move and replace the destination if needed.
os.replace(temp_file_path, 'myaccounts.txt')

print("File updated successfully!")