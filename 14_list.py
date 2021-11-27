"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  program common items in a list.
"""
list1=[1,"pune","zee"]
list2=["zee","mumbai",1]
result=(set(list1) & set(list2))
print("common element is :" ,list(result))
