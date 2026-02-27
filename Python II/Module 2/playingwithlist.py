#Q1. To sort a list in descending order, call list method 
# sort with the optional keyword argument ____ set to True.
my_list = ["z","a","g","p","b","h","n","k","e","l"]
my_list.sort(reverse=True)
print(my_list)

#Q2. Insert 10 random letters in the range ‘a’ through ‘z’ 
# into a list. Perform the following tasks and 
# display your results
my_list = ["z","a","g","a","b","h","n","k","e","k"]
# a. Sort the list in ascending order
my_list.sort()
print(f"Ascending order: {my_list}")
# b. Sort the list in descending order
my_list.sort(reverse=True)
print(f"Descending order:, {my_list}")
# c. Get the unique values sort them in ascending order
unique_list = list(set(my_list))
unique_list.sort()
print(f"Unique values in ascending order: {unique_list}")