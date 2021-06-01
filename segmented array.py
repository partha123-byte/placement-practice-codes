# Sort an array of 0s, 1s and 2s
# Difficulty Level : Medium
# Last Updated : 09 Apr, 2021
# Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
# Examples: 
 

# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}

# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}


a=input()
list=a.split(",")
list1=[]
b=3

   
for i in range(len(list)):
        list1.append(int(list[i]))

if (b in list1):
    print("cannot do swap")
else: 


    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if(list1[j]>list1[j+1]):
                list1[j],list1[j+1]=list1[j+1],list1[j]

    print(list1)

    #solved