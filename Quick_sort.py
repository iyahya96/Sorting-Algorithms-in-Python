'''def quick_sort(array: list[float], start:int, end:int):
    if start >= end:
        return array
    pivot = partition(array,start,end)
    quick_sort(array,start,pivot-1)
    quick_sort(array,pivot+1,end)


def partition(array:list[float], start:int, end:int) -> int:
    pivot = array[end]
    i = start - 1
    for j in range(start,end):
        if array[j] <= pivot:
            i += 1
            array[j] , array[i] = array[i] , array[j]
    array[i+1] , array[end] = array[end] , array[i+1]
    return i+1'''

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


# Test cases for quick_sort

# Empty list
print(quick_sort([]))  # []

# Single element
print(quick_sort([1.0]))  # [1.0]

# All elements are the same
print(quick_sort([2.0, 2.0, 2.0, 2.0]))  # [2.0, 2.0, 2.0, 2.0]

# Already sorted list
print(quick_sort([1.0, 2.0, 3.0, 4.0]))  # [1.0, 2.0, 3.0, 4.0]

# Reverse sorted list
print(quick_sort([4.0, 3.0, 2.0, 1.0]))  # [1.0, 2.0, 3.0, 4.0]

# List with negative numbers
print(quick_sort([-3.0, -1.0, -2.0, 0.0]))  # [-3.0, -2.0, -1.0, 0.0]

# List with floats and integers
print(quick_sort([1, 2.5, 0, 3.3]))  # [0, 1, 2.5, 3.3]

# Very large list
#print(quick_sort(list(range(1000, 0, -1)), 0, 999))  # [1, 2, ..., 1000]