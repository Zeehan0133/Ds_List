"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title : program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
"""
"""
Description:
           firstly we created one list and initialize counter variable and after that we itrate for loop
           and added condition if no of string satisfied the condition then count it and peint it  

Parameter:
      
Return:
"""
mylist=['abc', 'xyz', 'aba', '1221']
Counter=0
for i in mylist:
    if len(i)>1 and i[0]==i[-1]:
        print("given string is",i)
        Counter+=1
print("matching string is :" , Counter)
