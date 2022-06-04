# 1
# Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
   for num in range(num, -1, -1):
      print(num)
countdown(10)

######################################

#2
# Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_return(my_list = []):
   print(my_list[0])
   return my_list[1]

print_return([1, 2])


######################################

#3
# create a function that accepts a list and returns the sum of the first value in the list plus the list's length

def plus_length(num_list = []):
   stored = num_list[0] + len(num_list)
   print(stored)
plus_length([1,2,3,4,5])

######################################

#4
# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

i = 0
second_list = []
def greater_than_second(aList = []):
   for i in range(0, len(aList), 1):
      if aList[i] > aList[1]:
         second_list.append(aList[i])

   print(len(second_list))
   return second_list

greater_than_second([5,2,3,2,1,4])

######################################

#5
# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def len_value(size, value):
   new_list = []
   # new list length should equal size
   # every value in the list should equal value
   for i in range(0, size, 1):
      new_list.append(i)
      new_list[i] = value
      # print(new_list)   --- This was used to ensure it was returning the proper value at the end 
   
   return new_list


len_value(6,2)

