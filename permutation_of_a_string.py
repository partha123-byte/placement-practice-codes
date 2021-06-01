# Given a string S. The task is to print all permutations of a given string.

 

# Example 1:

# Input: ABC
# Output:
# ABC ACB BAC BCA CAB CBA
# Explanation:
# Given string ABC has permutations in 6 
# forms as ABC, ACB, BAC, BCA, CAB and CBA .


# solution---->



inp=input()


for i in range(len(inp)):
    if(inp[i]==inp[len(inp)-i]):
        continue
    else:
