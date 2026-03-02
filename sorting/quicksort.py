def quick_sort(arr,start,end):
    if start >= end:
        return
    
    pivot = partition(arr,start,end)
    
    quick_sort(arr,start,pivot-1)
    quick_sort(arr,pivot+1,end)

def partition(arr,start,end):
    pos = start
    for i in range(start,end+1):
        if arr[i] <= arr[end]:
            arr[i],arr[pos] = arr[pos],arr[i]
            pos += 1
    return pos-1

arr = [23,242,1,12,3]
quick_sort(arr,0,len(arr)-1)
print(arr)