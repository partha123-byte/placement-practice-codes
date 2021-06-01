def transitionPoint(arr, n):
    if(arr[0]==1):
        return 0
    for i in range(len(arr)-1):
        
        if (arr[i]==0):
            continue
        else:
            return i
    if(arr[len(arr)-1]==1):
        return len(arr)-1
            
    return -1 

n=5
arr=list(map(int, input().strip().split() ))
print(transitionPoint(arr, n))