"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  difference the items in a list.
"""
"""
Description: difference() to get the difference between two lists. 
Use set() to convert both lists into sets. Use set. difference(s) 

Parameter:
      
Return:
"""
mylist1=[5,10,20,40]
mylist2=[10,20,12,3]
diff=set(mylist1).difference(set(mylist2))
print("difference is mylist1 - mylist2 =", list(diff))
