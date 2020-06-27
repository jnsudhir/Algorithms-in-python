def bs(arr,L,R,X):
    while L<=R:
        mid = L + (R-1) // 2
        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            L = mid+1
        else:
            R = mid+1
    return -1
arr = list(map(int,input("Enter sorted list:").split()))
X = int(input("enter element to search:"))
result = bs(arr,0,len(arr)-1,X)
if(result==-1):
    print("element is not in the list")
else:
    print("element is at index: ", result)
