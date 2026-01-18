
def quick_sort(arr:list[float])-> list[float]:
    start = 0
    end = len(arr) - 1
    quick_sort_helper(arr,start,end)
    return arr


def quick_sort_helper(arr:list[float],start:int,end:int):
    if start >= end:
        return arr
    pivot = partition(arr,start,end)
    quick_sort_helper(arr,start,pivot-1)
    quick_sort_helper(arr,pivot+1,end)


def partition(arr:list[float],start:int,end:int)-> int:
    pivot = arr[end]
    i = start - 1
    for j in range(start,end):
        if arr[j] <= pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1
    
