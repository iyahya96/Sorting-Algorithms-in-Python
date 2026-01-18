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
