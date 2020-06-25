def search(arr,n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
arr = [12,23,34,45,56,67,78,89]
x = 56
n = len(arr)
result = search(arr,n, x)
if(result == -1):
    print("arr is not listed")
else:
    print("ele is at index:", result)
