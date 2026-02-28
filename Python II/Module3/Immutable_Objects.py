# Question4: Which of the following are immutable data structures? Why ? Please explain
#dictionaries and lists
#strings and tuples

#dictionaries and lists are mutable data structures because they can be modified after they are created. 
#You can add, remove, or change elements in a dictionary or a list.
#it changes the original list. 
#Similarly, if you change the value of a key in a dictionary, it modifies the original dictionary.
#Note that the key themselves are immutable, but the values can be mutable.

#example: 
my_list = [1, 2, 3]
my_list.append(4)  # This modifies the original list
print(my_list)  # Output: [1, 2, 3, 4]
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # This modifies the original dictionary 
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

#strings and tuples are immutable data structures because they cannot be modified after they are created.
#You cannot change individual characters in a string or elements in a tuple.
#If you try to modify a string or a tuple, you will get an error.
#example:(comment out the below code to avoid error)
my_string = "Niyati"
my_string[0] = 'h'  # TypeError: 'str' object does not support item assignment
my_tuple = (1, 2, 3)  #TypeError: 'tuple' object does not support item assignment      
my_tuple[0] = 4  

# Errors occur because strings and tuples do not allow modification of their contents after they have been created.



