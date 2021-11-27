"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title : program to print smallest number from the list
"""
"""
Description:
            declare a list of tuples.
           The function last returns the last element of each tuple in the list of tuples.
         The function sort returns the sorted list with the last function as its key.
          The sorted list is then printed.



Parameter:
      
Return:
"""
def last(n):
    return n[-1]  
 
def sort(tuples):
    return sorted(tuples, key=last)
 
mylist=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("list of tuple is Sorted:")
print(sort(mylist))
