
arr=[1,2,3,4,5]
for i in range(0,len(arr)-1,2):
    if(arr[i]<arr[i+1]):
        k=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=k
        # arr[i],arr[i+1]=arr[i+1],arr[i]  


print(arr)        