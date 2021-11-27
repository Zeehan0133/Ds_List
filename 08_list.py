"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Python function that takes two lists and returns True if they have at
least one common member.
"""

def common_mem(list1,list2):
    """
    Description: create a function with list parameter iterate for loop and then print function 
    Parameter: list1 and list 2
    Return: result
"""
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result

if __name__=='__main__':               
    print(common_mem([1,2,3,4,5],[5,6,7,8,9]))
