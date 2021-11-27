"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Python program to print a specified list after removing the 0th, 4th and 5th element
"""
"""
Description: create a function with list parameter iterate for loop and then print function 
           

Parameter:
      
Return:
"""
list1=['Red','Green','White','Black','Pink','Yellow']
# Expected Output : ['Green', 'White', 'Black']
list1.remove('Red')
list1.remove('Pink')
list1.remove('Yellow')
print(list1)
