# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example 1:

# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# # much.very.program.this.like.


# solution-------->




inp=input()
list1=inp.split(".")
list2=[]
for i in range(len(list1)):
   list2.insert(0,list1[i])

print(".".join(list2))