def selection_sort(arr: list[int]) -> list[int]:
    arr = arr.copy()
    if len(arr) < 2:
        return arr
    
    if not all(isinstance(x,int) for x in arr):
        raise TypeError('All elements must be of type: int')
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

# Test cases for selection_sort

print(selection_sort([]))                    # Empty list: []
print(selection_sort([1]))                   # Single element: [1]
print(selection_sort([5, 5, 5, 5]))          # All identical: [5, 5, 5, 5]
print(selection_sort([1, 2, 3, 4, 5]))       # Already sorted: [1, 2, 3, 4, 5]
print(selection_sort([5, 4, 3, 2, 1]))       # Reverse sorted: [1, 2, 3, 4, 5]
print(selection_sort([3, 1, 4, 1, 5, 9]))    # Random order with duplicates: [1, 1, 3, 4, 5, 9]
print(selection_sort([-2, -5, 0, 3, 1]))     # Includes negatives: [-5, -2, 0, 1, 3]
print(selection_sort([2, 3, 2, 1, 3]))       # Duplicates: [1, 2, 2, 3, 3]