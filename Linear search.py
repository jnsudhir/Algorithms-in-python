#taking input from the user
def ls(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1
arr = list(map(int,input("enter array list:").split()))
x = int(input("enter value to search:"))
n = len(arr)
result = ls(arr,n,x)
if(result==-1):
    print("element is not in the list")
else:
    print("elemant is at index", result)
  

