# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:59:51 2022

@author: Rajveer
"""

# Creating the main string variable
string = "I love Python Programming!"

# Question 1 
# Perform a word count
print("The original string is: " + string)
result1 = len(string.split())
print("Answer for Question 1")
print("The total number of words in the string are: " + str(result1) + " words")

# Question 2 
# Use a string count method to count the number of spaces and store the answer in a variable
# Defining a number_of_spaces function which utilizea the count method
def number_of_spaces(string):
    
    count = 0
    
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    return count

print("Answer for Question 2")
print("Total number of spaces: ", number_of_spaces(string))

# Question 3
# Increasing the answers for Question 1 and 2 to 20

# Question 1
print("Answer for Question 3: increase Question 1 to 20")
print(result1)
result2 = len(string.split()) + 16
print("There is a total of 4 words in the string as seen in the output above, after adding 16, we obtain ", result2)

# Question 2
print("Asnwer for Question 3: increase Question 2 to 20")
print(string.count(" "))
result3 = string.count(" ") + 17
print("There are a total of 3 spaces as seen in the output above, after adding 17, we obtain", result3)
