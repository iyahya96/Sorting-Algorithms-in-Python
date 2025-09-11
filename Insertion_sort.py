def insertion_sort(arr: list[float]) -> list[float]:
    arr = arr.copy()
    if not isinstance(arr,list):
        raise TypeError('All elements must be list.')
    if len(arr) < 2:
        return arr
    if not all(isinstance(x,int) for x in arr):
        raise TypeError('All elements must be int or float.')
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

print(insertion_sort([4,1,5,3,7,6,2,9,8]))
#Test Cases
print(insertion_sort([]))                    # Empty list: []
print(insertion_sort([1]))                   # Single element: [1]
print(insertion_sort([5, 5, 5, 5]))          # All identical: [5, 5, 5, 5]
print(insertion_sort([1, 2, 3, 4, 5]))       # Already sorted: [1, 2, 3, 4, 5]
print(insertion_sort([5, 4, 3, 2, 1]))       # Reverse sorted: [1, 2, 3, 4, 5]
print(insertion_sort([3, 1, 4, 1, 5, 9]))    # Random order with duplicates: [1, 1, 3, 4, 5, 9]
print(insertion_sort([-2, -5, 0, 3, 1]))     # Includes negatives: [-5, -2, 0, 1, 3]
print(insertion_sort([2, 3, 2, 1, 3]))       # Duplicates: [1, 2, 2, 3, 3]